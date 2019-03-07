
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int num = 0;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
}

void loop() {
  lcd.setCursor(16,0);
  while (Serial.available() > 0) {
    if(Serial.available() == 1) {
      break;
    }
    lcd.scrollDisplayLeft();
    lcd.write(Serial.read());
    delay(500);
  }
  lcd.clear();
}
