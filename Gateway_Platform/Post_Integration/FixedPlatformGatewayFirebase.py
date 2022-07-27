import pyrebase
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from datetime import datetime
import time
import calendar


""" Data & Alerts """

datafield_names = ["DateTime", "Distance", "Humidity", \
               "RoomTemp", "BodyTemp", "HeartRate"]
alertfield_names = ["OutOfBedAlert", "HumidityAlert", \
               "RoomTempAlert", "BodyTempAlert", "HeartRateAlert"]


""" Firebse database config values """

db_config = {
    "apiKey": "***************************************",                                            #Enter your Firebase API-KEY
    "authDomain": "****************.firebaseapp.com",                                               #Enter your project authentication domain
    "databaseURL": "https://******************************************.firebasedatabase.app",       #Enter your project database URL
    "projectId": "****************",                                                                #Enter your project unique ID
    "storageBucket": "****************.appspot.com",                                                #Enter your Storage Bucket ID
    "messagingSenderId": "************",                                                            #Enter Messaging Sending ID
    "appId": "*:************:web:**********************"                                            #Enter API ID
    

};


""" MQTT config values """

broker = "192.168.**.**" # Enter broker IP Address
port = **** # Enter port number eg 1888
topic = "arduino/data"        #Enter your broker TOPIC 




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
        
        # Add timestamp in seconds
        message = str(curr_unixtime) + ";" + message_in
        
        data = message.split(";")
        #print(data)

        # Send sensor data and timestamp to
        # Firebase Realtime database (one at a time)
        for i in range(6):
            database.child(datafield_names[i])
            output = {"key1": data[i]}
            database.set(output)

        alerts = [0 for i in range(5)] # clear alert status
        
        # Set alert if patient is out of bed
        if int(data[1]) > 50: # int
            alerts[0] = 1
        # Set alert if room humidity is too high or low
        if float(data[2]) < 40: # float
            alerts[1] = -1
        elif float(data[2]) > 60:
            alerts[1] = 1
        # Set alert if patient body temperature is too high or low
        if float(data[3]) < 35.5: # float
            alerts[2] = -1
        elif float(data[3]) > 37.5:
            alerts[2] = 1
        # Set alert if room temperature is too high or low
        if float(data[4]) < 18: # float
            alerts[3] = -1
        elif float(data[4]) > 26:
            alerts[3] = 1
        # Set alert if patient heart beat is too high or low
        if int(data[5]) < 60: # int
            alerts[4] = -1
        elif int(data[5]) > 100:
            alerts[4] = 1

        # Send alert status to Firebase Realtime database (one at a time)
        for i in range(5):
            database.child(alertfield_names[i])
            output = {"key1": alerts[i]}
            database.set(output)


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
            time.sleep(1)
            
    # Exit script on ^C
    except KeyboardInterrupt:
        print("\nExit with ^C")
        PiClient.disconnect()
        PiClient.loop_stop()
        pass
  



if __name__ == "__main__":        

    firebase = pyrebase.initialize_app(db_config)
    storage = firebase.storage()
    database = firebase.database()

    PiClient = mqtt.Client()
    PiClient.on_connect = on_connect
    PiClient.on_disconnect = on_disconnect
    PiClient.on_message = on_message
    PiClient.on_publish = on_publish
    
    main()





