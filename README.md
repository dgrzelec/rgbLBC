# rgb Led Background Controller

### What is it about
Imagine RGB LED strips at the sides of your TV, which reacts on whats happening in your favourite video game or film - this is what this project is trying to accomplish.

The idea is to capture screen and convert (downsample) captured image to Nx2 array of rgb data, where N is number of LEDs at each side of screen.
Next its going to be send over COM port to Arduino or similar microcontroller, which will handle addressable RGB strip. 

### What is done
- fast screenshot capturing library [d3dshot](https://pypi.org/project/d3dshot/#description)
- downsampling using [PIL.Image.resize()](https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=resize#PIL.Image.Image.resize) with Image.BOX resampling algorithm

### To do
- base class functionalities for console interface
- threaded start() method 
- COM communication (sending RGB values)
- Arduino code - (FastLED?)

### Requirements
As for now, d3dshot needs pillow version 7 to work, and latter does not support newest Python, so this project is coded under Python 3.7

### Future
- GUI 
