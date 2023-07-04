from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create SparkSession
spark = SparkSession.builder.appName("Average Transaction").getOrCreate()

# Assuming "transactions" DataFrame is already available

# Calculate average transaction amount for each user
average_amount_df = transactions.groupBy("user_id").agg(avg("amount").alias("average_amount"))

# Display the result
average_amount_df.show()
