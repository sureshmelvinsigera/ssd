# KAFKA/ZOOKEEPER microservices

## INTRODUCTION

As part of our tests, we created different microservices that were needed to recreate our
system design, we created a KAFKA installation alongside with a ZOOKEEPER. 

## KAFKA

The main KAFKA container, it needs an ENV VARIABLE to advertise its IP, 
later we would need it to connect other services to it

```
docker run -d \
--name kafka \
-p 7203:7203 \
-p 9092:9092 \
-e KAFKA_ADVERTISED_HOST_NAME=${KAFKA_IP} \
-e ZOOKEEPER_IP=${ZOO_IP} \
ches/kafka

```

## ZOOKEEPER

First we ran our ZOOKEEPER container, this service is needed to keep track of the KAFKA
nodes and topics and other services within the brocker. Also, it allows user to make
production and consuming simultaneously.

```
docker run -d \
--name zookeeper \
-p 2181:2181 \
jplock/zookeeper

```

## CREATING OUR MAIN TOPIC

All our data, in this case for systolic and diastolic information, will go to a topic called `blood`
Producers and Consumers will stream and receive data from a single partition

docker run \
--rm ches/kafka kafka-topics.sh \
--create \
--topic blood \
--replication-factor 1 \
--partitions 1 \
--zookeeper ${ZOO_IP}:2181