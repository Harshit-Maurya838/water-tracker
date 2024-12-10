#include <Wire.h>
#include <RTClib.h>  

RTC_DS3231 rtc;  

const int waterLevelPin = A0; 
int waterLevel;  
String dateTime; 

void setup() {
  Serial.begin(9600);  

  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));  

  Serial.println("Date,Time,Water Level");
}

void loop() {
  waterLevel = analogRead(waterLevelPin);

  DateTime now = rtc.now();
  
  dateTime = String(now.year()) + "/" + String(now.month()) + "/" + String(now.day()) + ","
           + String(now.hour()) + ":" + String(now.minute()) + ":" + String(now.second());

  Serial.print(dateTime);  
  Serial.print(",");
  Serial.println(waterLevel); 


  delay(1000);
}
