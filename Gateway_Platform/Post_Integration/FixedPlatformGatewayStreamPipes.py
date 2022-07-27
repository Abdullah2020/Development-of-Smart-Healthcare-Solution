import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from datetime import datetime
import time
import calendar


""" Data & Alerts """

datafield_names = ["DateTime", "Distance", "Humidity", \
               "RoomTemp", "BodyTemp", "HeartRate"]


""" MQTT config values """

broker = "192.168.***.***" #Enter broker IP Address
port = ****                #Enter broker port number eg 1888
topic = "arduino/data"     #Enter your broker TOPIC




""" Pi MQTT Broker methods setup """

# When connected to MQTT Broker
def on_connect(client, userdata, flags, rc):
    print("Connected to broker at {} port {}".format(broker, port))
    client.subscribe(topic)
    print("Subscribed to:", topic)

# When disconnected from MQTT Broker
def on_disconnect(client, userdata, rc):
    if rc == 0:
        print("Disconnected from broker at {} port {}".format(broker, port))
    else:
        print("Unexpected disconnection.")


# When receiving an MQTT message
def on_message(client, userdata, msg):
    message_in = msg.payload.decode("utf-8")
    topic = msg.topic

    # Only run if the message is data from the fixed platform
    if topic == "arduino/data":
        
        curr_unixtime = calendar.timegm(time.gmtime())
        curr_time = datetime.fromtimestamp(curr_unixtime)\
                    .strftime("%Y-%m-%d %H:%M:%S")
        print("Data received on topic '{}' at {}:".format(msg.topic, curr_time))
        print(message_in)
        
        # Add timestamp in milliseconds, since StreamPipes uses milliseconds
        message_out = str(curr_unixtime) + "000" + ";" + message_in

        # Send timestamp, sensor data, alerts to Streampipes
        client.publish("pi/upload", message_out)


# When publishing an MQTT message
def on_publish(client, userdata, mid):
    print('Data published to broker with mid {}'.format(mid))       




""" Execution """

def main():    
    try:
        # Connect to Pi MQTT Broker
        PiClient.connect(broker, port, 60)
        PiClient.loop_start()

        # Keep the broker running
        while True:
            time.sleep(5)
            
    # Exit script on ^C
    except KeyboardInterrupt:
        print("\nExit with ^C")
        PiClient.disconnect()
        PiClient.loop_stop()
        pass
  



if __name__ == "__main__":        
    PiClient = mqtt.Client()
    PiClient.on_connect = on_connect
    PiClient.on_disconnect = on_disconnect
    PiClient.on_message = on_message
    PiClient.on_publish = on_publish
    
    main()





