import mysql.connector
from mysql.connector import Error
from models.config import DBConfig
from models.model import GamaProducto, Producto


class BaseDAO:
    """
    Clase base para Data Access Objects (DAO) que gestiona la conexión a la base de datos MySQL.

    Proporciona métodos para establecer la conexión, ejecutar consultas y cerrar la conexión.
    Utiliza la configuración de la base de datos almacenada en `DBConfig`.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de BaseDAO y establece la conexión con la base de datos.

        Recupera la configuración de la base de datos de `DBConfig`.
        Lanza un `ValueError` si faltan datos de conexión o un `ConnectionError` si la conexión falla.
        """
        config = DBConfig.get_config()
        db = config.get("db")
        user = config.get("user")
        psw = config.get("psw")
        port = config.get("port")
        host = config.get("host")
        if not all([db, user, psw, port, host]):
            raise ValueError("Faltan datos de conexión a la BD.")

        try:
            self.conn = mysql.connector.connect(
                user=user,
                password=psw,
                port=int(port),
                host=host,
                database=db,
                auth_plugin="mysql_native_password",
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except Error as e:
            raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")

    def execute_query(self, query: str, params: tuple = None, fetch_one: bool = False):
        """
        Ejecuta una consulta SQL en la base de datos.

        Para consultas SELECT, devuelve los resultados. Para otras consultas (INSERT, UPDATE, DELETE),
        confirma la transacción y devuelve el ID de la última fila insertada si aplica.

        Args:
            query (str): La cadena de la consulta SQL a ejecutar.
            params (tuple, optional): Una tupla de parámetros para la consulta, si los hay.
                                      Por defecto es None.
            fetch_one (bool, optional): Si es True, devuelve solo la primera fila de los resultados
                                        para una consulta SELECT. Si es False, devuelve todas las filas.
                                        Por defecto es False.

        Returns:
            list or dict or int or None:
                - Una lista de diccionarios (cada diccionario representa una fila) para consultas SELECT.
                - Un diccionario (la primera fila) si `fetch_one` es True para consultas SELECT.
                - El ID de la última fila insertada para consultas INSERT.
                - None para otras consultas que no devuelven datos (UPDATE, DELETE).
        """
        self.cursor.execute(query, params or ())
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchone() if fetch_one else self.cursor.fetchall()
        else:
            self.conn.commit()
            return self.cursor.lastrowid

    def close(self):
        """
        Cierra el cursor y la conexión a la base de datos.

        Asegura que los recursos de la base de datos se liberen correctamente.
        """
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()

    @staticmethod
    def probar_conexion_con_config() -> bool:
        """
        Intenta establecer una conexión a la base de datos utilizando la configuración global de DBConfig.

        Esta función es útil para verificar la conectividad de la base de datos
        sin la necesidad de instanciar un DAO completo para operaciones de datos.

        Returns:
            bool: True si la conexión se establece exitosamente, False en caso contrario.

        Examples:
            >>> # Configura DBConfig para una conexión de prueba EXITOSA (¡AJUSTA ESTOS VALORES A TU BD!)
            >>> DBConfig.set_config({'db': 'jardineria', 'user': 'root', 'psw': 'root', 'host': 'localhost', 'port': 3307})
            >>> BaseDAO.probar_conexion_con_config()
            True

            >>> # Prueba con configuración INVÁLIDA (usuario/contraseña incorrectos)
            >>> DBConfig.set_config({'db': 'jardineria', 'user': 'usuario_falso', 'psw': 'pass_falso', 'host': 'localhost', 'port': 3307})
            >>> BaseDAO.probar_conexion_con_config()
            False

            >>> # Prueba con base de datos INEXISTENTE
            >>> DBConfig.set_config({'db': 'bd_inexistente', 'user': 'root', 'psw': 'root', 'host': 'localhost', 'port': 3307})
            >>> BaseDAO.probar_conexion_con_config()
            False

            >>> # Prueba con puerto INCORRECTO (si no hay nada escuchando en ese puerto)
            >>> DBConfig.set_config({'db': 'jardineria', 'user': 'root', 'psw': 'root', 'host': 'localhost', 'port': 1234})
            >>> BaseDAO.probar_conexion_con_config()
            False
        """
        try:
            dao = BaseDAO()
            dao.close()
            return True
        except (Error, ValueError, ConnectionError):
            return False


class JardineriaRepository(BaseDAO):
    """
    Repositorio específico para interactuar con las tablas `gama_producto` y `producto`
    de la base de datos de jardinería.

    Hereda la funcionalidad de conexión y ejecución de consultas de `BaseDAO`.
    """

    def get_all(self) -> list[GamaProducto]:
        """
        Obtiene todas las gamas de productos de la base de datos.

        Returns:
            list[GamaProducto]: Una lista de objetos GamaProducto, cada uno representando una gama.
        """
        query = "SELECT * FROM gama_producto"
        rows = self.execute_query(query)
        return [
            GamaProducto(
                row["gama"],
                row["descripcion_texto"],
                row["descripcion_html"],
                row["imagen"],
            )
            for row in rows
        ]

    def get_all_product_gama(self, gama: str) -> list[Producto]:
        """
        Obtiene todos los productos que pertenecen a una gama específica.

        Args:
            gama (str): El nombre de la gama de productos a buscar.

        Returns:
            list[Producto]: Una lista de objetos Producto, cada uno representando un producto
                            de la gama especificada.
        """
        query = "SELECT * FROM producto WHERE gama = %s"
        params = (gama,)
        rows = self.execute_query(query, params)
        productos = []
        for row in rows:
            producto = Producto(
                codigo_producto=row["codigo_producto"],
                nombre=row["nombre"],
                gama=row["gama"],
                dimensiones=row["dimensiones"],
                proveedor=row["proveedor"],
                descripcion=row["descripcion"],
                cantidad_en_stock=row["cantidad_en_stock"],
                precio_venta=row["precio_venta"],
                precio_proveedor=row["precio_proveedor"],
            )
            productos.append(producto)
        return productos
