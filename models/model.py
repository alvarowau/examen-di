class Oficina:
    """Representa una oficina de la empresa con su ubicación y datos de contacto.

    Attributes:
        codigo_oficina (str): Identificador único de la oficina.
        ciudad (str): Ciudad donde se encuentra la oficina.
        pais (str): País donde se encuentra la oficina.
        region (str, optional): Región o estado donde se encuentra la oficina.
        codigo_postal (str): Código postal de la ubicación.
        telefono (str): Número de teléfono de contacto.
        linea_direccion1 (str): Dirección principal.
        linea_direccion2 (str, optional): Segunda línea de dirección si es necesaria.
    """

    def __init__(self, codigo_oficina, ciudad, pais, codigo_postal, telefono, linea_direccion1, linea_direccion2=None, region=None):
        self.codigo_oficina = codigo_oficina
        self.ciudad = ciudad
        self.pais = pais
        self.region = region
        self.codigo_postal = codigo_postal
        self.telefono = telefono
        self.linea_direccion1 = linea_direccion1
        self.linea_direccion2 = linea_direccion2

    def __str__(self):
        return f"Oficina(codigo='{self.codigo_oficina}', ciudad='{self.ciudad}', pais='{self.pais}')"


class Empleado:
    """Representa un empleado de la empresa con sus datos personales y laborales.

    Attributes:
        codigo_empleado (int): Identificador único del empleado.
        nombre (str): Primer nombre del empleado.
        apellido1 (str): Primer apellido del empleado.
        apellido2 (str, optional): Segundo apellido del empleado.
        extension (str): Extensión telefónica del empleado.
        email (str): Correo electrónico del empleado.
        codigo_oficina (str): Oficina donde trabaja el empleado.
        codigo_jefe (int, optional): Código del supervisor directo.
        puesto (str, optional): Cargo o posición del empleado.
    """

    def __init__(self, codigo_empleado, nombre, apellido1, extension, email, codigo_oficina, codigo_jefe=None, puesto=None, apellido2=None):
        self.codigo_empleado = codigo_empleado
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.extension = extension
        self.email = email
        self.codigo_oficina = codigo_oficina
        self.codigo_jefe = codigo_jefe
        self.puesto = puesto

    def __str__(self):
        return f"Empleado(codigo={self.codigo_empleado}, nombre='{self.nombre} {self.apellido1}', oficina='{self.codigo_oficina}')"


class GamaProducto:
    """Representa una categoría o gama de productos ofrecidos por la empresa.

    Attributes:
        gama (str): Nombre de la gama de productos.
        descripcion_texto (str, optional): Descripción en texto plano.
        descripcion_html (str, optional): Descripción en formato HTML.
        imagen (str, optional): Ruta o referencia a imagen representativa.
    """

    def __init__(self, gama, descripcion_texto=None, descripcion_html=None, imagen=None):
        self.gama = gama
        self.descripcion_texto = descripcion_texto
        self.descripcion_html = descripcion_html
        self.imagen = imagen

    def __str__(self):
        return f"GamaProducto(gama='{self.gama}')"


class Cliente:
    """Representa un cliente de la empresa con sus datos de contacto y comerciales.

    Attributes:
        codigo_cliente (int): Identificador único del cliente.
        nombre_cliente (str): Nombre completo del cliente.
        nombre_contacto (str, optional): Nombre de la persona de contacto.
        apellido_contacto (str, optional): Apellido de la persona de contacto.
        telefono (str): Número de teléfono principal.
        fax (str): Número de fax.
        linea_direccion1 (str): Dirección principal.
        linea_direccion2 (str, optional): Segunda línea de dirección.
        ciudad (str): Ciudad del cliente.
        region (str, optional): Región o estado del cliente.
        pais (str, optional): País del cliente.
        codigo_postal (str, optional): Código postal.
        codigo_empleado_rep_ventas (int, optional): Empleado asignado como representante.
        limite_credito (float, optional): Límite de crédito asignado al cliente.
    """

    def __init__(self, codigo_cliente, nombre_cliente, telefono, fax, linea_direccion1, ciudad, nombre_contacto=None, apellido_contacto=None, linea_direccion2=None, region=None, pais=None, codigo_postal=None, codigo_empleado_rep_ventas=None, limite_credito=None):
        self.codigo_cliente = codigo_cliente
        self.nombre_cliente = nombre_cliente
        self.nombre_contacto = nombre_contacto
        self.apellido_contacto = apellido_contacto
        self.telefono = telefono
        self.fax = fax
        self.linea_direccion1 = linea_direccion1
        self.linea_direccion2 = linea_direccion2
        self.ciudad = ciudad
        self.region = region
        self.pais = pais
        self.codigo_postal = codigo_postal
        self.codigo_empleado_rep_ventas = codigo_empleado_rep_ventas
        self.limite_credito = limite_credito

    def __str__(self):
        return f"Cliente(codigo={self.codigo_cliente}, nombre='{self.nombre_cliente}', ciudad='{self.ciudad}')"


