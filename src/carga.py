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

def cargar_a_bd(df, db_path="data/processed/clientes.db", table_name="clientes_validados"):
    logging.info("Guardando los datos finales en SQLite...")
    
    try:
        # Primero me aseguro de que la carpeta exista antes de crear el archivo .db
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Conexión a SQLite (crea el archivo automáticamente si no existe)
        conexion = sqlite3.connect(db_path)
        
        # Uso 'replace' para que si corro el código 10 veces probando, no se dupliquen las tablas
        df.to_sql(table_name, conexion, if_exists='replace', index=False)
        
        logging.info(f"Se guardaron {len(df)} registros limpios en la base de datos.")
        
    except Exception as e:
        logging.error(f"Fallo crítico al guardar en la BD: {e}")
        raise e
        
    finally:
        # Siempre cierro la conexión por buenas prácticas
        if 'conexion' in locals():
            conexion.close()