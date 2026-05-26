# 🚀 Pipeline de Datos Automatizado - Evaluación Parcial 2

**Asignatura:** ITY1101 - Gestión de Datos para IA  
**Autor:** Antonio Ponce  

---

## 📌 Descripción del Proyecto
Este proyecto implementa una arquitectura **DataOps** mediante un pipeline secuencial y modular que extrae, limpia, valida y carga datos (ETL). El objetivo principal es preparar un conjunto de datos crudos, corrigiendo anomalías y asegurando reglas de negocio, para que puedan ser consumidos de forma confiable por un modelo de Inteligencia Artificial.

---

## 🏗️ Estructura del Proyecto
El desarrollo sigue el principio de modularidad para garantizar la mantenibilidad y separación de responsabilidades:

```text
📁 pipeline-datos-parcial2/
├── 📂 data/
│   ├── 📂 raw/           # Datos fuente originales (CSV con errores)
│   └── 📂 processed/     # Datos listos para IA (Base de datos SQLite)
├── 📂 logs/              # Archivos de auditoría y trazabilidad (pipeline.log)
├── 📂 src/               # Código fuente modularizado
│   ├── ingesta.py        # Fase 1: Extracción
│   ├── limpieza.py       # Fase 2: Transformación y corrección
│   ├── validacion.py     # Fase 3: Reglas semánticas
│   └── carga.py          # Fase 4: Persistencia
├── .gitignore            # Exclusión de entornos virtuales y caché
└── main.py               # Orquestador principal del pipeline