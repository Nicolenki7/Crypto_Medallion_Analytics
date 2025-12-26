# 🚀 Crypto Medallion Ecosystem: De la Incertidumbre a la Predicción

**Nicolas Zalazar** | Data & ML Engineer  
**Fecha de actualización:** 26/12/2025  
**Stack:** Microsoft Fabric (Lakehouse), PySpark, Dataflows Gen2, MLflow, Power BI, Streamlit.

---

## 📖 El Storytelling: ¿Por qué este proyecto?

En el mercado de criptoactivos, el volumen de datos es abrumador, pero la **señal útil** es escasa. La mayoría de los análisis se quedan en la superficie: el precio actual. Este proyecto nace de una necesidad estratégica: **¿Podemos validar si un movimiento de precio tiene sustento real o es puro ruido especulativo?**

He construido un ecosistema integral que no solo almacena datos, sino que los refina a través de una arquitectura **Medallion** para alimentar un modelo de **Machine Learning** capaz de reducir la incertidumbre en la toma de decisiones financieras.

---

## 🏗️ Ingeniería de Datos: Arquitectura Medallion

Diseñé un pipeline robusto dentro de **Microsoft Fabric**, asegurando que el ciclo de vida del dato fuera trazable y resiliente.

> ![Pipeline Completo](URL_DE_TU_SCREENSHOT_1)
> *Nota: Captura del pipeline integral desde la ingesta hasta el servicio de ML.*

### 1. Ingesta Híbrida (Capa Bronze)
Para la captura de datos crudos, utilicé un enfoque dual:
* **Dataflows Gen2:** Para una conectividad rápida y estructurada con las fuentes externas.
* **Notebooks (PySpark):** Para la orquestación y el manejo de grandes volúmenes de datos históricos.
* **Resultado:** Un aterrizaje de datos sin pérdida de integridad, listos para el refinamiento.

### 2. Transformación y Limpieza (Capa Silver)
Utilizando **Spark SQL**, ejecuté procesos de limpieza profunda: normalización de tipos, manejo de valores nulos y estandarización de divisas. Aquí, el dato crudo se convierte en una tabla Delta optimizada.

### 3. Agregación de Valor (Capa Gold)
Esta es la capa de negocio. Aquí calculamos:
* **Volatilidad Media Mensual:** Para entender el riesgo intrínseco.
* **Volumen Promedio:** Como validador de tendencias.
* **Retorno Real:** La métrica definitiva de éxito.

---

## 📊 Business Intelligence: El Dashboard como Brújula

El informe de **Power BI** no es decorativo; responde preguntas de negocio que definen la supervivencia de una inversión.

> ![Modelo Semántico](URL_DE_TU_SCREENSHOT_MODELO_SEMANTICO)
> *Nota: Visualización del modelo de datos unificado en Fabric.*

### El Insight del Volumen (Página 2 del Informe)
Nos enfrentamos a un problema común: ¿Este aumento de precio es una trampa (bull trap)? 
* **La Respuesta:** Al cruzar el *Precio de Inicio* con el *Volumen Promedio* en gráficos de dispersión, logramos visualizar la liquidez. Si el precio sube pero el volumen baja, el sistema emite una alerta visual. 
* **Impacto:** Esta herramienta permite a los gestores entrar solo en activos con "respaldo de mercado", minimizando entradas en activos manipulados o de baja liquidez.

---

## 🧠 Machine Learning: Predicción basada en Evidencia

El cierre del ecosistema es un modelo predictivo que transforma la historia en proyección.

### El Experimento
Entrenamos una **Regresión Lineal** utilizando las variables de alta señal de la capa Gold. El seguimiento se realizó con **MLflow** para asegurar la reproducibilidad.

* **Métricas Alcanzadas:**
  * **Precisión ($R^2$):** $0.9863$
  * **Error Absoluto Medio (MAE):** $463.49$ USD
* **Conclusión Técnica:** El modelo demuestra una convergencia casi perfecta entre el precio de apertura y las condiciones de volatilidad para predecir el cierre mensual.

> ![MLflow Metrics](URL_DE_TU_SCREENSHOT_METRICAS_ML)
> *Nota: Panel de MLflow mostrando el éxito del entrenamiento.*

---

## 🚀 Despliegue: Streamlit App
Para que el modelo sea útil, lo desacoplamos de la infraestructura de ingeniería y lo llevamos a una aplicación web interactiva.

* **Funcionalidad:** Los usuarios pueden ajustar sliders de volatilidad y volumen para obtener una predicción instantánea del activo seleccionado.
* **Independencia:** La app es autónoma y consume los datos procesados en la capa Gold.

> ![Streamlit App] https://crypto-medallion-ml-app-mq3eccyg95sxpc7ytwgoiv.streamlit.app/
> *Nota: Interfaz final de la aplicación predictiva en la nube.*

---

## 🎯 Conclusión
Este proyecto valida que la **Arquitectura Medallion** no es solo una forma de organizar archivos, sino una metodología para destilar valor. Desde la ingesta híbrida hasta la inferencia en Streamlit, cada paso fue diseñado para maximizar la señal y eliminar el ruido.

---
### 🔗 Enlaces de interés
* [Acceder al Simulador de ML (Streamlit)](TU_LINK_AQUI)
* [Ver Informe Estratégico (Power BI)](TU_LINK_AQUI)
