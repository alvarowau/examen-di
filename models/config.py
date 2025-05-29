class DBConfig:
    """
    Gestiona la configuración y el estado de conexión de la base de datos de manera global.

    Esta clase estática permite almacenar y recuperar la configuración de la base de datos,
    así como el estado de la conexión (conectado/desconectado) para ser utilizado
    en diferentes partes de la aplicación sin pasar la configuración explícitamente.

    Attributes:
        _is_connected (bool): Un indicador privado que es True si la última conexión
                               a la base de datos fue exitosa, False en caso contrario.
        _config (dict): Un diccionario privado que almacena los parámetros de configuración
                        de la base de datos, como el host, usuario, contraseña, etc.
    """

    _is_connected = False
    _config = {}

    @classmethod
    def set_config(cls, config: dict):
        """
        Guarda la configuración de la base de datos.

        Args:
            config (dict): Un diccionario que contiene los parámetros de configuración de la base de datos.
                           Por ejemplo: `{'host': 'localhost', 'user': 'root', 'password': 'my_password'}`.
        """
        cls._config = config

    @classmethod
    def get_config(cls) -> dict:
        """
        Devuelve la configuración de la base de datos actualmente almacenada.

        Returns:
            dict: Un diccionario con los parámetros de configuración de la base de datos.
        """
        return cls._config

    @classmethod
    def set_connected_status(cls, status: bool):
        """
        Establece el estado de conexión de la base de datos.

        Este método debe ser llamado después de intentar una conexión a la base de datos
        para reflejar si la conexión fue exitosa o no.

        Args:
            status (bool): True si la conexión fue exitosa, False si falló.
        """
        cls._is_connected = status

    @classmethod
    def is_connected(cls) -> bool:
        """
        Verifica si la base de datos está actualmente conectada.

        Returns:
            bool: True si la última conexión a la base de datos fue exitosa, False en caso contrario.
        """
        return cls._is_connected
