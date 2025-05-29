class DBConfig:
    _is_connected = False
    _config = {}  # Diccionario privado para la configuración

    @classmethod
    def set_config(cls, config):
        """Guarda la configuración de la base de datos."""
        cls._config = config

    @classmethod
    def get_config(cls):
        """Devuelve la configuración de la base de datos."""
        return cls._config

    @classmethod
    def set_connected_status(cls, status: bool):
        """Establece el estado de conexión."""
        cls._is_connected = status
        print(f"DEBUG: Estado de conexión de BD: {status}")

    @classmethod
    def is_connected(cls) -> bool:
        """Devuelve True si la última conexión fue exitosa, False en caso contrario."""
        return cls._is_connected