# rgb Led Background Controller

### What is it about
Imagine RGB LED strips at the sides of your TV, which reacts on whats happening in your favourite video game or film - this is what this project is trying to accomplish.

The idea is to capture screen and convert (downsample) captured image to Nx2 array of rgb data, where N is number of LEDs at each side of screen.
Next its going to be send over COM port to Arduino or similar microcontroller, which will handle addressable RGB strip. 

### Basic usage

- Create the rgbLBC object, passing number of LEDs and FPS you want to achieve. **IMPORTANT:** LED number should be the SIDE number of LEDs.

- If you want to send data via serial port you should use `setup_serial()` method and pass serial port name and baud rate.

**INFO:** Current version of the Arduino code sends "\<Arduino is ready\>" string when it is ready to handle incoming data, so you should handle waiting for that signal or: `from rgbLBC.serial_utilities import waitForArduino`
 
- Finally use `self.start()` method to start capturing the screen (and sending rgb data through serial)
- `self.stop()` should be used to properly stop capturing and close serial connection 

### What is done
- using fast screenshot capturing library [d3dshot](https://pypi.org/project/d3dshot/#description)
- downsampling using [PIL.Image.resize()](https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=resize#PIL.Image.Image.resize) with Image.BOX resampling algorithm
- class iherits now directly from D3DShot; easier access to methods and attributes, while maintaining singleton of parent class
- base class functionalities
- threaded start() method 
- serial communication - sending RGB values through serial port  
- Arduino code - receiving values
- Arduino code - FastLED part - setting up LEDs with received data

### To do
- timing - is current code fast enough to achieve at least 25 FPS?
- package files: setup.py etc

### Requirements
As for now, d3dshot needs pillow version 7 to work, and latter does not support newest Python, so this project is coded under Python 3.7

### Future
- GUI 
