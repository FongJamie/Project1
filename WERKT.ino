// Basic Bluetooth sketch HC-05_AT_MODE_01
// Communicate with a HC-05 using the serial monitor
//
// The HC-05 defaults to communication mode when first powered on you will need to manually enter AT mode
// The default baud rate for AT mode is 38400
// See www.martyncurrey.com for details
//
 
 
#include <SoftwareSerial.h>
SoftwareSerial BTserial(2, 3); // RX | TX
// Connect the HC-05 TX to Arduino pin 2 RX. 
// Connect the HC-05 RX to Arduino pin 3 TX through a voltage divider.
// 
 
char c = ' ';

int knop = 4;
int ledRood = 5;
int ledGroen = 6;
int ledGeel = 7;

bool isKnopGedrukt = false;
bool isKnopGedruktVorig;  //nodig voor de flankdetectie
bool isLedAan;

int bijhoudenKnop = 0;

void setup() 
{
    Serial.begin(9600);
    Serial.println("Arduino is ready");
    Serial.println("Remember to select Both NL & CR in the serial monitor");
 
    // HC-05 default serial speed for AT mode is 38400
    BTserial.begin(9600);  
    
    pinMode(ledRood, OUTPUT);
    pinMode(ledGroen, OUTPUT);
    pinMode(knop, INPUT_PULLUP);
}
 
void loop()
{
 
    // Keep reading from HC-05 and send to Arduino Serial Monitor
    if (BTserial.available())
    {  
        c = BTserial.read();
        Serial.write(c);
    }


    // Keep reading from Arduino Serial Monitor and send to HC-05
    if (Serial.available())
    {
      c =  Serial.read();
      BTserial.write(c);  
    }


  isKnopGedrukt = digitalRead(knop);
  if(isKnopGedrukt!=isKnopGedruktVorig && isKnopGedrukt ==false){
    //Serial.print(">");   
    
    BTserial.write("k");
    BTserial.write(10);
    //Serial.println("k");  
    bijhoudenKnop = bijhoudenKnop + 1;

    Serial.print(bijhoudenKnop);
    if (bijhoudenKnop >= 5){
      digitalWrite(ledGroen, HIGH);
      delay(5000);
      digitalWrite(ledGroen, LOW);
      }

//    else if(bijhoudenKnop == 4){
//      digitalWrite(ledGeel, HIGH);
//      delay(5000);
//      digitalWrite(ledGeel, LOW);
//      }
    else{
      digitalWrite(ledRood, HIGH);
      delay(5000);
      digitalWrite(ledRood, LOW);
      }
    
   } 
    isKnopGedruktVorig=isKnopGedrukt;
  delay(100);

}
 
void stuurKarakter(char karakter){
    // Keep reading from Arduino Serial Monitor and send to HC-05
    BTserial.write(karakter + '^J');  
}

