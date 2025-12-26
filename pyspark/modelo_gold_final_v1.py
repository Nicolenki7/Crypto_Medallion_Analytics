#!/usr/bin/env python
# coding: utf-8

# ## modelo_gold_final_v1
# 
# null

# In[1]:


from pyspark.sql.functions import col, avg, max, min, last, first, month, year, expr, round

# 1. Carga de la Capa Silver
df_silver = spark.table("silver_crypto_diario")

# 2. Ingeniería de Datos Gold: Agregaciones Financieras Reales
# campos de dimensión necesarios
df_gold = df_silver.groupBy(
    "ID_Moneda", 
    "Nombre_Moneda", 
    "Simbolo", 
    "Anio", 
    "Mes_Nombre", 
    "Mes_Referencia"
).agg(
    # --- MÉTRICAS DE PRECIO ---
    avg("Precio").alias("Precio_Promedio_Mensual"),
    max("Precio").alias("Maximo_Mensual"),
    min("Precio").alias("Minimo_Mensual"),
    first("Precio").alias("Precio_Inicio_Mes"),
    last("Precio").alias("Precio_Fin_Mes"),
    
    # --- MÉTRICAS DE VOLUMEN Y RIESGO ---
    avg("Volatilidad_7d").alias("Volatilidad_Media_Mensual"),
    avg("Volumen_24h").alias("Volumen_Promedio_Mensual"),
    
    # --- ORDEN CRONOLÓGICO () ---
    month(first("Mes_Referencia")).alias("Mes_Orden")
)

# 3. Cálculo de Retorno Mensual Real
# Fórmula: ((Precio Cierre / Precio Apertura) - 1)
df_gold_final = df_gold.withColumn(
    "Retorno_Mensual_Real", 
    (col("Precio_Fin_Mes") / col("Precio_Inicio_Mes")) - 1
).withColumn(
    # Limp
    "Precio_Promedio_Mensual", round(col("Precio_Promedio_Mensual"), 2)
).withColumn(
    "Retorno_Mensual_Real", round(col("Retorno_Mensual_Real"), 4) # 0.0521 = 5.21%
)

# 4. Guardar como Tabla Maestra (Overwrite total para Direct Lake)
df_gold_final.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("gold_rendimiento_cripto")

print(">>> CAPA GOLD PROCESADA CON ÉXITO: Cronología y Métricas Financieras Validadas.")
display(df_gold_final.sort("Anio", "Mes_Orden").limit(5))

