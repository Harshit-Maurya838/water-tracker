const int waterSensorPin = A0;  // Analog pin for water sensor

// Starting date and time
const int startDay = 9;  
const int startMonth = 12;  
const int startYear = 2024;  

unsigned long prevMillis = 0;  // To track the passage of time
unsigned long millisOffset = 0;  // Offset to adjust for Arduino reset

void setup() {
  Serial.begin(9600);  // Start Serial communication
  Serial.println("Day, Date, Time (HH:MM:SS:MS), Water Level");  // Print CSV header
}

void loop() {
  unsigned long currentMillis = millis();  // Get the current time since the Arduino started

  // Calculate elapsed time since the program started
  unsigned long totalMillis = currentMillis + millisOffset;
  unsigned long totalSeconds = totalMillis / 1000;
  unsigned long hours = (totalSeconds / 3600) % 24;
  unsigned long minutes = (totalSeconds / 60) % 60;
  unsigned long seconds = totalSeconds % 60;
  unsigned long milliseconds = totalMillis % 1000;

  // Water level reading
  int waterLevel = analogRead(waterSensorPin);

  // Format the day and date
  String dayName = "Monday";  // Start with Monday for 09/12/24 
  String date = String(startDay) + "/" + String(startMonth) + "/" + String(startYear);


  Serial.print(dayName); Serial.print(", ");
  Serial.print(date); Serial.print(", ");
  Serial.print(hours); Serial.print(":");
  Serial.print(minutes); Serial.print(":");
  Serial.print(seconds); Serial.print(":");
  Serial.print(milliseconds); Serial.print(", ");
  Serial.println(waterLevel);

  delay(60000);  // Log data every 60 seconds
}
