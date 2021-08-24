from screen_capture_d3dshot import capture_rgb
from screen_capture import capture_rgb_PIL
from typing import Tuple
from PIL import Image
import numpy as np
import cv2


def linear_returner(arr:np.ndarray)->Tuple[float,float,float]:
    temp = np.sum(arr,axis=0)/arr.shape[0]
    temp = np.sum(temp,axis=0)/arr.shape[1]

    #temp = np.mean(arr, axis=(0,1))#slower than sum and divide
    
    return (temp[0],temp[1],temp[2])

#@jit(nopython=True)
def linear_returner_jit(arr:np.ndarray)->Tuple[float,float,float]:
    
    temp_r = 0.0
    temp_g = 0.0
    temp_b = 0.0
    for i in range(0,arr.shape[0],10):
        for j in range(0,arr.shape[1],10):
            temp_r += arr[i,j,0]
            temp_g += arr[i,j,1]
            temp_b += arr[i,j,2]
    
    norm = arr.shape[0]*arr.shape[1]/100
    return (temp_r/norm, temp_g/norm,temp_b/norm)
    # return (temp[0],temp[1],temp[2])

def wage_returner(arr:np.ndarray)->Tuple[float,float,float]:
    pass

def scale_down_returner_cv2(img:np.ndarray, shape:Tuple[int,int]):
    return cv2.resize(img, dsize=shape, interpolation=cv2.INTER_AREA)

def scale_down_returner_PIL(img:Image, shape:Tuple[int,int])->np.ndarray:
    return np.flip(np.array(img.resize(shape,resample=Image.BOX),dtype=np.uint8)[:,:,:3],axis=2)

if __name__ == "__main__":
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', (400, 800))
    
    while True:
        # im = capture_rgb_PIL(1920,1080)
        im = capture_rgb()
        im = scale_down_returner_PIL(im, (2,16))
        
        cv2.imshow("image",im)
        

        if cv2.waitKey(25)&0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    
    # linear_returner_jit(0.7*np.ones((1920,1080,3)))
    # print()
    # t1 = time.time()
    # print(linear_returner(0.7*np.ones((1920,1080,3))))
    # t2 = time.time()
    # print("time:",t2-t1)
    

    # print()
    # t1 = time.time()
    # print(linear_returner_jit(0.7*np.ones((1920,1080,3))))
    # t2 = time.time()
    # print("time:",t2-t1)

    #linear_returner_jit.inspect_types()