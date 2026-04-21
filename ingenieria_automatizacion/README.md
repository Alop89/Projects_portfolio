# ⚙️ THE GRID: Data Engineering & Serverless Automation ⚡

> **By ArchData Consulting** 

## 💾 PROJECT OVERVIEW

La verdadera inteligencia de negocios no ocurre armando reportes manuales, ocurre de fondo mientras el negocio opera. Este proyecto representa la "plomería digital" de un ecosistema de datos moderno (*Lean Data Stack*).

El objetivo fue construir un *pipeline* automatizado (ETL) impulsado por eventos (*event-driven*), que monitorea directorios locales, procesa nuevos archivos y los inyecta directamente a una base de datos PostgreSQL Serverless en la nube, lista para alimentar tableros de Power BI.

### 🛠️ TECH STACK (THE ENGINE)

  * **Lenguaje Core:** Python 3.x 🐍
  * **Automatización de eventos:** `watchdog` (monitoreo de directorios 24/7)
  * **Data wrangling:** Pandas, SQLAlchemy
  * **Cloud database:** Neon Tech (PostgreSQL Serverless) ☁️
  * **Business intelligence:** Power BI

-----

## 🛤️ LA ARQUITECTURA DEL PIPELINE (Flujo de Datos)

El sistema fue diseñado para eliminar la intervención humana del proceso de actualización de reportes. El flujo sigue 4 fases críticas:

### 1️⃣ Ingesta automática (Zero-Click)

Utilizamos la librería `watchdog` de Python para crear un centinela digital en el servidor o equipo local.

  * **El detonante:** Cuando un usuario o el ERP guarda un nuevo archivo (ej. `ventas_semana_nueva.csv`) en la carpeta designada (`erp_inbox`), el script se despierta en milisegundos y captura la ruta del archivo de forma automática. ¡Cero clics manuales\!

### 2️⃣ Transformación y limpieza (data preprocessing)

Una vez detectado el archivo, el script de Python ejecuta el módulo de limpieza.

  * Estandarización de tipos de datos (fechas, monedas, strings).
  * Manejo de valores nulos y detección de duplicados.
  * Creación de nuevas columnas para segmentación de productos en automático.
  * Estructuración del *DataFrame* para que coincida exactamente con el esquema relacional de la base de datos destino.

### 3️⃣ Carga serverless en la nube (Neon Tech)

Aquí ocurre la magia de la infraestructura moderna. En lugar de depender de servidores locales costosos, utilizamos **Neon Tech**.

  * El script establece una conexión segura mediante SQLAlchemy y la cadena de conexión de Neon.
  * Los datos limpios se inyectan (*Upsert* / *Append*) a la base de datos PostgreSQL en la nube.
  * **Ventaja Neon:** Al ser *Serverless*, la base de datos escala su poder de cómputo automáticamente en el momento de la ingesta y se suspende cuando no hay tráfico, reduciendo los costos operativos drásticamente.

### 4️⃣ Despliegue en Business Intelligence

Con los datos estructurados en la nube, herramientas como **Power BI** simplemente se conectan a Neon mediante *DirectQuery* o importación programada. El tablero siempre refleja la última versión de la verdad comercial.

-----

## 🚀 IMPACTO Y LÓGICA DE NEGOCIO

Construir tuberías digitales bajo esta arquitectura transforma radicalmente la operación de una empresa:

1.  **Reducción de tiempo:** Pasamos de un proceso de cierre mensual de 3 días a una actualización continua en segundos.
2.  **Integridad de los datos:** Al eliminar la manipulación manual de archivos de Excel, se reduce el error humano a cero.
3.  **Infraestructura ágil:** Usar Neon Tech permite a las empresas tener el poder de bases de datos de nivel corporativo sin los costos de mantenimiento de servidores físicos.

-----

¡Qué onda, Alfredo! Aquí tienes la traducción impecable de tu "motor" de datos. Mantuve toda la jerga técnica en inglés (*event-driven*, *zero-click*, *upsert*) para que cualquier reclutador o cliente internacional vea de inmediato el nivel de ingeniería que manejas en ArchData. 

Listo para copiar y pegar directamente en tu repositorio:

---

# ⚙️ THE GRID: Data Engineering & Serverless Automation ⚡(ENG)

> **By ArchData Consulting** 


## 💾 PROJECT OVERVIEW

True business intelligence doesn't happen by manually putting together reports; it happens in the background while the business operates. This project represents the "digital plumbing" of a modern data ecosystem (*Lean Data Stack*).

The goal was to build an automated, event-driven ETL pipeline that monitors local directories, processes new files, and injects them directly into a cloud-based serverless PostgreSQL database, ready to feed Power BI dashboards.

### 🛠️ TECH STACK (THE ENGINE)

* **Core Language:** Python 3.x 🐍
* **Event Automation:** `watchdog` (24/7 directory monitoring)
* **Data Wrangling:** Pandas, SQLAlchemy
* **Cloud Database:** Neon Tech (Serverless PostgreSQL) ☁️
* **Business Intelligence:** Power BI

---

## 🛤️ PIPELINE ARCHITECTURE (Data Flow)

The system was designed to eliminate human intervention from the report updating process. The flow follows 4 critical phases:

### 1️⃣ Automatic Ingestion (Zero-Click)

We use the Python `watchdog` library to create a digital sentinel on the server or local machine.

* **The trigger:** When a user or the ERP saves a new file (e.g., `new_weekly_sales.csv`) in the designated folder (`erp_inbox`), the script wakes up in milliseconds and automatically captures the file path. Zero manual clicks!

### 2️⃣ Transformation and Cleaning (Data Preprocessing)

Once the file is detected, the Python script executes the cleaning module.

* Standardization of data types (dates, currencies, strings).
* Handling of null values and duplicate detection.
* Creation of new columns for automatic product segmentation.
* Structuring the *DataFrame* to match exactly with the target database's relational schema.

### 3️⃣ Serverless Cloud Loading (Neon Tech)

Here is where the magic of modern infrastructure happens. Instead of relying on expensive local servers, we use **Neon Tech**.

* The script establishes a secure connection using SQLAlchemy and the Neon connection string.
* Clean data is injected (*Upsert* / *Append*) into the cloud PostgreSQL database.
* **Neon Advantage:** Being *Serverless*, the database automatically scales its computing power at the moment of ingestion and suspends itself when there is no traffic, drastically reducing operational costs.

### 4️⃣ Business Intelligence Deployment

With structured data in the cloud, tools like **Power BI** simply connect to Neon via *DirectQuery* or scheduled import. The dashboard always reflects the latest version of commercial truth.

---

## 🚀 IMPACT AND BUSINESS LOGIC

Building digital pipelines under this architecture radically transforms a company's operation:

1. **Time reduction:** We went from a 3-day monthly closing process to continuous updating in seconds.
2. **Data integrity:** By eliminating the manual manipulation of Excel files, human error is reduced to zero.
3. **Agile infrastructure:** Using Neon Tech allows companies to have enterprise-level database power without the physical server maintenance costs.

---
*Developed by **[ArchData Consulting]***
-----
