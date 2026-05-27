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
    edad: int = Field(ge=18, le=100)  # La regla dice de 18 a 100 años (adios clienta de 150)
    meses_contrato: int = Field(ge=0) # Los contratos no pueden ser negativos
    total_pago: float = Field(ge=0.0) # El pago no puede ser negativo

def validar_datos(df):
    logging.info("Pasando los datos por el filtro de Pydantic...")
    registros = df.to_dict(orient='records')
    registros_validos = []
    
    for fila in registros:
        try:
            # Intento pasar la fila por el esquema
            ClienteSchema(**fila)
            registros_validos.append(fila)
        except ValidationError as e:
            # Si falla, saco el motivo y lo anoto, pero dejo que el código siga
            motivo = e.errors()[0]['msg']
            columna = e.errors()[0]['loc'][0]
            logging.warning(f"Se descartó el ID {fila.get('id_cliente')}: la columna '{columna}' {motivo}.")
            
    df_validado = pd.DataFrame(registros_validos)
    return df_validado