"""
 Counts words in UTF8 encoded, '\n' delimited text directly received from Kafka in every 2 seconds.
 Usage: direct_kafka_wordcount.py <broker_list> <topic>

 To run this on your local machine, you need to setup Kafka and create a producer first, see
 http://kafka.apache.org/documentation.html#quickstart

 and then run the example
    `$ ./bin/spark-submit --packages external/kafka-assembly/target/scala-*/spark-streaming-kafka-assembly-*.jar /home/abzooba/code/datastream/connect.py localhost:2181 ashleyexp`
"""

import findspark
findspark.init()
import pyspark
import json
import pprint
import pymysql.cursors
import pymysql.connections
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
sc = SparkContext(appName="datastream")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc,15)
#brokers = "52.44.255.113:2181"

def user(con, data):
    with con.cursor() as cur:
        if 'address' in data:
            address = data['address']
            if 'user' in address:
                user = address['user']
                if 'name' in user:
                    userName = user['name'].split(" ")
                    # print("123",userName)
                    firstName = str(userName[0])
                    lastName = str(userName[1])
                else:
                    firstName = ""
                    lastName = ""
                if 'id' in user:
                    userId = str(user['id'])
                else:
                    userId = ""
            else:
                firstName = ""
                lastName = ""
                userId = ""
        else:
            firstName = ""
            lastName = ""
            userId = ""
        if 'timestamp' in data:
            firstActiveTs = str(data['timestamp'])
        else:
            firstActiveTs = ""
        if 'profile_pic_link' in data:
            profilePicLink = str(data['profile_pic_link'])
        else:
            profilePicLink = ""
        if 'locale' in data:
            locale = str(data['locale'])
        else:
            locale = ""
        if 'timezone' in data:
            timezone = str(data['timezone'])
        else:
            timezone = ""
        if 'gender' in data:
            gender = str(data['gender'])
        else:
            gender = ""
        if 'is_payment_enabled' in data:
            isPaymentEnabled = str(data['is_payment_enabled'])
        else:
            isPaymentEnabled = ""
        if 'marked_spam' in data:
            markedSpam = str(data['marked_spam'])
        else:
            markedSpam = ""
        if 'has_blocked' in data:
            hasBlocked = str(data['has_blocked'])
        else:
            hasBlocked = ""
        # print("testingrajgopal", userId)
        sql = "SELECT `user_id` from `user` WHERE `user_id`= " + userId
        cur.execute(sql)
        data = cur.fetchall()
        if len(data) <= 0 :
            sql1 = "INSERT INTO `user` (`user_id`, `first_active_ts`, `first_name`, `last_name`, `profile_pic_link`, `locale`, `timezone`, `gender`, `is_payment_enabled`, `marked_spam`, `has_blocked`) VALUES ('" + userId + "' , '" + firstActiveTs+ "' , '" + firstName+ "' , '" + lastName+ " ',' " + profilePicLink+ " ', '" + locale+ " ', '" + timezone+ " ', '" + gender+ " ', '" + isPaymentEnabled+ " ', '" + markedSpam+ " ', '" + hasBlocked+ "')"
            # print("1")
            # print(sql1)
            cur.execute(sql1)
            cur.close()
    con.commit()

def chatlog(con, data):
    with con.cursor() as cur:
        if 'address' in data:
            address = data['address']
            if 'user' in address:
                user = address['user']
                if 'id' in user:
                    userId = str(user['id'])
                else:
                    userId = ""
            else:
                userId = ""
            if 'channelId' in address:
                channelId = str(address['channelId'])
            else:
                channelId = ""
        else:
            userId = ""
            channelId = ""
        if 'timestamp' in data:
            timestamp = str(data['timestamp'])
        else:
            timestamp = ""
        if 'session_id' in data:
            sessionNumber = str(data['session_id'])
        else:
            sessionNumber = ""
        if 'message_number' in data:
            messageNumber = str(data['message_number'])
        else:
            messageNumber = ""
        if '' in data:
            messageType = str(data['message_type'])
        else:
            messageType = ""
        if 'message_chat'  in data:
            messageChat = con.escape_string( data['message_chat'] )
        else:
            messageChat = ""
        if 'message_type_flag' in data:
            messageTypeFlag = str(data['message_type_flag'])
        else:
            messageTypeFlag = ""
        if 'visual_search' in data:
            visualSearch = con.escape_string( str(data['visual_search']) )
        else:
            visualSearch = ""
        if 'product_response_list' in data:
            if data['product_response_list'] != "":
                productResponseList = con.escape_string( json.dumps(str(data['product_response_list'])) )
            else:
                productResponseList = json.dumps(str({}))
        else:
            productResponseList = json.dumps(str({}))
        if 'nlp_query_response' in data:
            nlpQueryResponse = con.escape_string( str(data['nlp_query_response']) )
        else:
            nlpQueryResponse = ""
        if 'vision_file_link' in data:
            visionFileLink = str(data['vision_file_link'])
        else:
            visionFileLink = ""
        if 'vision_engine_response' in data:
            visionEngineResponse = con.escape_string( str(data['vision_engine_response']) )
        else:
            visionEngineResponse = ""
        if 'quick_reply_buttons' in data:
            quickReplyButton = con.escape_string( str(data['quick_reply_buttons']) )
        else:
            quickReplyButton = ""
        sql2 = "INSERT INTO `chatlog` (`user_id`, `timestamp`, `channel_id`, `session_id`, `message_number`, `message_type`, `message_chat`, `message_type_flag`, `visual_search`, `product_response_list`, `nlp_query_response`, `vision_file_link`, `vision_engine_response`, `quick_reply_button` ) VALUES ('" + userId + "' , '" + timestamp + "' , '" + channelId + "' , '" + sessionNumber + "' , '" + messageNumber + "' , '" + messageType + "' , '" + messageChat + "' , '" + messageTypeFlag + "' , '" + visualSearch + "' , '" + str(productResponseList) + "' , '" + nlpQueryResponse + "' , '" + visionFileLink + "' , '" + visionEngineResponse + "' , '" + quickReplyButton + "')"
        # print("2")
        # print(sql2)
        cur.execute(sql2)
        cur.close()
    con.commit()

