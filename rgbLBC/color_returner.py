# from screen_capture_d3dshot import capture_rgb
import d3dshot
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
    #return np.flip(np.array(img.resize(shape,resample=Image.BOX),dtype=np.uint8)[:,:,:3],axis=2) #flip possibly only for cv2 display
    return np.array(img.resize(shape,resample=Image.BOX),dtype=np.uint8)[:,:,:3]

if __name__ == "__main__":
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', (400, 800))
    
    d = d3dshot.create('pil')
    N = 30

    while True:
        # im = capture_rgb_PIL(1920,1080)
        im = capture_rgb()
        im = scale_down_returner_PIL(im, (2,16))
        im[0,0,:] = 255
        im[0,1,:] = 255

        # im = np.concatenate((np.flip(im[:,0,:], axis=0) ,im[:,1,:]),axis=0, dtype=np.uint8)
        # print(im.shape)

        im2 = im.reshape((2*N,1,3), order='F')
        im2[0:N,0,:] = im2[N-1::-1,0,:]

        cv2.imshow("image",np.flip(im,axis=-1))
        

        if cv2.waitKey(25)&0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    # im = d.screenshot()
    # im = scale_down_returner_PIL(im, (2,N))
    # im[0,0,:] = 255
    # im[0,1,:] = 255
    
    # import time
    # t1 = time.time()
    # for _ in range(1000):
    #     im2 = np.concatenate((np.flip(im[:,0,:], axis=0) ,im[:,1,:]),axis=0, dtype=np.uint8)
    # t2 = time.time()
    # print("time concatenate:",(t2-t1)/1000)
    # print("shape im2 = ", im2.shape)

    # im = d.screenshot()
    # im = scale_down_returner_PIL(im, (2,N))
    # im[0,0,:] = 255
    # im[0,1,:] = 255

    

    # t1 = time.time()
    # for _ in range(1000):
    #     im2 = im.reshape((2*N,1,3), order='F')
    #     im2[0:N,0,:] = im2[N-1::-1,0,:]
    #     im2 = np.squeeze(im2)
    # t2 = time.time()
    # print("time concatenate:",(t2-t1)/1000)
    # print("shape im2 = ", im2.shape)