from pyspark import SparkConf, SparkContext

# Create Spark configuration
conf = SparkConf().setAppName("WordCount")

# Create Spark context
sc = SparkContext(conf=conf)

# Load input text file
input = sc.textFile("YourInputFile.txt")

# Split each line into words and count occurrences
wordCounts = input \
    .flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

# Save the word counts to an output text file
wordCounts.saveAsTextFile("YourOutputFolder")

# Stop the Spark context
sc.stop()


spark-submit --master <spark-master-url> <path-to-python-file>
