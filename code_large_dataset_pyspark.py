from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("AnonymizeData") \
    .getOrCreate()

# Load CSV into Spark DataFrame
df = spark.read.csv('data.csv', header=True, inferSchema=True)

# Anonymize first_name, last_name, and address columns
df_anonymized = df.withColumn('first_name', sha2('first_name', 256)) \
                  .withColumn('last_name', sha2('last_name', 256)) \
                  .withColumn('address', sha2('address', 256))

# Write anonymized DataFrame to CSV
df_anonymized.write.csv('anonymized_data_spark', header=True, mode='overwrite')

# Stop SparkSession
spark.stop()
