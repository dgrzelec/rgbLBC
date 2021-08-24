# import numpy as np
import cv2

from PIL import Image, ImageGrab


def capture_rgb_PIL(w:int,h:int)->Image:
     return ImageGrab.grab() 


if __name__ == "__main__":

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