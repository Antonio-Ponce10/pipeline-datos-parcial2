import pandas as pd
import sqlite3
import logging
import os

# Configuración de logs
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [CARGA] - %(message)s'
)

def cargar_a_bd(df: pd.DataFrame, db_path: str = "data/processed/clientes.db", table_name: str = "clientes_validados"):
    """
    Carga el dataframe validado en una base de datos relacional SQLite.
    Garantiza la persistencia de los datos para su uso en modelos de IA.
    """
    logging.info(f"Iniciando carga de datos en la base de datos: {db_path}...")
    
    try:
        # 1. Asegurarnos de que la carpeta de destino exista
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # 2. Crear conexión a la base de datos (si no existe, SQLite la crea automáticamente)
        conexion = sqlite3.connect(db_path)
        
        # 3. Insertar los datos. 'if_exists="replace"' asegura que si corremos el pipeline 
        # varias veces, la tabla se actualice limpiamente sin duplicar todo.
        df.to_sql(table_name, conexion, if_exists='replace', index=False)
        
        logging.info(f"Carga exitosa. Se insertaron {len(df)} registros en la tabla '{table_name}'.")
        
    except Exception as e:
        logging.error(f"Error crítico al cargar los datos a la BD: {str(e)}")
        raise e
        
    finally:
        # 4. Buenas prácticas: Siempre cerrar la conexión a la base de datos
        if 'conexion' in locals():
            conexion.close()
            logging.info("Conexión a la base de datos cerrada de forma segura.")