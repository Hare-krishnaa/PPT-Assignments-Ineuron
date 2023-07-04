from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create SparkSession
spark = SparkSession.builder.appName("Read JSON").getOrCreate()

# Read JSON file into a DataFrame
df = spark.read.json("students.json")

# Filter DataFrame to include only students whose age is greater than 18
filtered_df = df.filter(col("age") > 18)

# Display the filtered DataFrame
filtered_df.show()
