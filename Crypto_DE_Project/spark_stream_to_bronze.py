from pyspark.sql.functions import from_json, col, current_timestamp, to_json,lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, TimestampType, BooleanType
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaToBronzeStreaming") \
    .getOrCreate()



# --- Kafka and PostgreSQL Configuration ---
kafka_bootstrap_servers = "😒😒😒😒:9092"
kafka_topic = "crypto-prices"

postgres_host = "😊😊😊😊"
postgres_port = "5432"
postgres_database = "crypto"
postgres_user = "postgres"
postgres_password = "🤪🤪🤪🤪🤪🤪🤪"
postgres_table = "Bronze_Crypto.raw_crypto_prices"

jdbc_url = f"jdbc:postgresql://{postgres_host}:{postgres_port}/{postgres_database}"

# --- Define Schema for Incoming JSON ---
crypto_schema = StructType([
    StructField("id", StringType(), True),
    StructField("symbol", StringType(), True),
    StructField("name", StringType(), True),
    StructField("image", StringType(), True),
    StructField("current_price", DoubleType(), True),
    StructField("market_cap", DoubleType(), True),
    StructField("market_cap_rank", LongType(), True),
    StructField("fully_diluted_valuation", DoubleType(), True),
    StructField("total_volume", DoubleType(), True),
    StructField("high_24h", DoubleType(), True),
    StructField("low_24h", DoubleType(), True),
    StructField("price_change_24h", DoubleType(), True),
    StructField("price_change_percentage_24h", DoubleType(), True),
    StructField("market_cap_change_24h", DoubleType(), True),
    StructField("market_cap_change_percentage_24h", DoubleType(), True),
    StructField("circulating_supply", DoubleType(), True),
    StructField("total_supply", DoubleType(), True),
    StructField("max_supply", DoubleType(), True),
    StructField("ath", DoubleType(), True),
    StructField("ath_change_percentage", DoubleType(), True),
    StructField("ath_date", StringType(), True),
    StructField("atl", DoubleType(), True),
    StructField("atl_change_percentage", DoubleType(), True),
    StructField("atl_date", StringType(), True),
    StructField("roi", StructType([
        StructField("times", DoubleType(), True),
        StructField("currency", StringType(), True),
        StructField("percentage", DoubleType(), True),
    ]), True),
    StructField("last_updated", StringType(), True)
])

# --- Read from Kafka ---
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "earliest") \
    .load()

# --- Parse Kafka JSON & Add Timestamp ---
parsed_df = kafka_df.selectExpr("CAST(value AS STRING) as json_str") \
    .withColumn("data", from_json(col("json_str"), crypto_schema)) \
    .select("data.*") \
    .withColumn("processing_timestamp", current_timestamp()) \
    .withColumn("roi", to_json(col("roi")))

# --- Define foreachBatch Sink ---
def upsert_to_postgres(df, epoch_id):
    try:
        if df.rdd.isEmpty():
            print(f"Epoch {epoch_id}: Empty batch.")
            return

        print(f"Epoch {epoch_id}: Writing {df.count()} rows to PostgreSQL.")
        df.write \
            .format("jdbc") \
            .option("url", jdbc_url) \
            .option("dbtable", postgres_table) \
            .option("user", postgres_user) \
            .option("password", postgres_password) \
            .option("driver", "org.postgresql.Driver") \
            .mode("append") \
            .save()
        print(f"Epoch {epoch_id}: Success.")
    except Exception as e:
        import traceback
        print(f"Epoch {epoch_id}: ERROR writing to PostgreSQL")
        traceback.print_exc()
        raise

# --- Start the Streaming Write ---
# Final step: start the stream
query = parsed_df.writeStream \
    .foreachBatch(upsert_to_postgres) \
    .outputMode("append") \
    .trigger(processingTime="10 seconds") \
    .start()

print("✅ Stream started. Writing to PostgreSQL every 10 seconds.")

# ✅ Keeps the stream alive
query.awaitTermination()
