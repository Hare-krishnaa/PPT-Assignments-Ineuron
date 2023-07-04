from pyspark.sql import SparkSession
from pyspark.sql.functions import hour
from pyspark.sql.functions import count

# Create SparkSession
spark = SparkSession.builder.appName("Count Events").getOrCreate()

# Assuming "logs" DataFrame is already available

# Extract hour from timestamp column
logs_with_hour = logs.withColumn("hour", hour("timestamp"))

# Count the number of events for each hour
event_counts_df = logs_with_hour.groupBy("hour").agg(count("event").alias("event_count"))

# Sort the DataFrame by hour
sorted_df = event_counts_df.orderBy("hour")

# Display the result
sorted_df.show()
