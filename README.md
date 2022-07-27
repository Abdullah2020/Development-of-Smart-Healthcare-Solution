# Development-of-Smart-Healthcare-Solution
This project uses full-fledged Internet of Thing (IoT) architecture to help collect important health data of elderly under care for optimal monitoring and care in the healthcare environment.

Contributors: This project was carried out by seven(7) ISEP Students (4 Masters students and 3 exchange students), they are as follows;

		1- Abdullah Isa AHMED
		2- EBO Ife Olalekan
		3- Jean-François ALBERTINI 
		4- Aneesh Yadav
		5- Kelly YEOH KAILI
		6- Shi Song PANG
		7- Arthur W. S. Kristiansen


Introduction:

Over the years, life expectancy has increased with accelerated aging of the population, which has called for increased attention. Elder care and medical issues are becoming a major social issue in the world. Years ago, the best option for elderly people care was to assign a nursing officer to look after them on a regular basis, debarring them from attending to other patients, which can be very routine and tedious. However, the advancement in technology and the advent of smart technologies has introduced devices and methodologies that have made life easier, such as the sensors, actuators, etc. 
Consequently, the advancement in the development of these digital devices has brought about advances in wearables, smart phones, and medical sensors (blood glucometer, oximeter, blood pressure, electrocardiogram sensor (ECG), etc.) which enables real-time collection of large amounts of health data for immediate processing and effective and efficient decision making. 


Project Use Case:

In this project, the target audience is the elderly patients, and our target location is the hospital wards. Nowadays, hospitals are short of healthcare workers especially because many staff are infected with Covid-19 and extra resources are directed at ameliorating the pandemic. In addition, the world is also troubled by an aging population with more than 1 billion people in the world being elderly. 

![image](https://user-images.githubusercontent.com/16369782/181297172-264bd5d8-f799-429a-8ee2-8ad38453df78.png)
            
                                                      
As shown in the figure above. The sensors will be placed beside the patient’s bed, this can reduce the number of nurses required to do manual work because they serve as an extra 'caretaker' to ensure the elderly's basic well-being. It is important to monitor the elderly because they are weaker and more vulnerable to complications as compared to youth. Moreover, medical professionals can monitor the vitals, predict the patient’s health by studying trends and thus provide timely aid.


For patients who should stay in bed or can only get out of bed with assistance from the nurses, the ultrasonic sensor raises an alert to the nurses when the elderly patient attempts to move out and is more than 50cm away from the bed. Using the Pulse sensor, we can detect irregularities to monitor if the heart is functioning well. An alert is raised if the heart rate is outside the range of 60-100 beats per minute. For the temperature & humidity sensor, it can be used to ensure that the patient’s room is at a comfortable temperature and at of appropriate dryness. An alert is raised if the room temperature is outside the range of 18 - 26 degree Celsius or if the humidity is outside the range of 40-60%. This is important because the 4 seasons may cause the room conditions to be unfavorable for the elderly who could be more sensitive and scared of the cold. The high accuracy temperature sensor measures and records body temperature for the patients. An alert is raised if the body temperature is outside the range of 35.5-37.5 degree Celsius.

System Architecture:

This system is a fixed platform divided into three main parts as shown in the figure below:
![image](https://user-images.githubusercontent.com/16369782/181297343-fcc48326-083d-451b-b19f-ea79620c62ef.png)


The first part consists of four sensors (body temperature sensor, home temperature and humidity sensor, pulse sensor, and ultrasound sensor) with the aim of collecting data through them. These sensors are connected to the microcontroller (Arduino Uno Wi-Fi Rev 2.0 board), which processes them and displays the processed data on the liquid crystal display (LCD). Furthermore, these data are sent to the gateway (Raspberry Pi) via the Wi-Fi by the microcontroller. 

The second part consists of the Gateway. The gateway works as the mediator between the Arduino units (first part) and the visualization (third part). A Raspberry Pi is used as both a Message Queuing Telemetry Transport (MQTT) broker and a client responsible for receiving data from the Arduino and sending it to the visualization services. 

The third part of the architecture is the visualization. The data are presented in the form of charts, timelines, and maps, that make it easy to see and understand patterns and unusual readings for urgent attention by the caretakers.

![image](https://user-images.githubusercontent.com/16369782/181298953-d3e3dd6a-9a72-4124-af0c-b0409c4fba8a.png)


Final Result:

This project implemented a full-fledged IoT connected system that aimed as collecting information from the sensors layer and send it gateway (represented by the raspberry pi). The platform allow the smart hospital users to check their vital signs (pulse, temperature) and other ambient values such as temperature and humidity. Some functionalities may raise alerts (sensors threshold exceeded for instance) at the visualisation level. Below figure shows the final integrated systems.

![Sensors and Gateway](https://user-images.githubusercontent.com/16369782/181306941-789c75f5-9005-44d3-bb1e-ce8bf1d4b529.png)

![Integrated Visualisation Platform](https://user-images.githubusercontent.com/16369782/181307027-abe8875f-30cd-470c-82d7-39c2021d3f8d.png)


Conclusion:

Finally, the overall system was a success as the complete system was able to provide the required information from the sensor layer down to the visualisation platform, The system ability to send real-time information of all accesses by an elderly patient proves that the system can perform the required function of smart healthcare. The system which is invariably a model for future expansion can be provided with other features for robustness and more functionality enhancement. Features such as high-level security, Artificial Intelligent (AI) model for prediction and Portable mobile application software to enhance accessibility.
