# 🌌 MEDTECH DATA GRID: Intelligence and market analysis 🏥⚡
> **By ArchData Consulting** 


![Banner Principal](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/medtech_banner.png)


## 💾 PROJECT OVERVIEW
Este proyecto representa el núcleo analítico de las ventas de dispositivos y consumibles médicos. Navegando a través de un ecosistema de datos bimodal, el objetivo fue extraer *insights* accionables para la cadena de suministro, estrategias de *pricing* y retención de clientes en el sector HealthTech. 

Pasamos de la generación de datos crudos a la inferencia estadística avanzada y modelado de series de tiempo.

### 🛠️ TECH STACK (THE MAINFRAME)
* **Core:** Python 3.x 🐍
* **Data wrangling:** Pandas, NumPy
* **Estadística :** SciPy, Statsmodels, Pingouin (ANOVA, Spearman, Games-Howell, Tukey)
* **Visualización:** Seaborn, Matplotlib (Estética customizada), Plotly.
* **Time series:** Statsmodels (Seasonal Decomposition)

---

## 📊 CORE INSIGHTS AND BUSINESS LOGIC

### 1️⃣ Análisis de varianza 
**Protocolo:** ANOVA de una vía y pruebas Post-Hoc de Games-Howell y Tukey.
* **El reto:** ¿Compran los hospitales públicos de forma diferente a los privados o clínicas especializadas?
* **El análisis:** Se detectó heterocedasticidad (varianzas desiguales) impulsada por el sector público. Al aplicar la prueba robusta de Games-Howell, se comprobó que **no existe una diferencia estadística significativa** ($p > 0.05$) en el ticket promedio por tipo de hospital.
* **El insight:** El tipo de institución no determina el monto total de ventas; la estrategia comercial no debe segmentarse por hospital, sino por categoría de producto.

![Análisis de relación entre descuento y venta](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/descuento_vs_volumen_de_venta.png)
![Análisis de varianza hospitalaria](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/consumibles_vs_bienes_de_capital.png)

### 2️⃣ Detección de Anomalías
**Protocolo:** Z-Score global vs. IQR segmentado.
* **El reto:** Limpiar el ruido del *dataset* sin destruir información de alto valor.
* **El análisis:** Aplicar un Z-Score global resultó en un falso positivo del 97% debido a la naturaleza multimodal del sector médico (consumibles de bajo costo vs. bienes de capital de alto costo). Pivotamos hacia un **Rango Intercuartílico (IQR) segmentado por categoría** para encontrar los casos reales que deben ser revisados para descartar errores o posibles fraudes.
* **El insight:** Se aislaron con precisión 53 anomalías operativas críticas (errores de captura o posibles fraudes).

![Detección de Anomalías IQR](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/outliers_ventas_region.png)

### 3️⃣ Satisfacción del Cliente
**Protocolo:** Correlación de rangos de Spearman ($\rho$).
* **El reto:** ¿Una mayor satisfacción permite cobrar un ticket más alto en Imagenología?
* **El análisis:** La correlación de Spearman ($\rho = 0.07, p = 0.11$) demostró que la satisfacción no altera el valor unitario de los contratos (el precio está anclado al mercado). Sin embargo, el análisis de densidades reveló que las categorías de satisfacción "Alta" concentran casi todo el ingreso.
* **El insight:** La satisfacción no es un *Price Driver*, es un **Volume Driver**. En HealthTech, el servicio post-venta garantiza la cuota de mercado (*Market Share*) y la frecuencia de compra.

![Porcentaje de satisfacción](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/piechart_.png)
![Densidad de compras por nivel de satisfacción](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/joint_plot.png)

### 4️⃣ Forecasting and Supply chain
**Protocolo:** Descomposición de series de tiempo (modelo aditivo) y proyección de stock.
* **El reto:** Prevenir desabastos (*stockouts*) de material crítico.
* **El análisis:** Se aplicaron promedios móviles (ventan de 3 meses) para filtrar el ruido diario y una descomposición aditiva para aislar la demanda orgánica de los ciclos.
* **El insight:** Desarrollamos un motor de recomendaciones de abastecimiento que suma la tendencia, el efecto estacional del mes y un **Stock de Seguridad dinámico** ($2\sigma$ de los residuos del modelo). 


![Tendencia de ventas](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/tendencia_.png)
![Time series decomposition](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/descomp_demanda.png)
![Tabla de recomendaciones de abastecimiento](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/demanda_esperada.png)



### Tablero dinámico 

