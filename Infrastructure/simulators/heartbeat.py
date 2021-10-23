import pandas as pd
import random
from time import sleep
from json import dumps
from kafka import KafkaProducer

"""
HEARTBEAT SIMULATOR

Our source of information that it is going to be passed on to our Application needs to be 
delivered from an IoT device, we tested with different simulators but those only have 
circuit simulation as on/off signal. With that in mind we needed to build our own simulator
to produce the data that it is needed. 

"""

# Bootstrap servers information to pass data to Kafka 

producer = KafkaProducer(bootstrap_servers=['172.17.0.1:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

# We found heartrate data CSV taht has data from an actual IoT device, we DO NOT stream this data, we just use it as reference to make our simualation

heartrate = pd.read_csv('ring_data.csv', header=None)