import logging
from src.ingesta import ejecutar_ingesta
from src.limpieza import limpiar_y_transformar
from src.validacion import validar_datos
from src.carga import cargar_a_bd

# Configuro el log para que guarde todo en el archivo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    ruta_archivo = "data/raw/clientes_sucio.csv"
    
    try:
        print("\n--- Arrancando el Pipeline de Datos ---")

        
        # 1. Ingesta
        print("Paso 1: Leyendo el CSV...")
        df_crudo = ejecutar_ingesta(ruta_archivo)
        
        # 2. Limpieza
        print("Paso 2: Limpiando formatos y nulos...")
        df_limpio = limpiar_y_transformar(df_crudo)
        
        # 3. Validación
        print("Paso 3: Pasando el filtro de Pydantic...")
        df_validado = validar_datos(df_limpio)
        
        # 4. Carga a Base de Datos
        print("Paso 4: Guardando en SQLite...")
        cargar_a_bd(df_validado)
        

        print("\n¡Todo listo! Los datos están en clientes.db")

    except Exception as e:
        logging.critical(f"El pipeline falló: {e}")
        print("\n❌ ERROR CRÍTICO EN EL PIPELINE. Revisa logs/pipeline.log")