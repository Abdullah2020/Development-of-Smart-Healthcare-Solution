//DistanceMeasured = Ultrasound Sensor
//Hum = Humidity sensor
//roomTemp = Home Temperature
//cTemp = Body Temperature Sensor
//myBPM = Pulse sensor

String getSensorData()
{
  int myBPM = getBMP();                     
  float cTemp = getBodyTemp();
  DistanceMeasured = getDistance();
  //Read data and store it to variables hum and temp (Humidity and Temperature)
  hum = dht.readHumidity();
  roomTemp = dht.readTemperature();
  lcdUpdate(DistanceMeasured, hum, roomTemp, cTemp, myBPM);

  
  String output = String(DistanceMeasured) + ";" + String(hum) + ";" + String(roomTemp) + ";" + String(cTemp) + ";" + String(myBPM);
  Serial.println(output); // # output:  DistenceMeasured;Humitity;bodyTemp;roomTemp;BMP
  Serial.println("________");
  return output;

}

int getBMP() {
  starttime = millis();
  while (millis() < starttime + 10000)               // Reading pulse sensor for 10 seconds
  {

    sensorValue = analogRead(sensorPin);
    if (sensorValue > 550 && counted == false)  // Threshold value is 550 (~ 2.7V)
    {
      count++;
      delay (50);

      counted = true;
    }
    else if (sensorValue < 550)
    {
      counted = false;
    }
  }

  heartrate = count * 6;                             // Multiply the count by 6 to get beats per minute
  count = 0;
  return heartrate;                        // Display BPM in the Serial Monitor

}

float getDistance(){
  digitalWrite(URTRIG, LOW);
  digitalWrite(URTRIG, HIGH);
  unsigned long LowLevelTime = pulseIn(URECHO, LOW) ;
  if (LowLevelTime >= 50000)              // the reading is invalid. instead of 50k
  {
    pValue = pValue - 1;
  }
  else
  {
    DistanceMeasured = LowLevelTime / 50;  // every 50us low level stands for 1cm
    pValue = lagValue;
  }
  return DistanceMeasured;
}

 
void lcdUpdate(float DistanceMeasured, float hum, float roomTemp, float cTemp, float myBPM) {
  lcd.clear();
  if (turn == 1 ) {
    lcd.setCursor(0, 0);
    lcd.print("Body Temp:" + String(cTemp));
    lcd.setCursor(0, 1);
    lcd.print("Room Temp:" + String(roomTemp));
    turn += 1;
  }
  else if (turn == 2) {
    lcd.setCursor(0, 0);
    lcd.print("hum:" + String(hum));
    lcd.setCursor(0, 1);
    lcd.print("Distance:" + String(DistanceMeasured) );

    turn += 1;
  }
  else {
    lcd.setCursor(0, 0);
    lcd.print("BPM:" + String(myBPM));
    lcd.setCursor(0, 1);
    lcd.print("Group 3");
    turn = 1;
  }
}


float getBodyTemp() {
  tempsensor.wake();   // wake up, ready to read!

  // Read and print out the temperature, then convert to *F
  float c = tempsensor.readTempC();
 
  
  tempsensor.shutdown(); // shutdown MCP9808 - power consumption ~0.1 micro Ampere

  return c;
  
  }
