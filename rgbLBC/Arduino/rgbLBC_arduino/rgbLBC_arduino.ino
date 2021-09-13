#include <FastLED.h>

#define BRIGHTNESS_PIN A5
#define MAX_BRIGHTNESS 255
#define LED_PIN 5 //data pin
#define nLEDs 60

// // buffers
// byte R[nLEDs] = {0};
// byte G[nLEDs] = {0};
// byte B[nLEDs] = {0};

//fastLED array
CRGB LED_vals[nLEDs] = {0};
//buffer
uint8_t crgb_buffer[3] = {0};

bool receiving_complete = false;
int analog_input = 0;

// funtions
void blinkLED(int pinLED = LED_BUILTIN){
  static bool led_state = 0;
  led_state = !led_state;
  digitalWrite(pinLED, led_state);
}



void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  // cleaning serial
  while(!Serial){ };
  //pins
  pinMode(LED_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(BRIGHTNESS_PIN, INPUT);

  //fastLED shit here
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(LED_vals,nLEDs); // add LED strip to FastLED; probably GRB but not sure
  // FastLED.setBrightness(100);

  //ready message
  Serial.println("<Arduino is ready>");
}

void loop() {

  static int index = 0;
  
  // brightness from analog pin
  analog_input = analogRead(BRIGHTNESS_PIN);
  FastLED.setBrightness(map(analog_input, 0, 1023, 0, 255)); 

  if(Serial.available() >= 3){
    Serial.readBytes(crgb_buffer, 3); // reading into buffer
    LED_vals[index++].setRGB(crgb_buffer[0],crgb_buffer[1],crgb_buffer[2]); // setting the next LED to received rgb vals

    if(index == nLEDs){
      index = 0;
      receiving_complete = true;
      }
  }

  if(receiving_complete){
      blinkLED();
      FastLED.show();
      receiving_complete = false;
  }

}
