from pyspark.sql.functions import col, avg, sum as _sum, min as _min, max as _max, date_trunc, expr
from pyspark.sql.functions import max as _max, min as _min, sum as _sum

from pyspark.sql import SparkSession

# --- SparkSession ---
spark = SparkSession.builder \
    .appName("Silver ETL") \
    .getOrCreate()

# --- JDBC config ---
postgres_host = "😁😁😁😁😁😁"
postgres_port = "5432"
postgres_database = "crypto"
postgres_user = "🤪🤪🤪🤪"
postgres_password = "🤐🤐🤐🤐🤐🤐"
bronze_table = "bronze_crypto.raw_crypto_prices"
silver_table = "silver_crypto.crypto_hourly_summary"

jdbc_url = f"jdbc:postgresql://{postgres_host}:{postgres_port}/{postgres_database}"
connection_properties = {
    "user": postgres_user,
    "password": postgres_password,
    "driver": "org.postgresql.Driver"
}

# --- Step 1: Read from Bronze layer ---
bronze_df = spark.read.jdbc(
    url=jdbc_url,
    table=bronze_table,
    properties=connection_properties
)

# --- Step 2: Filter and extract hour timestamp ---
bronze_df = bronze_df.filter(col("processing_timestamp").isNotNull())
bronze_df = bronze_df.withColumn("hour_start", date_trunc("hour", col("processing_timestamp")))
bronze_df = bronze_df.withColumn("hour_end", expr("hour_start + INTERVAL 1 hour"))


# --- Step 3: Group & Aggregate ---
silver_df = bronze_df.groupBy("id", "symbol", "name", "hour_start", "hour_end").agg(
    avg("current_price").alias("avg_price"),
    _max("current_price").alias("max_price"),
    _min("current_price").alias("min_price"),
    _sum("total_volume").alias("volume"),
    avg("market_cap").alias("market_cap"),
    avg("price_change_percentage_24h").alias("price_change_percentage_24h")
)


# --- Step 4: Write to Silver Layer ---
silver_df.write.jdbc(
    url=jdbc_url,
    table=silver_table,
    mode="append",  # Use "overwrite" only when rebuilding all data
    properties=connection_properties
)

print("✅ Hourly ETL to silver_crypto.crypto_hourly_summary complete!")
