# 🧬 THE CLINICAL ORACLE: Predictive Risk & Explainable AI in Clinical Trials 🏥🤖
> **By ArchData Consulting** ![Banner Principal](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/arch_data_.png)

## 💾 PROJECT OVERVIEW
Este proyecto representa una solución integral de Machine Learning (MLOps) diseñada para mitigar uno de los mayores riesgos financieros y científicos en la investigación médica: **el abandono de pacientes en ensayos clínicos (Drop-outs)**. 

Pasamos de la limpieza hermética de datos clínicos a la optimización matemática de umbrales predictivos y la implementación de Inteligencia Artificial Explicable (XAI) mediante una aplicación web interactiva para el cuerpo médico.

### 🛠️ TECH STACK (THE MAINFRAME)
* **Core:** Python 3.9+ 🐍
* **Data wrangling:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Pipelines, Logistic Regression, GridSearchCV, StratifiedKFold)
* **Explainable AI (XAI):** SHAP (Valores de Shapley)
* **Visualización:** Matplotlib, Seaborn
* **Despliegue & MLOps:** Streamlit, Joblib

---

## 📊 CORE INSIGHTS AND BUSINESS LOGIC

### 1️⃣ Preprocesamiento hermético (Zero Data Leakage)
**Protocolo:** Arquitectura de pipeline unificado (`ColumnTransformer` + `StandardScaler` + `OneHotEncoder`).
* **El reto:** Evitar que el modelo espiara datos del futuro durante la validación cruzada, un error crítico que invalida modelos médicos.
* **El análisis:** Se encapsuló el preprocesamiento de biomarcadores numéricos y categóricos directamente dentro de la canalización del modelo. Al combinarlo con un `StratifiedKFold` de 5 pliegues, el escalamiento se recalculó desde cero en cada iteración.
* **El insight:** Se garantizó una matriz matemática 100% pura y libre de *Data Leakage*, asegurando que el ROC-AUC (0.783) reportado sea el rendimiento verdadero en el mundo real.

![Distribución](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/box_violin_distribution.png)
![Matriz de Correlación](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/pairplot.png)


### 2️⃣ Optimización de umbral clínico (Threshold Tuning)
**Protocolo:** Curva Precision-Recall y métrica $F_2$-Score.
* **El reto:** El umbral por defecto (50%) en Machine Learning asume que un Falso Positivo cuesta lo mismo que un Falso Negativo. En ensayos clínicos, perder a un paciente (Falso Negativo) cuesta millones.
* **El análisis:** Se forzó al algoritmo a priorizar la sensibilidad del ensayo (Recall). Al optimizar la métrica $F_2$ (que da doble peso al Recall), el límite de decisión se calibró agresivamente al **20.4%**.
* **El insight:** Erradicamos los Falsos Negativos (**Recall del 100%**). El modelo detecta a todos los pacientes en riesgo. Asumimos estratégicamente un volumen menor de falsas alarmas, cuyo costo operativo (una llamada preventiva) es justificable frente a la pérdida de datos del estudio.


