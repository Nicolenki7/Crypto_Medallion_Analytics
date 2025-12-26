# 🚀 Crypto Medallion Ecosystem: De la Ingeniería a la Inferencia Predictiva

**Nicolas Zalazar** | Data & ML Engineer  
**Stack Tecnológico:** Microsoft Fabric (Lakehouse), PySpark, Dataflows Gen2, MLflow, Power BI, Streamlit.

---

## 📖 Storytelling: El Desafío de la Claridad en el Caos
En el mercado de criptoactivos, los datos abundan pero la sabiduría escasea. El problema central no es la falta de información, sino el **ruido**. ¿Es un aumento de precio una tendencia orgánica o una anomalía sin liquidez? 

Este ecosistema fue diseñado con un enfoque de **pensamiento crítico**, priorizando la relación señal-ruido. No es solo un pipeline; es una herramienta de toma de decisiones que recorre todo el ciclo de vida del dato: desde el bit crudo hasta la predicción basada en evidencia.

---

## 🏗️ Fase 1: Ingeniería de Datos y Orquestación (Pipeline)

El proceso comienza con una arquitectura **Medallion** implementada en **Microsoft Fabric**. La clave aquí fue la flexibilidad: utilicé un enfoque híbrido para garantizar que la ingesta no solo fuera rápida, sino resiliente.

![Pipeline de Datos](https://github.com/Nicolenki7/Crypto_Medallion_Analytics/raw/a36083d8ecf27beb88da5b37a0341a340beee8ab/pipeline.png)

* **Ingesta (Bronze):** Combinación de **Dataflows Gen2** para conectividad estructurada y **Notebooks de PySpark** para la carga masiva de históricos.
* **Refinamiento (Silver):** Limpieza, tipado y normalización para eliminar inconsistencias de origen.
* **Servicio de ML:** El pipeline culmina integrando directamente el servicio de entrenamiento y análisis, cerrando el ciclo de ingeniería.

---

## 📂 Fase 2: El Corazón del Negocio (Modelo Semántico)

Una vez refinados, los datos convergen en la capa **Gold**. Aquí es donde la ingeniería se encuentra con la estrategia.

![Modelo Semántico Gold](https://github.com/Nicolenki7/Crypto_Medallion_Analytics/raw/a36083d8ecf27beb88da5b37a0341a340beee8ab/modelosemantico_gold.png)

Este **Modelo Semántico** fue diseñado para soportar consultas de alto rendimiento. Al estructurar las relaciones entre activos, tiempos y métricas de rendimiento, permitimos que el motor de Power BI analice millones de registros con latencia mínima, manteniendo la integridad de las dimensiones de negocio.

---

## 📊 Fase 3: Business Intelligence - El Dashboard Estratégico

El dashboard no es descriptivo, es **interrogativo**. Está diseñado para responder preguntas críticas de inversión a través de tres niveles de profundidad:

### Hoja 1: Panorama General y Estado del Mercado
![Dashboard Hoja 1](https://github.com/Nicolenki7/Crypto_Medallion_Analytics/raw/a36083d8ecf27beb88da5b37a0341a340beee8ab/dashboard_final_!.png)
* **Pregunta de Negocio:** ¿Cuál es el estado actual de los activos y cómo se comparan entre sí en términos de volumen y valor?
* **Respuesta:** Mediante KPIs de alto nivel y comparativas directas, esta hoja permite identificar rápidamente qué activos están liderando el mercado y cuáles presentan anomalías en sus precios de apertura.

### Hoja 2: Análisis de Riesgo y Validación de Tendencias
![Dashboard Hoja 2](https://github.com/Nicolenki7/Crypto_Medallion_Analytics/raw/a36083d8ecf27beb88da5b37a0341a340beee8ab/dashboard_final2.png)
* **Pregunta de Negocio:** ¿Este movimiento de precio tiene respaldo real o es pura volatilidad?
* **Análisis Técnico:** Aquí analizamos la convergencia entre **Volumen y Estabilidad**. Al observar los gráficos de dispersión, el inversor puede detectar si un rally de precios está "respaldado" por liquidez. Si el precio sube pero el volumen se estanca, el gráfico nos advierte de un posible riesgo. Es una matriz de correlación visual para la supervivencia financiera.

### Hoja 3: Performance Histórico y Rankings
![Dashboard Hoja 3](https://github.com/Nicolenki7/Crypto_Medallion_Analytics/raw/a36083d8ecf27beb88da5b37a0341a340beee8ab/dashboard_final3.png)
* **Pregunta de Negocio:** ¿Cómo se posiciona cada activo en el largo plazo y cuál es su tendencia de retorno real?
* **Respuesta:** A través de rankings anuales y tendencias de performance, identificamos los activos con mayor resiliencia. No miramos la foto del día, miramos la película completa para entender la convergencia del valor en el tiempo.

---

## 🧠 Fase 4: Machine Learning - Inferencia Predictiva

El proyecto culmina con un modelo de **Regresión Lineal** entrenado para predecir el precio de cierre mensual basado en variables de la capa Gold (Precio de Inicio, Volatilidad y Volumen).

![Análisis de Machine Learning](https://github.com/Nicolenki7/Crypto_Medallion_Analytics/raw/a36083d8ecf27beb88da5b37a0341a340beee8ab/machine_learning.png)

### El Caso de Bitcoin
En la visualización superior, podemos observar el comportamiento de la regresión. La línea roja no es una simple diagonal; es una **representación multidimensional** que "va y vuelve" porque el modelo está ajustando la predicción no solo al precio, sino al impacto de la volatilidad y el volumen de cada mes. 
* **R² de 0.9863:** Un nivel de precisión altísimo que valida nuestras variables de entrada.
* **Uso Práctico:** El modelo nos permite simular: *"Si la volatilidad proyectada es X, ¿cuál es el precio de salida esperado?"*. Esto transforma la intuición en cálculo.

---

## 🚀 Despliegue y Acceso Directo

Para democratizar estos insights, he desplegado una Web App interactiva donde se puede interactuar con el modelo de ML en tiempo real.

🔗 **[Acceder al Simulador Predictivo en Streamlit](https://crypto-medallion-ml-app-mq3eccyg95sxpc7ytwgoiv.streamlit.app/)**

---

## 🎯 Conclusión
Este ecosistema demuestra que la ingeniería de datos, cuando se aplica con rigor y sentido de negocio, puede reducir drásticamente la incertidumbre. Desde la automatización del pipeline en Fabric hasta la inferencia en la nube con Streamlit, cada paso fue diseñado para maximizar la señal y entregar valor real.
