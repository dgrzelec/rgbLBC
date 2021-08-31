from time import sleep
import numpy as np
import d3dshot

from PIL import Image
#change downsampling func here if necessary
from color_returner import scale_down_returner_PIL as downsample_func

from exit_handler import set_exit_handler


class rgbLBC_app:
    def __init__(
        self, 
        n_LEDs:int, 
        target_fps:int, 
        debug:bool = False, 
        log_func = print, 
        display = 0
        ) -> None:

        self.nLEDs = n_LEDs
        self.target_fps = target_fps
        self.debug = debug
        self.log_func = log_func
        self.display = display

        self.shape = (2,self.nLEDs)

        #initializations
        set_exit_handler(self.stop) #
        self.d3d_object = d3dshot.create(capture_output='pil', frame_buffer_size=1)

        ############################### displays
        self.__log("Displays available:")
        for i,display in enumerate(self.d3d_object.displays):
            self.__log("[{}]".format(i)+str(display))
        self.__log("Choosing display index [{}]".format(self.display))
        self.set_display(self.display)
        ################################

        self._is_running = False
    
    @property
    def is_running(self):
        return self._is_running

    @property
    def is_frame_ready(self):
        return bool(self.d3d_object.frame_buffer)

    def __generate_rgb(self):
        self.rgb_vals_array = downsample_func(self.d3d_object.get_latest_frame(), self.shape) 

    def __send_to_COM():
        pass

    def __log(self,msg:str, kind:str = 'INFO'):
        """log function to use inside a class; defined by 'log_func' init parameter

        Args:
            msg (str): your message
            kind (str, optional): what kind of log message it is.  Defaults to 'INFO'.
        """
        self.log_func(kind+': '+msg)
    
    def set_display(self,index:int)->None:
        try:
            self.d3d_object.display = self.d3d_object.displays[index]
            self.__log("Display set to: " + "[{}]".format(index)+str(self.d3d_object.display))
        except IndexError:
            self.__log("No display with index [{}] detected".format(index), "WARNING")
            self.d3d_object.display = self.d3d_object.displays[0]
            self.__log("Display set to: " + "[{}]".format(0)+str(self.d3d_object.display))
        

    def start(self):
        pass
    
    def stop(self):
        if self._is_running:
            self._is_running = False
            #sth else to stop here
        if self.d3d_object.is_capturing:
            self.d3d_object.stop()
        print("app stopped properly")

if __name__ == "__main__":
    app = rgbLBC_app(30,1)
    app.d3d_object.screenshot_every(1)
    sleep(1)
    # print(len(app.d3d_object.frame_buffer))
    # app.d3d_object.frame_buffer.popleft()
    # print(len(app.d3d_object.frame_buffer))
    if app.d3d_object.frame_buffer:
        print(len(app.d3d_object.frame_buffer))
    app.d3d_object.frame_buffer.popleft()
    if app.d3d_object.frame_buffer:
        print(len(app.d3d_object.frame_buffer))
    # print(app.is_running)
    app.stop()
