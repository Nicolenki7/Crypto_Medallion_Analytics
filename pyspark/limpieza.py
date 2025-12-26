from pyspark.sql.functions import col, month, year, dayofweek, date_format, quarter

# 1. Leer de la tabla Bronze
df_bronze = spark.table("bronze_crypto_diario_historico")

# 2. Limpieza de Duplicados
# Solo un registro por moneda y por día
df_clean = df_bronze.dropDuplicates(["ID_Moneda", "Fecha"])

# 3. Enriquecimiento Temporal (Estacionalidad)
df_silver = df_clean.withColumn("Anio", year(col("Fecha"))) \
                    .withColumn("Mes_Numero", month(col("Fecha"))) \
                    .withColumn("Mes_Nombre", date_format(col("Fecha"), "MMMM")) \
                    .withColumn("Dia_Semana", date_format(col("Fecha"), "EEEE")) \
                    .withColumn("Trimestre", quarter(col("Fecha")))

# 4. Guardar en la Capa Silver
# Nombre técnico: silver_crypto_diario
df_silver.write.format("delta") \
         .mode("overwrite") \
         .option("overwriteSchema", "true") \
         .saveAsTable("silver_crypto_diario")

# resultado
display(df_silver.select("ID_Moneda", "Fecha", "Mes_Nombre", "Dia_Semana").limit(10))
