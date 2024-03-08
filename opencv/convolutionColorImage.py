import cv2  
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import statistics
        
        
if __name__ == "__main__":
    print("Hello OpenCV!!!")   
    
    

    #input data
    img  = cv2.imread("noise1.jpg", -1)
    b,g,r = cv2.split(img)
    
    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bconvImg = np.zeros(b.shape, np.uint8)

    kSizeX = 3
    kSizeY = 3
    kernel = np.ones((kSizeX, kSizeY), np.uint8) 
   
    

    anchorPoint = (int(kSizeX/2), int(kSizeY/2))
    kSum = kernel.sum()
    if kSum == 0:
        kSum = 1
        print(kSum)
        
    print("kernel ", kernel)    
    print("anchorPoint ", anchorPoint)
    

  
    for i in range(-anchorPoint[0], b.shape[0] - anchorPoint[0]):                 
        for j in range(-anchorPoint[1], b.shape[1] - anchorPoint[1]):            
            kernelSum = 0
            arr = []
            for ki in range(0, kernel.shape[0]):       
                for kj in range(0, kernel.shape[1]):   
                    ii = i
                    jj = j
                    
                    #handle left & top borders 
                    if i<0:
                        ii = 0
                    if j<0:
                        jj = 0
   
                    #handle right & bottom borders  
                    if ii + ki >= b.shape[0]:
                        ii = b.shape[0] - 1 - ki
                        
                    if jj + kj >= b.shape[1]:
                        jj = b.shape[1] - 1 - kj


                    #img * kernel --> convolution based multiplication
                    kernelSum =gray[ii+ki,jj+kj]*kernel[ki,kj]
                    arr.append(kernelSum)
                    arr.sort()
                    median = statistics.median(arr)
                   
                
            
               
          
            bconvImg[i+anchorPoint[0], j+anchorPoint[1]] = np.uint8(int(median))
    

# for green color
gconvImg = np.zeros(b.shape, np.uint8)
for i in range(-anchorPoint[0], g.shape[0] - anchorPoint[0]):                 
        for j in range(-anchorPoint[1], g.shape[1] - anchorPoint[1]):            
            kernelSum = 0
            arr = []
            for ki in range(0, kernel.shape[0]):       
                for kj in range(0, kernel.shape[1]):   
                    ii = i
                    jj = j
                    
                    #handle left & top borders 
                    if i<0:
                        ii = 0
                    if j<0:
                        jj = 0
   
                    #handle right & bottom borders  
                    if ii + ki >= b.shape[0]:
                        ii = g.shape[0] - 1 - ki
                        
                    if jj + kj >= b.shape[1]:
                        jj = g.shape[1] - 1 - kj


                    #img * kernel --> convolution based multiplication
                    kernelSum =g[ii+ki,jj+kj]*kernel[ki,kj]
                    arr.append(kernelSum)
                    arr.sort()
                    median = statistics.median(arr)
               
            gconvImg[i+anchorPoint[0], j+anchorPoint[1]] = np.uint8(int(median))
    

#for red color
rconvImg = np.zeros(r.shape, np.uint8)
for i in range(-anchorPoint[0], r.shape[0] - anchorPoint[0]):                 
        for j in range(-anchorPoint[1], r.shape[1] - anchorPoint[1]):            
            kernelSum = 0
            arr = []
            for ki in range(0, kernel.shape[0]):       
                for kj in range(0, kernel.shape[1]):   
                    ii = i
                    jj = j
                    
                    #handle left & top borders 
                    if i<0:
                        ii = 0
                    if j<0:
                        jj = 0
   
                    #handle right & bottom borders  
                    if ii + ki >= r.shape[0]:
                        ii = r.shape[0] - 1 - ki
                        
                    if jj + kj >= b.shape[1]:
                        jj = r.shape[1] - 1 - kj


                    #img * kernel --> convolution based multiplication
                    kernelSum =r[ii+ki,jj+kj]*kernel[ki,kj]
                    arr.append(kernelSum)
                    arr.sort()
                    median = statistics.median(arr)
               
            rconvImg[i+anchorPoint[0], j+anchorPoint[1]] = np.uint8(int(median))

colorIMg=cv2.merge([bconvImg, gconvImg, rconvImg])
    #Display
cv2.imshow('img', img)
cv2.imshow('colorIMg', colorIMg)
#cv2.imshow('bconvImg', bconvImg)
#v2.imshow('gconvImg', gconvImg)
#cv2.imshow('rconvImg', rconvImg)
cv2.waitKey(0)
    

