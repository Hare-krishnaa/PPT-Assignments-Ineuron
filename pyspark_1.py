from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("Read CSV").getOrCreate()

# Read CSV file into a DataFrame
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# Display the top 10 records
df.show(10)