Se generó un tablero dinámico que contiene indicadores de rentabilidad, satisfacción del cliente, demanda y recomendaciones de abastecimiento.

En el siguiente link puedes descargar el tablero de prueba:

![Tablero dinámico](https://github.com/Alop89/Projects_portfolio/blob/main/inteligencia_comercial_medtech/reports/figures/medtech.png) 

[Link al tablero de prueba](https://1drv.ms/u/c/13cfd995d9a175b3/IQDfxAisu-CeTIkNg6Epr468AfUpj-43_DJN7b-h-Kul5XQ?e=8sDkKD)

---

## 🚀 SYSTEM OVERRIDE: NEXT STEPS
La fase de análisis estadístico está cerrada. El próximo salto en la red es la **Fase de ingeniería de datos (ETL)**, donde este conocimiento será inyectado en una base de datos PostgreSQL en la nube (Neon) para alimentar un Dashboard.



---
-----

# 🌌 MEDTECH DATA GRID: Intelligence and Market Analysis 🏥⚡(ENG)

> **By ArchData Consulting** 

## 💾 PROJECT OVERVIEW

This project represents the analytical core for medical device and consumable sales. Navigating through a bimodal data ecosystem, the objective was to extract actionable insights for supply chain management, pricing strategies, and customer retention within the HealthTech sector.

We transitioned from raw data generation to advanced statistical inference and time-series modeling.

### 🛠️ TECH STACK (THE MAINFRAME)

  * **Core:** Python 3.x 🐍
  * **Data wrangling:** Pandas, NumPy
  * **Statistics:** SciPy, Statsmodels, Pingouin (ANOVA, Spearman, Games-Howell, Tukey)
  * **Visualization:** Seaborn, Matplotlib (Custom aesthetics), Plotly.
  * **Time series:** Statsmodels (Seasonal Decomposition)

-----

## 📊 CORE INSIGHTS AND BUSINESS LOGIC

### 1️⃣ Analysis of variance (ANOVA)

**Protocol:** One-way ANOVA and Post-Hoc testing (Games-Howell & Tukey).

  * **The challenge:** Do public hospitals purchase differently compared to private ones or specialized clinics?
  * **The analysis:** We detected heteroscedasticity (unequal variances) driven by the public sector. By applying the robust Games-Howell test, it was proven that **no statistically significant difference** ($p > 0.05$) exists in the average ticket across hospital types.
  * **The insight:** Institution type does not dictate total sales volume; the commercial strategy should not be segmented by hospital type, but rather by product category.

### 2️⃣ Anomaly detection

**Protocol:** Global Z-Score vs. Segmented IQR.

  * **The challenge:** Clean the noise from the dataset without destroying high-value information.
  * **The analysis:** Applying a global Z-Score resulted in a 97% false positive rate due to the multimodal nature of the medical sector (low-cost consumables vs. high-cost capital goods). We pivoted toward a **Segmented Interquartile Range (IQR) by category** to identify real cases requiring review to rule out errors or potential fraud.
  * **The insight:** 53 critical operational anomalies (data entry errors or potential fraud) were accurately isolated.

### 3️⃣ Customer Satisfaction

**Protocol:** Spearman's Rank Correlation ($\rho$).

  * **The challenge:** Does higher satisfaction allow for a higher contract ticket in Imaging/Radiology?
  * **The analysis:** Spearman's correlation demonstrated that satisfaction does not alter the unit value of contracts (prices are market-anchored). However, density analysis revealed that "High" satisfaction categories concentrate nearly all revenue.
  * **The insight:** Satisfaction is not a *Price Driver*; it is a **Volume Driver**. In HealthTech, post-sale service guarantees Market Share and purchase frequency.

### 4️⃣ Forecasting and Supply Chain

**Protocol:** Time-series decomposition (Additive Model) and stock projection.

  * **The challenge:** Prevent stockouts of critical materials.
  * **The analysis:** 3-month moving averages were applied to filter daily noise, alongside additive decomposition to isolate organic demand from cycles.
  * **The insight:** We developed a supply recommendation engine that combines trend, monthly seasonal effects, and a **Dynamic safety stock** ($2\sigma$ of the model residuals).

-----

## 🚀 SYSTEM OVERRIDE: NEXT STEPS

The statistical analysis phase is now complete. The next leap into the grid is the **Data Engineering Phase (ETL)**, where this knowledge will be injected into a cloud-based PostgreSQL database (Neon) to power a dynamic Dashboard.

-----

*Developed by **[ArchData Consulting]***
