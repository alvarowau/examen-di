import mysql.connector
from mysql.connector import Error # Asegúrate de que Error está importado
from models.config import DBConfig
from models.model import GamaProducto, Producto

class BaseDAO:
    def __init__(self):
        config = DBConfig.get_config()
        db = config.get("db")
        user = config.get("user")
        psw = config.get("psw")
        port = config.get("port")
        host = config.get("host")
        if not all([db, user, psw, port, host]):
            raise ValueError("Faltan datos de conexión a la BD.")

        # Intentamos conectar a la base de datos
        try:
            self.conn = mysql.connector.connect(
                user=user,
                password=psw,
                port=int(port), # Asegúrate de que el puerto sea un entero
                host=host,
                database=db,
                auth_plugin='mysql_native_password' # Para compatibilidad con MySQL 8+
            )
            self.cursor = self.conn.cursor(dictionary=True)
            # print("DEBUG: Conexión a la base de datos establecida en BaseDAO.") # Puedes descomentar para depurar
        except Error as e:
            # print(f"ERROR: Fallo al conectar a la base de datos en BaseDAO: {e}") # Puedes descomentar para depurar
            raise ConnectionError(f"No se pudo conectar a la base de datos: {e}") # Lanza un error más específico


    def execute_query(self, query, params=None, fetch_one=False):
        self.cursor.execute(query, params or ())
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchone() if fetch_one else self.cursor.fetchall()
        else:
            self.conn.commit()
            return self.cursor.lastrowid

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()

    @staticmethod
    def probar_conexion_con_config():
        """
        Intenta establecer una conexión a la base de datos usando la configuración global de DBConfig.
        Esta función es ideal para pruebas rápidas y doctests.

        El doctest verifica si la función devuelve True cuando la configuración es válida
        y la conexión se puede establecer.

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
            # Intentamos crear una instancia de BaseDAO, lo que intentará la conexión
            dao = BaseDAO()
            dao.close()
            return True
        except (Error, ValueError, ConnectionError): # Capturamos los errores esperados de conexión o configuración
            return False


class JardineriaRepository(BaseDAO):
    def get_all(self):
        query = "SELECT * FROM gama_producto"
        rows = self.execute_query(query)
        return [GamaProducto(row['gama'], row['descripcion_texto'], row['descripcion_html'], row['imagen']) for row in rows]

    def get_all_product_gama(self, gama):
        """Obtiene todos los productos de una gama específica."""
        query = "SELECT * FROM producto WHERE gama = %s"
        params = (gama,)
        rows = self.execute_query(query, params)
        productos = []
        for row in rows:
            producto = Producto(
                codigo_producto=row['codigo_producto'],
                nombre=row['nombre'],
                gama=row['gama'],
                dimensiones=row['dimensiones'],
                proveedor=row['proveedor'],
                descripcion=row['descripcion'],
                cantidad_en_stock=row['cantidad_en_stock'],
                precio_venta=row['precio_venta'],
                precio_proveedor=row['precio_proveedor']
            )
            productos.append(producto)
        return productos