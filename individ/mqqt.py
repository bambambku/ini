from mysecrets import hmq_mqtt_client_id, hmq_mqtt_host, hmq_user, hmq_password
from umqtt.simple import MQTTClient as MQTTReceiver
from umqtt.robust import MQTTClient as MQTTSender
from mysecrets import *
from machine import Pin
import json
from wifi import Wifi
from umqtt.robust import MQTTClient

      
mqtt_topic = "home/test"
mqtt_topic2 = "home/cleft"

mqtt_client = MQTTClient(
        client_id=hmq_mqtt_client_id,
        server=hmq_mqtt_host,
        port=8883,
        ssl=True,
        ssl_params={'server_hostname': hmq_mqtt_host},
        user=hmq_user,
        password=hmq_password)


def send(data, mqtt_topic):
    data = json.dumps(data)
    mqtt_client.publish(mqtt_topic, data)
    topic2 = "home/best"
    data2 = json.dumps({ 'message': 'ciasteczka'})
    mqtt_client.publish(topic2, data2)

# mqtt_client.disconnect()


mqtt_receiver = MQTTReceiver(
        client_id=hmq_mqtt_client_id,
        server=hmq_mqtt_host,
        port=8883,
        ssl=True,
        ssl_params={'server_hostname': hmq_mqtt_host},
        user=hmq_user,
        password=hmq_password)

def message_received(topic, response):
    print("Message received!")
    print(f"topic: {topic}")
    print(response)
    data = json.loads(response)
    print(data)
    global calories_left
    calories_left = data['calories']


def receive():
    listen = True
    print('receiving')
    while listen:
        data = mqtt_receiver.check_msg()
        if data:
            listen = False

# 
# Wifi()
# mqtt_client.connect()
# mqtt_topic = "home/test"
# mqtt_topic2 = "home/cleft"    
# mqtt_receiver.connect()
# mqtt_receiver.set_callback(message_received)
# mqtt_receiver.subscribe(mqtt_topic2)
# 
# data = {'baba': 'babalu'}
# data = json.dumps({'baba': 'babalu'})
# mqtt_client.publish(mqtt_topic, data)
# topic2 = "home/cleft"
# data2 = json.dumps({ 'message': 'ciasteczka'})
# mqtt_client.publish(topic2, data2)
#     


# send({'ciasteczka': 'ciacha'}, mqtt_topic)
# data = receive()
# print(f'data received finally: {data}')