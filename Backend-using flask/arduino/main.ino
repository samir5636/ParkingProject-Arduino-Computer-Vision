#include <LiquidCrystal.h>
#include <Servo.h>
#define ledRed 6
#define ledBlue 5
#define ledGreen 4
#define pirPin 3
#define servoPin 13

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);
Servo myServo;
void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  myServo.attach(servoPin);
  pinMode(ledRed, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledBlue, OUTPUT); // Added missing pinMode for Blue LED
  pinMode(pirPin, INPUT);
  digitalWrite(ledBlue, LOW);
  digitalWrite(ledRed, HIGH);
  digitalWrite(ledGreen, LOW);
  myServo.write(90);
}

void loop() {
  if (Serial.available()) {
    // Read the value from the serial port
    char receiveChar = Serial.read();
    lcd.setCursor(0, 1);
    lcd.clear();
    if (receiveChar == 'O' || receiveChar == 'o') {//O:Welcome   , o:See you later
      digitalWrite(ledBlue, HIGH);
      digitalWrite(ledRed, LOW);
      digitalWrite(ledGreen, LOW);
      myServo.write(180);
      //String fullname = Serial.readStringUntil('\n');//full name of user
      if(receiveChar == 'o'){
        lcd.print("See you later !!");
      }else if(receiveChar == 'O'){
        lcd.print("Welcome !!");
      }
      delay(3000);
    } else if (receiveChar == 'C' ) {
      digitalWrite(ledBlue, LOW);
      digitalWrite(ledRed, HIGH);
      digitalWrite(ledGreen, LOW);
      myServo.write(90);
      lcd.print("I am a Smart parking");
      delay(3000);
    }else if(receiveChar == 'n'){
      lcd.print("You are not a client");
      delay(1000);
    }else if(receiveChar == 's'){
      lcd.print("You sold is insuffisant");
      delay(1000);
    }
  }
}
