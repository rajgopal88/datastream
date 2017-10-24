"""
 Counts words in UTF8 encoded, '\n' delimited text directly received from Kafka in every 2 seconds.
 Usage: direct_kafka_wordcount.py <broker_list> <topic>

 To run this on your local machine, you need to setup Kafka and create a producer first, see
 http://kafka.apache.org/documentation.html#quickstart

 and then run the example
    `$ ./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.1.0 /home/abzooba/code/datastream/connect1.py`
"""
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.streaming import DataStreamReader
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.types import StructType

spark = SparkSession.builder \
    .master("local") \
    .appName("analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

#ip = 52.44.255.113

ds1 = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ashleyexp") \
    .load()

ds1.printSchema()
ds1.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Split the lines into words
# word = ds1.select(
#    explode(
#        split(ds1.value, ",")
#    ).alias("word")
# )

# Generate running word count
# wordCounts = word.groupBy("word").count()

user = df.select("value").distinct()

user = words \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

user.awaitTermination()