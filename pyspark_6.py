from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("Retrieve Customers").getOrCreate()

# Assuming the "Customers" table is already available as a DataFrame named "customers"

# Register the "customers" DataFrame as a temporary view
customers.createOrReplaceTempView("customers")

# Retrieve customers whose age is greater than 25 and have made at least one purchase
query = '''
    SELECT *
    FROM customers
    WHERE age > 25 AND purchases > 0
'''

# Execute the SQL query and retrieve the result
result = spark.sql(query)

# Display the result
result.show()
