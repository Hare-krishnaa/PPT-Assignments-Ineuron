from pyspark.sql import SparkSession
from pyspark.sql.functions import count
from pyspark.sql.functions import desc

# Create SparkSession
spark = SparkSession.builder.appName("Total Orders").getOrCreate()

# Assuming the "Orders" table is already available as a DataFrame named "orders"

# Group by customer and count the number of orders
order_counts_df = orders.groupBy("customer").agg(count("order_id").alias("order_count"))

# Sort the DataFrame by the number of orders in descending order
sorted_df = order_counts_df.orderBy(desc("order_count"))

# Display the result
sorted_df.show()
