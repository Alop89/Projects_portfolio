# 🌌 NEON GRID: Análisis del Embudo de Conversión y Pruebas A/B
Este proyecto decodifica el comportamiento del usuario y la efectividad del embudo de conversión dentro de una plataforma digital. Para lograrlo, procesamos un dataset de eventos, aislando la señal del ruido a partir del 31 de julio de 2019, fecha en la que los flujos de datos mostraron un pico de actividad significativa (con una pérdida de datos casi nula del 0.32%).

El análisis divide a los usuarios en tres sectores de la red: dos grupos de control (Protocolos 246 y 247) y un grupo de prueba (Protocolo 248).

## 🕹️ El embudo (secuencia de eventos)

Al rastrear la huella digital de los usuarios ("total_events"), mapeamos la ruta principal del sistema:

* MainScreenAppear (Pantalla de inicio)

* OffersScreenAppear (Carga de ofertas)

* CartScreenAppear (Terminal del carrito)

* PaymentScreenSuccessful (Transacción exitosa)

* Tutorial (Módulo de asistencia auxiliar)

## 📊 Insights del Sistema
El punto crítico del sistema se encuentra entre la pantalla principal y las ofertas, conservando solo al 62% de los usuarios. Aquí es donde la interfaz necesita una actualización de hardware/software para captar mejor el interés.

Sobremarcha : Una vez superada la barrera inicial, la retención es de alto rendimiento: 81% avanza de las ofertas al carrito, y un masivo 94.7% completa el pago. El circuito de compra final está hiper-optimizado.

Módulo de tutorial inactivo: Solo el 4.2% de los usuarios activa el tutorial, sugiriendo que la navegación es intuitiva o que el módulo está oculto en la interfaz. La distribución general muestra que la mayoría de los dispositivos registran un número bajo de eventos.

## 🧬 Diagnóstico estadístico (A/A/B Testing)
Se ejecutaron pruebas de proporciones para evaluar el impacto de las variaciones en los grupos experimentales.

Hipótesis Nula (H0): Los algoritmos de los grupos operan sin diferencias estadísticas.

Resolución: Para evitar sobrecargar el sistema con falsos positivos (Error Tipo I) al realizar múltiples comparaciones, calibramos el análisis con la Corrección de Bonferroni, ajustando el nivel de significancia a 0.05.

Resultado Final: Los datos confirmaron la hipótesis nula (p-valor > alfa). No se encontraron diferencias estadísticas significativas entre los grupos de control, ni entre los grupos de control y el de prueba en ninguna de las etapas.



### 📊 Gráficos generados

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/Alop89/Projects_portfolio/blob/main/ab_test/reports/figures/distribucion_eventos.png?raw=true" width="400px"/>
      <br /><b>Distribución de eventos por usuarios</b>
    </td>
    <td align="center">
      <img src="https://github.com/Alop89/Projects_portfolio/blob/main/ab_test/reports/figures/eventos_usuarios_unicos.png?raw=true" width="400px"/>
      <br /><b>Eventos por usuarios únicos</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/Alop89/Projects_portfolio/blob/main/ab_test/reports/figures/timeline.png?raw=true" width="400px"/>
      <br /><b>Evolución de datos respecto al tiempo</b>
    </td>
    <td align="center">
      <img src="https://github.com/Alop89/Projects_portfolio/blob/main/ab_test/reports/figures/embudo.png?raw=true" width="400px"/>
      <br /><b>Embudo de eventos</b>
    </td>
  </tr>
</table>

---

### 📺 Full Presentation

A continuación, puedes acceder a la presentación completa del proyecto. Haz clic en la imagen para abrir el archivo en Google Slides:

<p align="center">
  <a href="https://docs.google.com/presentation/d/1sjTefAV15vfuypZ0-MEgZdVjGfL6E-JTydEaufR-NyQ/edit?usp=sharing">
    <img src="https://github.com/Alop89/Projects_portfolio/blob/main/ab_test/reports/figures/presentation.png?raw=true" width="700px" alt="Presentation Cover">
  </a>
</p>

[👉 Click here to view the presentation](https://docs.google.com/presentation/d/1sjTefAV15vfuypZ0-MEgZdVjGfL6E-JTydEaufR-NyQ/edit?usp=sharing)


También está disponible un dashboard de prueba que contien los datos usados para el proyecto:

<p align="center">
  <a href="https://docs.google.com/presentation/d/1sjTefAV15vfuypZ0-MEgZdVjGfL6E-JTydEaufR-NyQ/edit?usp=sharing">
    <img src="https://github.com/Alop89/Projects_portfolio/blob/main/ab_test/reports/figures/dash_v1.0.png" width="700px" alt="Presentation Cover">
  </a>
</p>




## 🇺🇸 English Version
# 🌌 NEON GRID: Conversion Funnel & A/A/B Testing Analysis 🌌
Booting up analysis sequence...
This project decodes user behavior and conversion funnel effectiveness within our digital platform. To achieve this, we processed a massive event dataset, isolating the signal from the noise starting July 31, 2019, a timestamp that marked a massive surge in data streams (maintaining optimal data integrity with only 0.32% data loss).

The analysis segments users into three distinct grid sectors: two control groups (Protocols 246 and 247) and one test group (Protocol 248).

## 🕹️  The Neon Funnel (Event Sequence)
By tracking user digital footprints ("total_events"), we successfully mapped the mainframe's core pathway:

* MainScreenAppear

* OffersScreenAppear

* CartScreenAppear

* PaymentScreenSuccessful

* Tutorial (Auxiliary Support Module)

## 📊 System Insights
Initial Voltage Drop: The critical system bottleneck occurs between the main screen and the offers, retaining only 62% of users. This is where the UI needs a serious visual or structural upgrade to hook users.

End-Circuit Overdrive: Once users pass the initial firewall, retention hits peak performance: 81% advance from offers to the cart, and a massive 94.7% complete the payment. The final checkout loop is hyper-optimized.

Dormant Tutorial Module: Only 4.2% of users jack into the tutorial. This suggests either the UI is inherently intuitive, or the module is hidden deep within the grid. Overall distribution shows most devices register a low frequency of events.

## 🧬 Statistical Diagnostics (A/A/B Testing)
Proportion tests were executed to evaluate the impact of the variations across the grid sectors.

Null Hypothesis (H0): The algorithms across all groups operate with no significant statistical difference.

Resolution: To prevent system overload from false positives (Type I Error) during multiple comparisons, we calibrated the matrix using the Bonferroni Correction, hardcoding the significance level to 0.05.

Final Output: The data streams confirmed the null hypothesis (p-value > alpha). No statistically significant differences were found between the control groups, nor between the control and test groups at any stage of the funnel.

