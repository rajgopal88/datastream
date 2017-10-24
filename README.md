# My project's README
To run this project locally in our system check the below link

There needs to be a Spark setup and Jupyter setup
https://docs.google.com/document/d/19cSpXTHsik9jf7f0tkByYxgz8u9My9QIXXbG2M6Wfmg/edit

To run the connect.py file which is same as the jupyter notebook

./bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2,org.apache.spark:spark-streaming-kafka_2.10:1.6.3,mysql:mysql-connector-java:5.1.17 /datastream/connect.py# datastream
