from sense_hat import SenseHat
import time
import calendar
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish




Broker = "192.168.**.**"              #Enter your broker IP Address

sub_topic = "sensor/instructions"    # receive messages on this TOPIC
output = ""


def on_connect(client, userdata, flags, rc):
    client.subscribe("arduino/data")



def on_message(client, userdata, msg):
    message = msg.payload
    topic = msg.topic
    print(topic)
    print(message.decode("utf-8"))
    if topic == "arduino/data":
        output = str(calendar.timegm(time.gmtime())) + "000" + ";" + message.decode("utf-8") # output:  Timestamp;DistenceMeasured;Humitity;bodyTemp;roomTemp;puls
        print(output)
        lst = output.split(";")
        print(lst)
        client.publish("pi/upload", output)
        




def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1888, 60)
client.loop_start()


while True:
    time.sleep(5)

##Reference
### Python code: https://stackoverflow.com/questions/37006863/python-mqtt-script-on-raspberry-pi-to-send-and-receive-messages
