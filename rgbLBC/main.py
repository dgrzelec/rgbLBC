import numpy as np
import d3dshot

from PIL import Image
#change downsampling func here if necessary
from color_returner import scale_down_returner_PIL as downsample_func

from exit_handler import set_exit_handler


class rgbLBC_app:
    def __init__(self, n_LEDs:int, target_fps:int, debug:bool) -> None:
        self.nLEDs = n_LEDs
        self.target_fps = target_fps
        self.debug = debug

        #initializations
        set_exit_handler(self.stop)
        self.d3d_object = d3dshot.create(capture_output='pil', frame_buffer_size=self.target_fps)

    def __generate_rgb():
        pass

    def send_to_COM():
        pass

    def start():
        pass
    
    def stop():
        print("app stopped properly")

if __name__ == "__main__":
    app = rgbLBC_app()

