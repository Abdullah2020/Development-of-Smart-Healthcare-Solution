#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>
#include <DFRobot_Heartrate.h>
#include "Adafruit_MCP9808.h"
#include <Wire.h>
#include <DHT.h> // Including library for dht
#include <LiquidCrystal.h>
#include <PulseSensorPlayground.h>


char ssid[] = "*****";       // Enter your network SSID (name)
char pass[] = "********";    // Enter your network password (use for WPA, or use as key for WEP)
 
WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

// declearing broker info
const char broker[] = "192.168.**.**";       //Enter your broker IP Address
int        port     = ****;                 // Enter broker port number e.g 1888

// declearing varibels
String msg;


// var for sensors
#define DHTPIN 8

int sensorPin = A1;                                // A1 is the input pin for the heart rate sensor
float sensorValue = 0;                             // Variable to store the value coming from the sensor
int count = 9;
unsigned long starttime = 0;
int heartrate = 0;
boolean counted = false;
int waitTime = 15000;
unsigned long lastRun = 0;
int turn = 1;


#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value
float roomTemp;

const int PulseWire = 0;       // connected to ANALOG PIN 0
int Threshold = 550;

PulseSensorPlayground pulseSensor;
long timeInit = 0; //min

// MCP9808 I2C address is 0x18(24)
#define Addr 0x18
int URECHO = 10;         // PWM Output 0-50000US,Every 50US represent 1cm
int URTRIG = 6;         // trigger pin
unsigned int DistanceMeasured = 0;
int delayTime = 3000;   //every 3seconds the sensor will give an output
int lagValue = 15;      // the output will be vqlid for 45seconds before another reading
int pValue = 0;


// Create the MCP9808 temperature sensor object
Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();

// LCD
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


void setup() {
  
  lcd.begin(16, 2);
  lcd.print("Setting up");
  
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the Network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();

  // setup sensors
  pulseSensor.analogInput(PulseWire);
  pulseSensor.setThreshold(Threshold);


  // Initialise I2C communication as MASTER
  Wire.begin();
  dht.begin();

  pinMode(URTRIG, OUTPUT);                   // A low pull on pin COMP/TRIG
  // pinMode(ledPin, OUTPUT);                   // A low pull on pin COMP/TRIG
  digitalWrite(URTRIG, HIGH);                // Set to HIGH
  pinMode(URECHO, INPUT);                    // Sending Enable PWM mode command
  // delay(500);
  Serial.println("Init the sensor");


  
if (!tempsensor.begin()) {
    Serial.println("Couldn't find MCP9808!");
    while (1);
  }

}

void loop() {
  mqttClient.poll();
  if ((millis() - lastRun) >= waitTime) {
    lastRun = millis();
    mqttClient.beginMessage("arduino/data");
    mqttClient.print(getSensorData());
    mqttClient.endMessage();
  }
  delay(500);

}
