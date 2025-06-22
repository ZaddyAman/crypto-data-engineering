# spark_etl.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Step 1: Start Spark
spark = SparkSession.builder \
    .appName("CryptoNewsETL") \
    .getOrCreate()

# Step 2: Read data
df = spark.read.text("crypto_news_data.txt")

# Step 3: Basic parsing
# Assume format: "COIN | SENTIMENT | TITLE"
df_split = df.selectExpr("split(value, '\\|') as parts") \
             .selectExpr("trim(parts[0]) as coin", "trim(parts[1]) as sentiment", "trim(parts[2]) as headline")

# Step 4: Map sentiment to numeric
df_final = df_split.withColumn("sentiment_score", when(col("sentiment") == "Positive", 1)
                                                  .when(col("sentiment") == "Negative", -1)
                                                  .otherwise(0))

# Step 5: Show result
df_final.show(truncate=False)

# Step 6: Save to CSV for ML model
df_final.write.mode("overwrite").csv("processed_crypto_news", header=True)

spark.stop()
