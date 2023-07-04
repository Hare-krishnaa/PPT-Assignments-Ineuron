from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("Retrieve Out of Stock Products").getOrCreate()

# Assuming the "Products" table is already available as a DataFrame named "products"

# Register the "products" DataFrame as a temporary view
products.createOrReplaceTempView("products")

# Retrieve names of products that are currently out of stock
query = '''
    SELECT name
    FROM products
    WHERE stock_quantity = 0
'''

# Execute the SQL query and retrieve the result
result = spark.sql(query)

# Display the result
result.show()
