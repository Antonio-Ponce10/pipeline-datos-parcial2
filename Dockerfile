# 1. Definir el "Sistema Operativo" base
FROM python:3.11-slim

# 2. Crear una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar la lista de librerías desde tu PC al contenedor
COPY requirements.txt .

# 4. Instalar las librerías dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código de tu proyecto al contenedor
COPY . .

# 6. El comando que se ejecutará al encender el contenedor
CMD ["python", "main.py"]