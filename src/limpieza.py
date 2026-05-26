import pandas as pd
import logging

# Configuración de logs para este módulo
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [LIMPIEZA] - %(message)s'
)

def limpiar_y_transformar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica reglas de limpieza para estandarizar el dataset y manejar valores nulos o atípicos.
    """
    logging.info("Iniciando la fase de Limpieza y Transformación...")
    
    # Trabajamos sobre una copia para no alterar el dataframe original en memoria
    df_limpio = df.copy()

    try:
        # 1. Eliminar duplicados exactos (Como el ID 1001 que pusimos dos veces)
        filas_antes = len(df_limpio)
        df_limpio = df_limpio.drop_duplicates()
        logging.info(f"Se eliminaron {filas_antes - len(df_limpio)} registros duplicados.")

        # 2. Estandarizar texto: Quitar espacios accidentales en los nombres (Ej: " Luis Rojas ")
        if 'nombre' in df_limpio.columns:
            df_limpio['nombre'] = df_limpio['nombre'].str.strip()
            logging.info("Se estandarizó la columna 'nombre' (eliminación de espacios).")
        
        # 3. Tratamiento de valores nulos: Rellenar correos vacíos
        if 'email' in df_limpio.columns:
            nulos_email = df_limpio['email'].isna().sum()
            df_limpio['email'] = df_limpio['email'].fillna('no_registra@mail.com')
            logging.info(f"Se imputaron {nulos_email} valores nulos en la columna 'email'.")
        
        # 4. Limpieza matemática básica: Convertir edades negativas a positivas (Ej: -5 a 5)
        if 'edad' in df_limpio.columns:
            df_limpio['edad'] = df_limpio['edad'].abs()
            logging.info("Se transformaron las edades negativas a valores absolutos.")
        
        logging.info(f"Limpieza finalizada con éxito. Registros resultantes: {len(df_limpio)}")
        return df_limpio

    except Exception as e:
        logging.error(f"Error inesperado durante la limpieza de datos: {str(e)}")
        raise e