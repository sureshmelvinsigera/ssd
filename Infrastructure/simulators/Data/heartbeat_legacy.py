import pandas as pd
import random
import logging
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

producer = KafkaProducer(bootstrap_servers=[
                         '172.17.0.1:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

# We found heartrate data CSV taht has data from an actual IoT device, we DO NOT stream this data, we just use it as reference to make our simualation

heartrate = pd.read_csv('ring_data.csv', header=None)

# From the data source we selected 0.25 and 0.75 quantile values to stream the simulation between the boundaries of a regular blood pressure
# For a lowe pressure individual MIN and 0.25 quantiles could be selected, on the opposite, 0.75 quantile and MAX values could be selected.
# It would need more data to refine our simulator to be close to what a real person would produce in terms of data.

b = heartrate[0].quantile(0.25)
a = heartrate[0].quantile(0.75)


# This last part stream the data to the Kafka topic, right now it is on its simplest form, but can be expanded to STOP and START with different commands


for x in range(1000):
    e = round(random.uniform(a, b), 2)
    data = {'rate': e}  # The data to be sent
    try:
        # Sends the data to the selected topic, in this case bloodp
        producer.send('blood', value=data)
    except:
        # Log the issue that prevented data to be saved, and then try again. This helps achieve OWASP A10 because visibility is provided.
        # The only exception that can be raised by producer.send() is a KafkaTimeoutError, making it possible to output one log message.
        logging.error(
            "A timeout has occurred sending the data, attempted to send data for astronaut_id %s", data["astronaut_id"])
        continue
    sleep(900)  # The producer waits 15 minutes to stream new data, this value is expressed in seconds, in this case 900 seconds
