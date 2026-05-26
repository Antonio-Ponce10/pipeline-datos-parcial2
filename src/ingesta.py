import os
import pandas as pd
import logging

# Configuración local de logs para este módulo
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [INGESTA] - %(message)s'
)

def ejecutar_ingesta(ruta_origen: str) -> pd.DataFrame:
    """
    Lee el archivo CSV de la fuente original de manera controlada.
    Aplica principios DataOps de trazabilidad y manejo de excepciones.
    """
    logging.info(f"Iniciando el proceso de ingesta desde: {ruta_origen}")
    
    # Control de Excepción 1: Verificar si el archivo realmente existe
    if not os.path.exists(ruta_origen):
        error_msg = f"Error crítico: El archivo en '{ruta_origen}' no existe."
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)
        
    try:
        # Intentamos realizar la lectura automatizada
        df = pd.read_csv(ruta_origen)
        
        # Log de éxito informando las dimensiones encontradas
        logging.info(f"Ingesta completada con éxito. Se cargaron {df.shape[0]} filas y {df.shape[1]} columnas.")
        return df
        
    except pd.errors.EmptyDataError:
        logging.error("El archivo fuente está completamente vacío.")
        raise ValueError("El archivo CSV está vacío.")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado durante la lectura: {str(e)}")
        raise e