from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create SparkSession
spark = SparkSession.builder.appName("Average Price by Category").getOrCreate()

# Assuming the "Products" table is already available as a DataFrame named "products"

# Group by category and calculate the average price
average_price_df = products.groupBy("category").agg(avg("price").alias("average_price"))

# Display the result
average_price_df.show()
