#include <FastLED.h>

#define LED_PIN 5 //data pin
#define nLEDs 60

// buffers
byte R[nLEDs] = {0};
byte G[nLEDs] = {0};
byte B[nLEDs] = {0};

//fastLED array
CRGB LED_vals[nLEDs] = {0};

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  while(!Serial){ };
  //pins
  pinMode(LED_PIN, OUTPUT);
  //fastLED shit here

  //ready message
  Serial.println("<Arduino is ready>");
}

void loop() {
  if(Serial.available() >= nLEDs){
    Serial.readBytes(R,nLEDs);

  Serial.print("<red passed");
  Serial.print("  Last value: ");
  Serial.print(R[nLEDs-1]);
  Serial.println(">");
  }


}
