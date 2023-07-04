from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.window import Window
from pyspark.sql.functions import desc

# Create SparkSession
spark = SparkSession.builder.appName("Total Revenue").getOrCreate()

# Assuming "sales_data" DataFrame is already available

# Calculate total revenue for each product
total_revenue_df = sales_data.groupBy("product_name").agg(sum("revenue").alias("total_revenue"))

# Sort the DataFrame in descending order of total revenue
sorted_df = total_revenue_df.orderBy(desc("total_revenue"))

# Display the result
sorted_df.show()
