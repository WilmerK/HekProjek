#include <RCSwitch.h>
RCSwitch mySwitch = RCSwitch();
int relay = 6;

void setup() {
  mySwitch.enableReceive(0);
  pinMode(relay, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  if (mySwitch.available()) {
    
    int value = mySwitch.getReceivedValue();
    
    if (value == 0) {
    } else {
      Serial.println(value);
      if (value == 1647) {
        digitalWrite(relay, HIGH);
        delay(100);
        digitalWrite(relay, LOW);
        delay(100);
    }
    }
    
    mySwitch.resetAvailable();
  
  }

}