![Mutual information graph](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/mutual_info_barplot.png)
![Matriz de confusión clínica](rhttps://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/conf_matrix.png)

### 3️⃣ Inteligencia Artificial Explicable (XAI)
**Protocolo:** Teoría de Juegos de Shapley (SHAP) - Beeswarm & Waterfall Plots.
* **El reto:** Los directores médicos no confían en "Cajas Negras". Necesitan evidencia clínica del porqué detrás de cada alerta predictiva.
* **El análisis:** El modelo fue auditado con SHAP. A nivel global, descubrimos que la privación del tratamiento activo (`Treatment_Arm_Placebo`) es el principal disparador de abandonos, validando que el ensayo sufre por falta de eficacia percibida.
* **El insight:** A nivel local, el sistema descompone el riesgo de cada paciente individual, mostrando exactamente cuántos puntos de riesgo añade su presión arterial o nivel de glucosa, dándole al médico una guía de intervención precisa.

![Análisis global SHAP](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/beeswarm_plot.png)

![Explicación local SHAP](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/waterfall_graph.png)

### Panel clínico interactivo (Streamlit App)
Se generó una aplicación web de soporte a decisiones clínicas (CDSS) donde los especialistas ingresan los biomarcadores del paciente y el motor de inferencia calcula el riesgo y renderiza el razonamiento (SHAP Waterfall) en tiempo real.

![Demo de la App Streamlit](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/streamlit_negative.png) 

![Demo de la App Streamlit](https://github.com/Alop89/Projects_portfolio/blob/main/clinical_oracle/reports/figures/streamlit_positive.png) 

---

## 🚀 SYSTEM OVERRIDE: NEXT STEPS
La fase de inferencia explicable está en producción. El próximo salto en la red es la **Fase de Integración Hospitalaria**, donde este Pipeline se conectará mediante APIs REST a ecosistemas de salud estandarizados (FHIR, HL7v2) para evaluar el riesgo de los pacientes directamente desde sus Expedientes Clínicos Electrónicos (EHR) sin captura manual.

---
-----

# 🧬 THE CLINICAL ORACLE: Predictive Risk & Explainable AI in Clinical Trials 🏥🤖 (ENG)

> **By ArchData Consulting** ## 💾 PROJECT OVERVIEW
This project represents an end-to-end Machine Learning (MLOps) solution designed to mitigate one of the greatest financial and scientific risks in medical research: **patient drop-outs in clinical trials**.

We transitioned from hermetic clinical data cleaning to mathematical predictive threshold optimization and the implementation of Explainable Artificial Intelligence (XAI) via an interactive web app for the medical staff.

### 🛠️ TECH STACK (THE MAINFRAME)
* **Core:** Python 3.9+ 🐍
* **Data wrangling:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Pipelines, Logistic Regression, GridSearchCV, StratifiedKFold)
* **Explainable AI (XAI):** SHAP (Shapley Values)
* **Visualization:** Matplotlib, Seaborn
* **Deployment & MLOps:** Streamlit, Joblib

---

## 📊 CORE INSIGHTS AND BUSINESS LOGIC

### 1️⃣ Hermetic preprocessing (Zero Data Leakage)
**Protocol:** Unified Pipeline Architecture (`ColumnTransformer` + `StandardScaler` + `OneHotEncoder`).
* **The challenge:** Prevent the model from snooping on future data during cross-validation—a critical error that invalidates medical models.
* **The analysis:** Biomarker scaling and categorical encoding were encapsulated directly inside the model's pipeline. Combined with a 5-fold `StratifiedKFold`, the scaling was computed from scratch in each iteration.
* **The insight:** We guaranteed a 100% pure mathematical matrix free of *Data Leakage*, ensuring the reported ROC-AUC (0.783) reflects true real-world performance.

### 2️⃣ Clinical threshold tuning
**Protocol:** Precision-Recall Curve & $F_2$-Score metric.
* **The challenge:** The default ML threshold (50%) assumes a False Positive costs the same as a False Negative. In clinical trials, losing a patient (False Negative) costs millions.
* **The analysis:** We forced the algorithm to prioritize trial sensitivity (Recall). By optimizing the $F_2$ metric (which gives double weight to Recall), the decision boundary was aggressively calibrated to **20.4%**.
* **The insight:** We eradicated False Negatives (**100% Recall**). The model detects every single at-risk patient. We strategically accepted a manageable volume of false alarms, as the operational cost of a preventive check-up is negligible compared to losing trial data.

### 3️⃣ Explainable Artificial Intelligence (XAI)
**Protocol:** Shapley Game Theory (SHAP) - Beeswarm & Waterfall Plots.
* **The challenge:** Medical directors do not trust "Black Boxes." They require clinical evidence detailing the "why" behind every predictive alert.
* **The analysis:** The model was audited using SHAP. Globally, we discovered that deprivation of active treatment (`Treatment_Arm_Placebo`) is the primary driver for drop-outs, validating that the trial suffers from a lack of perceived efficacy.
* **The insight:** Locally, the system breaks down the risk for each individual patient, showing exactly how much risk their blood pressure or glucose level adds, providing the doctor with a precise intervention guide.

### Interactive clinical dashboard (Streamlit App)
A Clinical Decision Support System (CDSS) web app was deployed. Specialists input patient biomarkers, and the inference engine calculates the risk while rendering the model's reasoning (SHAP Waterfall) in real-time.

---

## 🚀 SYSTEM OVERRIDE: NEXT STEPS
The explainable inference phase is now in production. The next leap into the grid is the **Hospital Integration Phase**, where this Pipeline will connect via REST APIs to standardized healthcare ecosystems (FHIR, HL7v2) to evaluate patient risk directly from Electronic Health Records (EHR) with zero manual data entry.

---
*Developed by **ArchData Consulting***