import pandas as pd
import logging
from pydantic import BaseModel, ValidationError, Field

# Configuración de logs
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [VALIDACION] - %(message)s'
)

# Definimos el "Esquema" estricto. Esto dicta cómo DEBE ser un cliente válido
class ClienteSchema(BaseModel):
    id_cliente: int
    nombre: str = Field(min_length=2) # El nombre debe tener al menos 2 letras
    email: str
    edad: int = Field(ge=18, le=100)  # Regla de negocio: Clientes entre 18 y 100 años
    meses_contrato: int = Field(ge=0) # No pueden haber meses negativos
    total_pago: float = Field(ge=0.0) # El pago no puede ser negativo

def validar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra el dataframe dejando solo los registros que cumplen con las reglas de negocio.
    """
    logging.info("Iniciando Validación Estructural y Semántica...")
    registros = df.to_dict(orient='records')
    registros_validos = []
    
    for idx, fila in enumerate(registros):
        try:
            ClienteSchema(**fila)
            registros_validos.append(fila)
        except ValidationError as e:
            motivo = e.errors()[0]['msg']
            columna = e.errors()[0]['loc'][0]
            logging.warning(f"Anomalía en ID {fila.get('id_cliente')}: La columna '{columna}' {motivo}. Registro descartado.")
            
    df_validado = pd.DataFrame(registros_validos)
    return df_validado