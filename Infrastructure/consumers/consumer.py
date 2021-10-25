from kafka import KafkaConsumer
from json import loads
import logging
import psycopg2


"""

KAFKA CONSUMER FOR POSTGRESQL

To deliver data to the our database, we build this service to get messages from the producer
this must be deployed to a container that receives and translates KAFKA messages 


"""

# We create the consumer that it is going to fetch messages from the KAFKA topic of our interest

consumer = KafkaConsumer(
    'blood',
    bootstrap_servers=['172.17.0.1:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))  # Messages need to be decoded before processing the info

# This function inserts the data that comes from the topic, it takes two values for Systolic and Diastolic data
# as this moment we did not use any other value to be inserted.


def insert_ast(sys, dys):

    # DB settings to create a connection object

    db = psycopg2.connect(user="postgres",
                          password="Xoco_137946",
                          host="172.17.0.1",
                          port="5432",
                          database="ssd_iss")

    """ insert astronaut data into table """
    sql = """INSERT INTO authentication_astronauthealthreport(weight, blood_type, blood_pressure, heart_rate, muscle_mass, astronaut_id)
             VALUES(%s, %s, %s, %s, %s, %s);
    """

    # This variables are part of the data that could be fetched from any IoT device
    # We did a simulator for two values for this test

    weight = '155'
    blood_type = 'B'
    blood_pressure = str(sys)
    heart_rate = str(dys)
    muscle_mass = '34'
    astronaut_id = '1'

    conn = None
    vendor_id = None
    try:
        # create a new cursor
        cur = db.cursor()
        # get the generated id back
        #id = cur.fetchone()[0]

        # execute the INSERT statement
        cur.execute(sql, (weight, blood_type, blood_pressure,
                    heart_rate, muscle_mass, astronaut_id,))

        # commit the changes to the database
        db.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        curs = db.cursor()
        curs.execute("ROLLBACK")
        db.commit()  # Rollback is needed if the query returned an error
        # Log the issue that prevented data to be saved, and then try again. This helps achieve OWASP A10 because visibility is provided.
        logging.error("Failed to insert entry into database, cause %s", error)
    finally:
        if db is not None:
            db.close()  # After insert is done connection is closed
