from typing import Tuple
# from mss.screenshot import ScreenShot
import numpy as np
import cv2
# from mss import mss
from PIL import Image, ImageGrab

# sct = mss()

def capture_rgb_PIL(w:int,h:int)->Image:
     return ImageGrab.grab() 

# def capture_rgb_mss_numpy(w:int,h:int)->np.ndarray:    

#     return np.array(sct.grab({'top': 0, 'left': 0, 'width': w, 'height': h}), dtype=np.uint8)[:,:,:3]


def capture_rgb_fastgrab(w:int,h:int)->np.ndarray:
    pass

if __name__ == "__main__":
#print(img_numpy, img_numpy.shape)
    w, h = 1920, 1080
    monitor ={'top': 0, 'left': 0, 'width': w, 'height': h}
    #### test: show image on screen
    cv2.imshow("test",capture_rgb_PIL(w,h))
    cv2.waitKey(0)
    if 0xFF == ord('q'):
        cv2.destroyAllWindows()

################ continous grabbing
# while 1:
#     
#     img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
#     cv2.imshow('test', cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break