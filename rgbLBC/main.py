from time import sleep

import numpy as np
# from d3dshot.d3dshot import D3DShot
# from d3dshot import create
import d3dshot
from PIL import Image

#change downsampling func here if necessary
from color_returner import scale_down_returner_PIL as downsample_func


class rgbLBC_app(object):
    def __init__(
        self, 
        n_LEDs:int, 
        target_fps:int, 
        debug:bool = False, 
        log_func = print, 
        display_idx = 0
        ) -> None:
 
        # super().__init__(capture_output='pil', frame_buffer_size=1) #buffer_size = 1 for pop aproach
        self.d3d_object = d3dshot.create(capture_output='pil', frame_buffer_size=1)

        self.nLEDs = n_LEDs
        self.target_fps = target_fps
        self.debug = debug
        self.log_func = log_func
        self.display_idx = display_idx

        self.shape = (2,self.nLEDs)
        self.rgb_vals_array = np.zeros(self.shape)


        ############################### displays
        self.__log("Displays available:")
        for i,display in enumerate(self.displays):
            self.__log("[{}]".format(i)+str(display))
        self.__log("Choosing display index [{}]".format(self.display_idx))
        self.set_display(self.display_idx)
        ################################

        self._is_running = False
    

    #### instead of inheritance(which doesnt work), getattr is used
    def __getattr__(self,name):
        return self.d3d_object.__getattribute__(name)

    @property
    def is_running(self)->bool:
        return self._is_running

    @property
    def is_frame_ready(self)->bool:
        return bool(self.frame_buffer)

    def get_current_rgb(self)->np.ndarray:
        return self.rgb_vals_array

    def pop_latest_frame(self)->Image:
        return self.frame_buffer.popleft()

    def __generate_rgb(self):
        return downsample_func(self.pop_latest_frame(), self.shape) 

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
            self.display = self.displays[index]
            self.__log("Display set to: " + "[{}]".format(index)+str(self.display))
        except IndexError:
            self.__log("No display with index [{}] detected".format(index), "WARNING")
            self.display = self.displays[0]
            self.__log("Display set to: " + "[{}]".format(0)+str(self.display))
        

    def start(self):
        pass
    
    def stop(self):
        if self._is_capturing:
            self.d3d_object.stop()

        if self._is_running:
            self._is_running = False
            #sth else to stop here

        self.__log("app stopped properly")

if __name__ == "__main__":
    from exit_handler import set_exit_handler

    print("enter main")

    app = rgbLBC_app(30,40)
    set_exit_handler(app.stop)
    app.screenshot()
    # app.set_display(0)

    app.screenshot_every(1)
    sleep(1)
    # print(len(app.d3d_object.frame_buffer))
    # app.d3d_object.frame_buffer.popleft()
    # print(len(app.d3d_object.frame_buffer))
    if app.is_frame_ready:
        print(len(app.frame_buffer))
    app.pop_latest_frame()
    if app.is_frame_ready:
        print(len(app.frame_buffer))
    # print(app.is_running)
    app.stop()
