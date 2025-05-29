import os
import pyreportjasper
import shutil
import sys
import site


def compile_jasper_report(jrxml_path: str):
    print(f"DEBUG: Entrando a compile_jasper_report para {jrxml_path}")
    if not os.path.exists(jrxml_path):
        error_msg = f"Archivo JRXML no encontrado para compilar: {jrxml_path}"
        print(f"ERROR: {error_msg}")
        return False, error_msg

    jasper_path = jrxml_path.replace('.jrxml', '.jasper')
    jasper = pyreportjasper.PyReportJasper()
    try:
        print(f"DEBUG: Intentando compilar JRXML: {jrxml_path} a {jasper_path}")
        jasper.compile(jrxml_path)
        print(f"DEBUG: Compilación JRXML exitosa. Compilado a: {jasper_path}")
        return True, jasper_path
    except Exception as e:
        error_msg = f"Fallo al compilar JRXML '{jrxml_path}': {e}"
        print(f"ERROR: {error_msg}")
        return False, error_msg


def advanced_example_using_database(ficheroEntrada, ficheroSalida, con, parametros):
    print(f"DEBUG: Entrando a advanced_example_using_database para {ficheroEntrada}")
    input_file = ficheroEntrada
    output_file = ficheroSalida

    jasper = pyreportjasper.PyReportJasper()

    try:
        print(f"DEBUG: Generando informe: {input_file}")
        print(f"DEBUG: Salida en: {output_file}.pdf")
        print(f"DEBUG: Conexión BD: {con}")
        print(f"DEBUG: Parámetros informe: {parametros}")

        jasper.process(
            input_file,
            output_file,
            format_list=["pdf"],
            parameters=parametros,
            db_connection=con,
            locale='es_ES'
        )
        print(f"DEBUG: Informe generado con éxito en {output_file}.pdf")
        return True, f"Informe generado con éxito en: {output_file}.pdf"

    except Exception as e:
        error_message = f"Error al generar informe: {e}"
        print(f"ERROR: {error_message}")
        return False, error_message