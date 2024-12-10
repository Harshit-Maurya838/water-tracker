const int waterSensorPin = A0;  // Analog pin for water sensor

void setup() {
  Serial.begin(9600);  
  Serial.println("Time (Seconds), Water Level");  //  CSV header
}

void loop() {
  // Read water level
  int waterInml = analogRead(waterSensorPin);
  int waterLevel = waterInml / 1;

  // Get time in seconds
  unsigned long currentTime = millis() / 1000;

  // Print data to Monitor
  Serial.print(currentTime);
  Serial.print(", ");
  Serial.println(waterLevel);

  delay(1000);  // Log data every 1 seconds
}
