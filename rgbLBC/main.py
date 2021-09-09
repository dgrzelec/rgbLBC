from time import sleep
import numpy as np
from d3dshot.d3dshot import D3DShot
from d3dshot import _validate_capture_output

import threading

from PIL import Image
from numpy.core.fromnumeric import shape

#change downsampling func here if necessary
from color_returner import scale_down_returner_PIL as downsample_func

from serial import Serial

class rgbLBC_app(D3DShot):
    def __init__(
        self, 
        n_LEDs:int, 
        target_fps:int, 
        debug:bool = False, 
        log_func = print, 
        display_idx = 0
        ) -> None:

        co = _validate_capture_output('pil') #validating by hand instead of create() function
        super().__init__(capture_output=co, frame_buffer_size=1) #buffer_size = 1 for pop aproach
        # self.d3d_object = d3dshot.create(capture_output='pil', frame_buffer_size=1)

        self.nLEDs = n_LEDs
        self.target_fps = target_fps
        self.debug = debug
        self.log_func = log_func
        self.display_idx = display_idx
        #################################### VALIDATION 
        self.target_fps = self._validate_target_fps(self.target_fps)

        ####################################
        self.shape = (2,self.nLEDs)
        self.rgb_vals_array = np.zeros(self.shape, dtype=np.uint8)
        self.rgb_vector = np.zeros(2*self.nLEDs, dtype=np.uint8)

        ############################### displays
        self.__log("Displays available:")
        for i,display in enumerate(self.displays):
            self.__log("[{}]".format(i)+str(display))
        self.__log("Choosing display index [{}]".format(self.display_idx))
        self.set_display(self.display_idx)
        ################################

        self._is_running = False
        self._rgb_thread = None
        self._is_serial_set = False

    @property
    def is_running(self)->bool:
        return self._is_running

    @property
    def is_frame_ready(self)->bool:
        return bool(self.frame_buffer)

    @property
    def is_serial_set(self):
        return self._is_serial_set

    def get_current_rgb(self)->np.ndarray:
        return self.rgb_vector

    def pop_latest_frame(self)->Image:
        return self.frame_buffer.popleft()

    def setup_serial(self, port:str, baudrate:int):
        self.ser = Serial(port, baudrate)
        self._is_serial_set = True

    def __log(self,msg:str, kind:str = 'INFO'):
        """log function to use inside a class; defined by 'log_func' init parameter

        Args:
            msg (str): your message
            kind (str, optional): what kind of log message it is.  Defaults to 'INFO'.
        """
        self.log_func(kind+': '+msg)
    
    def set_display(self,index:int)->None:
        try:
            self.display = self.displays[index]
            self.__log("Display set to: " + "[{}]".format(index)+str(self.display))
        except IndexError:
            self.__log("No display with index [{}] detected".format(index), "WARNING")
            self.display = self.displays[0]
            self.__log("Display set to: " + "[{}]".format(0)+str(self.display))
        

    def start(self):
        if self.is_running:
            return False

        self._is_running = True

        self.capture(self.target_fps)

        self._rgb_thread = threading.Thread(target=self._start)
        self._rgb_thread.start()

        return True
    
    def stop(self):
        if self._is_capturing:
            super().stop()

        if self._is_running:
            self._is_running = False
            self._rgb_thread.join(timeout=1)
            self._rgb_thread = None

        if self.is_serial_set:
            self.ser.close

        self.__log("app stopped properly")

    def send(self):
        if self.is_serial_set:
            for i in range(2*self.nLEDs):
                self.__send_to_COM(self.ser, bytearray(self.rgb_vector[i,:]))
            if self.debug:
                print(self.rgb_vector[0,:].shape)

        else: raise RuntimeError("Serial connection is not set, us setup_serial() method") 

    def __generate_rgb(self):
        """Generates and stores downsampled screenshot and RGB values vector, ready to be send through COM.
        There should be frame in a frame buffer
        """
        self.rgb_vals_array = downsample_func(self.pop_latest_frame(), self.shape) 
        
        #converting to vector of RGB values, assuming lower left starting point
        self.rgb_vector = self.rgb_vals_array.reshape((2*self.nLEDs,1,3), order='F')
        self.rgb_vector[0:self.nLEDs,0,:] = self.rgb_vector[self.nLEDs-1::-1,0,:]
        self.rgb_vector = np.squeeze(self.rgb_vector)

    def __send_to_COM(self, ser: Serial, data:bytearray):
        ser.write(data)
    
    def _start(self):
        while self.is_running:
            if self.is_frame_ready:
                self.__generate_rgb()
                self.send()
            sleep(0.001)


if __name__ == "__main__":
    from exit_handler import set_exit_handler
    from serial_utilities import waitForArduino

    print("enter main")


    app = rgbLBC_app(30,40, debug=True)
    def stop_helper(sig, func=None):
        app.stop()

    set_exit_handler(stop_helper)
    
    app.setup_serial("COM3", 115200)
    waitForArduino(app.ser)

    app.start()

    sleep(0.05)
    
    app.stop()