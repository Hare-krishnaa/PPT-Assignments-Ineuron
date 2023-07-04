from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, desc

# Create SparkSession
spark = SparkSession.builder.appName("Top 5 Customers").getOrCreate()

# Assuming the "Transactions" table is already available as a DataFrame named "transactions"

# Group by customer and calculate the total amount spent on purchases
total_amount_df = transactions.groupBy("customer").agg(sum("amount").alias("total_amount"))

# Sort the DataFrame by the total amount spent in descending order
sorted_df = total_amount_df.orderBy(desc("total_amount"))

# Retrieve the top 5 customers
top_5_customers = sorted_df.limit(5)

# Display the result
top_5_customers.show()
