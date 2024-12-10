const int waterSensorPin = A0;  // Analog pin for water sensor

// Starting date and time
int currentDay = 9;    
int currentMonth = 12; 
int currentYear = 2024; 
String currentDayName = "Monday"; // Starting day of the week

unsigned long prevMillis = 0;  // To track passage of time
unsigned long millisOffset = 0;  // Offset to account for Arduino reset

// Array for month lengths (non-leap year by default)
int daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

// Array for day names
String daysOfWeek[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

void setup() {
  Serial.begin(9600);  // Start Serial communication
  Serial.println("Day, Date, Time (HH:MM:SS:MS), Water Level");  // Print CSV header

  // Check if starting year is a leap year
  if (isLeapYear(currentYear)) {
    daysInMonth[1] = 29;  // Update February for leap year
  }
}

void loop() {
  unsigned long currentMillis = millis();  // Get current time since Arduino started
  unsigned long totalMillis = currentMillis + millisOffset;

  // Calculate elapsed time
  unsigned long totalSeconds = totalMillis / 1000;
  unsigned long hours = (totalSeconds / 3600) % 24;
  unsigned long minutes = (totalSeconds / 60) % 60;
  unsigned long seconds = totalSeconds % 60;
  unsigned long milliseconds = totalMillis % 1000;

  // Update the date and day if a day has passed
  if (hours == 0 && minutes == 0 && seconds == 0 && milliseconds == 0) {
    updateDate();
  }

  // Water level reading
  int waterLevel = analogRead(waterSensorPin);

  // Format the date as a string
  String date = String(currentDay) + "/" + String(currentMonth) + "/" + String(currentYear);

  // Print data to Serial Monitor
  Serial.print(currentDayName); Serial.print(", ");
  Serial.print(date); Serial.print(", ");
  Serial.print(hours); Serial.print(":");
  Serial.print(minutes); Serial.print(":");
  Serial.print(seconds); Serial.print(":");
  Serial.print(milliseconds); Serial.print(", ");
  Serial.println(waterLevel);

  delay(1000);  // Log data every second (can change to 60000 for 1 minute intervals)
}

// Function to update date and day of the week
void updateDate() {
  currentDay++;  // Move to the next day

  // Check if we need to change the month
  if (currentDay > daysInMonth[currentMonth - 1]) {
    currentDay = 1;  // Reset to first day of the next month
    currentMonth++;

    // Check if we need to change the year
    if (currentMonth > 12) {
      currentMonth = 1;  // Reset to January
      currentYear++;
      
      // Update February for the new year's leap status
      if (isLeapYear(currentYear)) {
        daysInMonth[1] = 29;
      } else {
        daysInMonth[1] = 28;
      }
    }
  }

  // Update the day of the week
  int dayIndex = (getDayIndex(currentDayName) + 1) % 7;
  currentDayName = daysOfWeek[dayIndex];
}

// Function to check if a year is a leap year
bool isLeapYear(int year) {
  return (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
}

// Function to get the index of the current day name
int getDayIndex(String day) {
  for (int i = 0; i < 7; i++) {
    if (daysOfWeek[i] == day) {
      return i;
    }
  }
  return -1;  // Error case (shouldn't happen)
}
