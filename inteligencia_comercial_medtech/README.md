# 🌌 MEDTECH DATA GRID: Intelligence and market analysis 🏥⚡
> **By ArchData Consulting** 


![Banner Principal](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/medtech_banner.png)


## 💾 PROJECT OVERVIEW
Este proyecto representa el núcleo analítico de las ventas de dispositivos y consumibles médicos. Navegando a través de un ecosistema de datos bimodal, el objetivo fue extraer *insights* accionables para la cadena de suministro, estrategias de *pricing* y retención de clientes en el sector HealthTech. 

Pasamos de la generación de datos crudos a la inferencia estadística avanzada y modelado de series de tiempo.

### 🛠️ TECH STACK (THE MAINFRAME)
* **Core:** Python 3.x 🐍
* **Data Wrangling:** Pandas, NumPy
* **Estadística Inferencia:** SciPy, Statsmodels, Pingouin (ANOVA, Spearman, Games-Howell)
* **Visualización:** Seaborn, Matplotlib (Estética customizada)
* **Time Series:** Statsmodels (Seasonal Decomposition)

---

## 📊 CORE INSIGHTS AND BUSINESS LOGIC

### 1️⃣ Análisis de Varianza 
**Protocolo:** ANOVA de una vía y pruebas Post-Hoc de Games-Howell y Tukey.
* **El Reto:** ¿Compran los hospitales públicos de forma diferente a los privados o clínicas especializadas?
* **El Análisis:** Se detectó heterocedasticidad (varianzas desiguales) impulsada por el sector público. Al aplicar la prueba robusta de Games-Howell, se comprobó que **no existe una diferencia estadística significativa** ($p > 0.05$) en el ticket promedio por tipo de hospital.
* **El Insight:** El tipo de institución no determina el monto total de ventas; la estrategia comercial no debe segmentarse por hospital, sino por categoría de producto.

![Análisis de relación entre descuento y venta](inteligencia_comercial_medtech/reports/figures/descuento_vs_volumen_de_venta.png)
![Análisis de Varianza hospitalaria](inteligencia_comercial_medtech/reports/figures/consumibles_vs_bienes_de_capital.png)

### 2️⃣ Detección de Anomalías
**Protocolo:** Z-Score global vs. IQR segmentado.
* **El Reto:** Limpiar el ruido del *dataset* sin destruir información de alto valor.
* **El Análisis:** Aplicar un Z-Score global resultó en un falso positivo del 97% debido a la naturaleza multimodal del sector médico (consumibles de bajo costo vs. bienes de capital de alto costo). Pivotamos hacia un **Rango Intercuartílico (IQR) segmentado por categoría** para encontrar los casos reales que deben ser revisados para descartar errores o posibles fraudes.
* **El Insight:** Se aislaron con precisión 53 anomalías operativas críticas (errores de captura o posibles fraudes).

![Detección de Anomalías IQR](inteligencia_comercial_medtech/reports/figures/outliers_ventas_region.png)

### 3️⃣ Satisfacción del Cliente
**Protocolo:** Correlación de rangos de Spearman ($\rho$).
* **El Reto:** ¿Una mayor satisfacción permite cobrar un ticket más alto en Imagenología?
* **El Análisis:** La correlación de Spearman ($\rho = 0.07, p = 0.11$) demostró que la satisfacción no altera el valor unitario de los contratos (el precio está anclado al mercado). Sin embargo, el análisis de densidades reveló que las categorías de satisfacción "Alta" concentran casi todo el ingreso.
* **El Insight:** La satisfacción no es un *Price Driver*, es un **Volume Driver**. En HealthTech, el servicio post-venta garantiza la cuota de mercado (*Market Share*) y la frecuencia de compra.

![Porcentaje de satisfacción](inteligencia_comercial_medtech/reports/figures/piechart_.png)
![Densidad de compras por nivel de satisfacción](inteligencia_comercial_medtech/reports/figures/joint_plot.png)

### 4️⃣ Forecasting and Supply chain
**Protocolo:** Descomposición de series de tiempo (modelo aditivo) y proyección de stock.
* **El Reto:** Prevenir desabastos (*stockouts*) de material crítico.
* **El Análisis:** Se aplicaron promedios móviles (ventan de 3 meses) para filtrar el ruido diario y una descomposición aditiva para aislar la demanda orgánica de los ciclos.
* **El Insight:** Desarrollamos un motor de recomendaciones de abastecimiento que suma la tendencia, el efecto estacional del mes y un **Stock de Seguridad dinámico** ($2\sigma$ de los residuos del modelo). 


![Tendencia de ventas](inteligencia_comercial_medtech/reports/figures/tendencia_.png)
![Time series decomposition](inteligencia_comercial_medtech/reports/figures/descomp_demanda.png)
![Tabla de recomendaciones de abastecimiento](inteligencia_comercial_medtech/reports/figures/demanda_esperada.png)

---

## 🚀 SYSTEM OVERRIDE: NEXT STEPS
La fase de análisis estadístico está cerrada. El próximo salto en la red es la **Fase de Ingeniería de Datos (ETL)**, donde este conocimiento será inyectado en una base de datos PostgreSQL en la nube (Neon) para alimentar un Dashboard.



---
*Developed by **[ArchData Consulting]** 