def click(con, data):
    with con.cursor() as cur:
        if 'address' in data:
            address = data['address']
            if 'user' in address:
                user = address['user']
                if 'id' in user:
                    userId = str(user['id'])
                else:
                    userId = ""
            else:
                userId = ""
        else:
            userId = ""
        if 'session_id' in data:
            sessionNumber = str(data['session_id'])
        else:
            sessionNumber = ""
        if 'message_number' in data:
            messageNumber = str(data['message_number'])
        else:
            messageNumber = ""
        if 'timestamp' in data:
            timestamp = str(data['timestamp'])
        else:
            timestamp = ""
        if 'click_item_sku' in data:
            if data['click_item_sku'] != "" :
                clickItem = str(data['click_item_sku'])
                sql3 = "INSERT INTO `click` (`user_id`, `session_id`, `message_number`, `timestamp`, `click_item`) VALUES ('" + userId + "' , '" + sessionNumber + "' , '" + messageNumber + "' , '" + timestamp + "' , '" + clickItem + "')"
                # print("3")
                # print(sql3)
                cur.execute(sql3)
                cur.close()
        else:
            clickItem = ""
    con.commit()    

num = 1000
def takeAndPrint(rdd):
    Host = '54.173.2.137'
    Port = 3307
    User = 'root'
    Password = 'Abz00ba1nc'
    Charset = 'utf8'
    con_jeanie = pymysql.connect(host = Host, port = Port, user = User, password = Password, db = 'jeanie_metricdb', charset = Charset)
    con_botcoture = pymysql.connect(host = Host, port = Port, user = User, password = Password, db = 'botcoture_metricdb', charset = Charset)
    con_expconsumerapp = pymysql.connect(host = Host, port = Port, user = User, password = Password, db = 'expconsumerapp_metricdb', charset = Charset)
    taken = rdd.take(num + 1)
    
    for record in taken[:num]:
        row = json.loads(record[1])
        # print(row)
        botcoture_id = '1810940785897042'
        expconsumerapp_id = '1815860935330860'
        jeanieexp_id = '640615506130372'
        botId = ''
        if 'address' in row:
            address = row['address']
            if 'bot' in address:
                bot = address['bot']
                if 'id' in bot:
                    botId = str(bot['id'])
                else:
                    botId = ""
                    print("No bot present1")
            else:
                botId = ""
                print("No bot present2")
        else:
            userId = ""
            print("No bot present3")
        if botId == botcoture_id:
            print(botId)
            con = con_botcoture
            user(con, row)
            chatlog(con, row)
            click(con, row)
        elif botId == jeanieexp_id:
            print(botId)
            con = con_jeanie
            user(con, row)
            chatlog(con, row)
            click(con, row)
        elif botId == expconsumerapp_id:
            print(botId)
            con = con_expconsumerapp
            user(con, row)
            chatlog(con, row)
            click(con, row)
topics = {'ashleyexp': 1}
#kafkastream = KafkaUtils.createStream(ssc, "34.203.102.251:2181", 'test-consumer-group', topics)
kafkastream = KafkaUtils.createStream(ssc, "34.203.102.251:2181", 'test-consumer-group', topics)
parsed = kafkastream.foreachRDD(takeAndPrint)

ssc.start()
ssc.awaitTermination()
