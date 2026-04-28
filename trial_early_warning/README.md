# 🧬 Trial Early Warning System (TEWS) - MLOps Architecture

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2.1-EE4C2C.svg)](https://pytorch.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC.svg)](https://www.terraform.io/)

## 📌 Visión General del Proyecto
El **Trial Early Warning System** es una solución integral de Machine Learning diseñada para predecir el riesgo de Eventos Adversos Severos (SAE) en pacientes de ensayos clínicos. 

Este proyecto no es solo un modelo predictivo, sino un ecosistema MLOps completo. Abarca desde la ingeniería de datos y el análisis exploratorio, hasta el despliegue de una API RESTful contenedorizada, garantizando escalabilidad, explicabilidad médica y automatización en la nube.

## 🔬 Hallazgos Clínicos y Analíticos (Fase de Data Science)
Durante la fase de análisis exploratorio de datos (EDA) y entrenamiento del modelo, descubrimos *insights* críticos para la gestión del ensayo clínico:
* **Biomarcadores críticos:** El índice de masa corporal (BMI) base y los niveles de la enzima hepática ALT demostraron ser los predictores más fuertes de toxicidad.
* **Explicabilidad (SHAP):** Se implementó la librería SHAP para garantizar que cada predicción pueda ser interpretada por los médicos investigadores, evitando el efecto de "caja negra" y cumpliendo con regulaciones de salud.
* **Umbrales de decisión:** Optimizamos el modelo XGBoost no por *Accuracy*, sino por *Recall*, ajustando el umbral probabilístico a `0.0878` para priorizar la detección temprana de pacientes en riesgo sobre los falsos positivos.

## 🏗️ Arquitectura del sistema (ciclo MLOps)
El sistema está construido siguiendo los más altos estándares de ingeniería de software para IA:

1. **Motores analíticos multimodelo:** * **XGBoost:** Modelo principal optimizado para datos tabulares clínicos.
   * **PyTorch (Deep Learning):** Red Neuronal (MLP) secundaria integrada para capturar relaciones altamente no lineales y preparar la arquitectura para futura ingesta multimodal (ej. imágenes DICOM).
2. **Capa de servicio (FastAPI):** Endpoints asíncronos con validación estricta de esquemas de datos mediante Pydantic para proteger el modelo de inputs erróneos.
3. **Testing automatizado (Pytest):** Suite de pruebas que audita los endpoints y las lógicas de negocio antes de cualquier despliegue.
4. **Contenedorización (Docker):** Aislamiento de dependencias y sistema operativo para garantizar paridad entre entornos de desarrollo y producción.
5. **Infraestructura y CI/CD:** * **Terraform:** Infraestructura como Código (IaC) para aprovisionamiento automatizado de servidores EC2 en AWS.
   * **GitHub Actions:** Pipeline de despliegue continuo que ejecuta pruebas y construye la imagen de Docker automáticamente en cada *push*.

## 📂 Estructura del Repositorio
```text
trial_early_warning/
├── .github/workflows/        # Pipelines de CI/CD (GitHub Actions)
├── data/                     # Datos crudos y procesados
├── infrastructure/           # Scripts de Terraform (main.tf)
├── notebooks/                # Jupyter Notebooks (EDA, SHAP analysis)
├── src/
│   ├── models/               # Archivos de modelos (.pkl, .pt) y scripts de entrenamiento
│   └── webapp/               # Aplicación web y servidor FastAPI (api.py)
├── tests/                    # Framework de pruebas (test_api.py)
├── Dockerfile                # Receta de contenedorización
├── requirements.txt          # Dependencias congeladas
└── README.md                 # Documentación del proyecto
```

## 🚀 Guía de Ejecución

### Opción 1: Ejecución Local (Desarrollo)
1. Clona el repositorio e instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Levanta el servidor de la API:
   ```bash
   cd src/webapp
   uvicorn api:app --reload
   ```
3. Visita `http://127.0.0.1:8000/docs` para interactuar con Swagger UI.

### Opción 2: Ejecución con Docker (Producción)
1. Construye la imagen hermética:
   ```bash
   docker build -t clinical-oracle:v1 .
   ```
2. Ejecuta el contenedor:
   ```bash
   docker run -p 8000:8000 clinical-oracle:v1
   ```
3. La API estará disponible en `http://localhost:8000/docs`.

## 🧪 Ejecución de Pruebas (Auditoría)
Para correr la suite de pruebas unitarias y asegurar la integridad del sistema:
```bash
pytest tests/ -p no:cacheprovider
```

---

***

# 🧬 Trial Early Warning System (TEWS) - MLOps Architecture (ENG)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2.1-EE4C2C.svg)](https://pytorch.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC.svg)](https://www.terraform.io/)

## 📌 Project Overview
The **Trial Early Warning System** is an end-to-end Machine Learning solution designed to predict the risk of Severe Adverse Events (SAEs) in clinical trial patients. 

This project is not just a predictive model, but a complete MLOps ecosystem. It spans from data engineering and exploratory analysis to the deployment of a containerized RESTful API, ensuring scalability, medical explainability, and cloud automation.

## 🔬 Clinical & Analytical Findings (Data Science Phase)
During the Exploratory Data Analysis (EDA) and model training phases, we discovered critical insights for clinical trial management:
* **Critical Biomarkers:** Baseline Body Mass Index (BMI) and ALT liver enzyme levels proved to be the strongest predictors of toxicity.
* **Explainability (SHAP):** The SHAP library was implemented to ensure that every prediction can be interpreted by medical researchers, avoiding the "black box" effect and complying with healthcare regulations.
* **Decision Thresholds:** The XGBoost model was optimized not for Accuracy, but for *Recall*. We adjusted the probability threshold to `0.0878` to prioritize the early detection of at-risk patients over false positives.

## 🏗️ System Architecture (MLOps Lifecycle)
The system is built following the highest software engineering standards for AI:

1. **Multimodal Analytical Engines:** * **XGBoost:** Primary model optimized for clinical tabular data.
   * **PyTorch (Deep Learning):** Secondary Multi-Layer Perceptron (MLP) integrated to capture highly non-linear relationships and prepare the architecture for future multimodal ingestion (e.g., DICOM images).
2. **Serving Layer (FastAPI):** Asynchronous endpoints with strict data schema validation via Pydantic to protect the model from erroneous inputs.
3. **Automated Testing (Pytest):** A comprehensive test suite that audits endpoints and business logic before any deployment.
4. **Containerization (Docker):** Isolation of dependencies and operating system to guarantee parity between development and production environments.
5. **Infrastructure & CI/CD:** * **Terraform:** Infrastructure as Code (IaC) for the automated provisioning of EC2 servers on AWS.
   * **GitHub Actions:** Continuous Deployment pipeline that runs tests and builds the Docker image automatically on every *push*.

## 📂 Repository Structure
```text
trial_early_warning/
├── .github/workflows/        # CI/CD Pipelines (GitHub Actions)
├── data/                     # Raw and processed datasets
├── infrastructure/           # Terraform scripts (main.tf)
├── notebooks/                # Jupyter Notebooks (EDA, SHAP analysis)
├── src/
│   ├── models/               # Model artifacts (.pkl, .pt) and training scripts
│   └── webapp/               # Web application and FastAPI server (api.py)
├── tests/                    # Testing framework (test_api.py)
├── Dockerfile                # Containerization recipe
├── requirements.txt          # Frozen dependencies
└── README.md                 # Project documentation
```

## 🚀 Execution Guide

### Option 1: Local Execution (Development)
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the API server:
   ```bash
   cd src/webapp
   uvicorn api:app --reload
   ```
3. Visit `http://127.0.0.1:8000/docs` to interact with the Swagger UI.

### Option 2: Docker Execution (Production)
1. Build the hermetic image:
   ```bash
   docker build -t clinical-oracle:v1 .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 clinical-oracle:v1
   ```
3. The API will be available at `http://localhost:8000/docs`.

## 🧪 Running Tests (Auditing)
To run the unit test suite and ensure system integrity:
```bash
pytest tests/ -p no:cacheprovider
```

---
*Developed with scientific rigor and MLOps methodologies to impact the future of clinical analysis.*
