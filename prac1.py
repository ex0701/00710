# Import the necessary libraries
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("DataStorageDemo").getOrCreate()

# Create sample data
data = [("John", 30), ("Alice", 25), ("Bob", 28), ("Eve", 22)]
columns = ["Name", "Age"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Show the contents of the DataFrame
df.show()

# Save the DataFrame to a Parquet file
df.write.parquet("data.parquet")

# Read data from the Parquet file into a new DataFrame
new_df = spark.read.parquet("data.parquet")

# Show the contents of the retrieved DataFrame
new_df.show()

# Stop the Spark session
spark.stop()
