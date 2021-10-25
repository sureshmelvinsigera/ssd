import pandas as pd
import random
from time import sleep
from json import dumps
import logging
from kafka import KafkaProducer

"""
HEARTBEAT SIMULATOR

After the first test, a more direct simulation with data with Systolic and Diastolic information were implemented
this data is created following a NORMAL/ELEVATED/HIGH pattern (Whelton et al. 2017)

"""
# Bootstrap servers information to pass data to Kafka

producer = KafkaProducer(bootstrap_servers=[
                         '${KAFKA_IP}:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

# This function returns systolic data


def retSys(r='normal'):
    if r == 'normal':
        a = 120.1
        b = 120.9
    elif r == 'elevated':
        a = 121.1
        b = 129.9
    elif r == 'high':
        a = 130.1
        b = 135.9
    return a, b

# This function returns diastolic data


def retDys(r='normal'):
    if r == 'normal':
        a = 80.1
        b = 80.9
    elif r == 'elevated':
        a = 75.1
        b = 80.9
    elif r == 'high':
        a = 81.1
        b = 90.9
    return a, b

# MIN and MAX ranges of systolic and diastolic info are passed to this variables


rate = 'high'  # Changing the variable syncs both variables to give a consistent sys/dis tuple

sys = retSys(rate)
dys = retDys(rate)

count = 0

for x in range(1440):  # Produces 24 hours of heartbeat data
    e = round(random.uniform(sys[0], sys[1]), 1)  # Randomize sys variable
    f = round(random.uniform(dys[0], dys[0]), 1)  # Randomize dys variable
    data = {'sys': e, 'dys': f, 'astronaut_id': 1, 'count': count}  # Create
    try:
        producer.send('blood', value=data)
    except:
        # Log the issue that prevented data to be saved, and then try again
        logging.basicConfig(level=logging.INFO, filename='error.log')
        continue
    print(data)
    sleep(60)

"""

REFERENCES

National High Blood Pressure Education Program (2003) Prevention, Detection, 
Evaluation. Bethesda, MD: National Heart, Lung, and Blood Institute. Available from: 
https://www.nhlbi.nih.gov/files/docs/guidelines/express.pdf

"""
