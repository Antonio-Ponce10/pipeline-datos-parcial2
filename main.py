import logging
from src.ingesta import ejecutar_ingesta
from src.limpieza import limpiar_y_transformar
from src.validacion import validar_datos
from src.carga import cargar_a_bd

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    ruta_archivo = "data/raw/clientes_sucio.csv"
    
    try:
        print("\n=======================================")
        print("🚀 INICIANDO DATA PIPELINE AUTOMATIZADO")
        print("=======================================\n")
        
        # 1. Ingesta
        print("➤ [Fase 1]: Extrayendo datos crudos...")
        df_crudo = ejecutar_ingesta(ruta_archivo)
        
        # 2. Limpieza
        print("➤ [Fase 2]: Limpiando y estandarizando...")
        df_limpio = limpiar_y_transformar(df_crudo)
        
        # 3. Validación
        print("➤ [Fase 3]: Aplicando reglas de negocio (Pydantic)...")
        df_validado = validar_datos(df_limpio)
        
        # 4. Carga a Base de Datos
        print("➤ [Fase 4]: Cargando datos a la Base de Datos Relacional...")
        cargar_a_bd(df_validado)
        
        print("\n=======================================")
        print("✅ PIPELINE EJECUTADO CON ÉXITO")
        print("=======================================")
        print("Tus datos validados ahora viven en: data/processed/clientes.db\n")
        
    except Exception as e:
        logging.critical(f"El pipeline falló: {e}")
        print("\n❌ ERROR CRÍTICO EN EL PIPELINE. Revisa logs/pipeline.log")