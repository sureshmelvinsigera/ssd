from kafka import KafkaConsumer
from json import loads
import sys
import psycopg2
from psycopg2 import Error


'''
KAFKA CONSUMER AND POSTGRES INTEGRATION

The final step of the data flow goes to the PostgreSQL

'''

consumer = KafkaConsumer(
    'blood',
     bootstrap_servers=['172.17.0.1:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


param_dic = {
    "host"      : "172.17.0.1",
    "database"  : "ssd_iss",
    "user"      : "postgres",
    "password"  : "Xoco_137946"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

for message in consumer:
    message = message.value