import os

import pyreportjasper


def compile_jasper_report(jrxml_path: str) -> tuple[bool, str]:
    """Compila un archivo JRXML a formato Jasper.

    Args:
        jrxml_path (str): Ruta al archivo .jrxml a compilar.

    Returns:
        tuple[bool, str]: (éxito, mensaje) donde:
            - éxito: True si la compilación fue exitosa
            - mensaje: Ruta del archivo .jasper o mensaje de error
    """
    if not os.path.exists(jrxml_path):
        error_msg = f"Archivo JRXML no encontrado para compilar: {jrxml_path}"
        return False, error_msg

    jasper_path = jrxml_path.replace(".jrxml", ".jasper")
    jasper = pyreportjasper.PyReportJasper()

    try:
        jasper.compile(jrxml_path)
        return True, jasper_path
    except Exception as e:
        error_msg = f"Fallo al compilar JRXML '{jrxml_path}': {e}"
        return False, error_msg


def advanced_example_using_database(
    ficheroEntrada: str, ficheroSalida: str, con: any, parametros: dict
) -> tuple[bool, str]:
    """Genera un informe JasperReports usando conexión a base de datos.

    Args:
        ficheroEntrada (str): Ruta al archivo .jasper
        ficheroSalida (str): Ruta de salida para el informe (sin extensión)
        con (any): Conexión a la base de datos
        parametros (dict): Parámetros para el informe

    Returns:
        tuple[bool, str]: (éxito, mensaje) donde:
            - éxito: True si la generación fue exitosa
            - mensaje: Ruta del informe generado o mensaje de error
    """
    input_file = ficheroEntrada
    output_file = ficheroSalida
    jasper = pyreportjasper.PyReportJasper()

    try:
        jasper.process(
            input_file,
            output_file,
            format_list=["pdf"],
            parameters=parametros,
            db_connection=con,
            locale="es_ES",
        )
        return True, f"Informe generado con éxito en: {output_file}.pdf"
    except Exception as e:
        error_message = f"Error al generar informe: {e}"
        return False, error_message