class Pedido:
    """Representa un pedido realizado por un cliente.

    Attributes:
        codigo_pedido (int): Identificador único del pedido.
        fecha_pedido (date): Fecha en que se realizó el pedido.
        fecha_esperada (date): Fecha esperada de entrega.
        fecha_entrega (date, optional): Fecha real de entrega.
        estado (str): Estado actual del pedido.
        comentarios (str, optional): Comentarios adicionales.
        codigo_cliente (int): Cliente que realizó el pedido.
    """

    def __init__(self, codigo_pedido, fecha_pedido, fecha_esperada, codigo_cliente, estado, fecha_entrega=None, comentarios=None):
        self.codigo_pedido = codigo_pedido
        self.fecha_pedido = fecha_pedido
        self.fecha_esperada = fecha_esperada
        self.fecha_entrega = fecha_entrega
        self.estado = estado
        self.comentarios = comentarios
        self.codigo_cliente = codigo_cliente

    def __str__(self):
        return f"Pedido(codigo={self.codigo_pedido}, fecha='{self.fecha_pedido}', cliente={self.codigo_cliente}, estado='{self.estado}')"


class Producto:
    """Representa un producto ofrecido por la empresa.

    Attributes:
        codigo_producto (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        gama (str): Gama a la que pertenece el producto.
        dimensiones (str, optional): Dimensiones físicas del producto.
        proveedor (str, optional): Proveedor del producto.
        descripcion (str, optional): Descripción detallada.
        cantidad_en_stock (int): Cantidad disponible en inventario.
        precio_venta (float): Precio de venta al público.
        precio_proveedor (float, optional): Precio de compra al proveedor.
    """

    def __init__(self, codigo_producto, nombre, gama, cantidad_en_stock, precio_venta, precio_proveedor=None, dimensiones=None, proveedor=None, descripcion=None):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.gama = gama
        self.dimensiones = dimensiones
        self.proveedor = proveedor
        self.descripcion = descripcion
        self.cantidad_en_stock = cantidad_en_stock
        self.precio_venta = precio_venta
        self.precio_proveedor = precio_proveedor

    def __str__(self):
        return f"Producto(codigo='{self.codigo_producto}', nombre='{self.nombre}', gama='{self.gama}', precio={self.precio_venta})"


class DetallePedido:
    """Representa un ítem específico dentro de un pedido.

    Attributes:
        codigo_pedido (int): Pedido al que pertenece este detalle.
        codigo_producto (str): Producto solicitado.
        cantidad (int): Cantidad solicitada.
        precio_unidad (float): Precio unitario al momento del pedido.
        numero_linea (int): Número de línea dentro del pedido.
    """

    def __init__(self, codigo_pedido, codigo_producto, cantidad, precio_unidad, numero_linea):
        self.codigo_pedido = codigo_pedido
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_unidad = precio_unidad
        self.numero_linea = numero_linea

    def __str__(self):
        return f"DetallePedido(pedido={self.codigo_pedido}, producto='{self.codigo_producto}', cantidad={self.cantidad}, precio_unidad={self.precio_unidad})"


class Pago:
    """Representa un pago realizado por un cliente.

    Attributes:
        codigo_cliente (int): Cliente que realizó el pago.
        forma_pago (str): Método de pago utilizado.
        id_transaccion (str): Identificador de la transacción.
        fecha_pago (date): Fecha en que se realizó el pago.
        total (float): Monto total del pago.
    """

    def __init__(self, codigo_cliente, forma_pago, id_transaccion, fecha_pago, total):
        self.codigo_cliente = codigo_cliente
        self.forma_pago = forma_pago
        self.id_transaccion = id_transaccion
        self.fecha_pago = fecha_pago
        self.total = total

    def __str__(self):
        return f"Pago(cliente={self.codigo_cliente}, forma_pago='{self.forma_pago}', total={self.total})"