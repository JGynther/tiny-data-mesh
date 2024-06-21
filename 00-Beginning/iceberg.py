from pyspark.sql import SparkSession

ICEBERG_JAR = "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2"
ICEBERG_EXTENSION = "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"

spark = (
    SparkSession.builder.appName("sandbox")
    .config("spark.jars.packages", ICEBERG_JAR)
    .config("spark.sql.extensions", ICEBERG_EXTENSION)
    .config("spark.sql.catalog.sandbox", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.sandbox.type", "hadoop")
    .config("spark.sql.catalog.sandbox.warehouse", "warehouse")
    .getOrCreate()
)

spark.sql(
    "CREATE TABLE sandbox.test (first_name string, last_name string) USING iceberg;"
)
