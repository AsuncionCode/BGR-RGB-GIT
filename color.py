import cv2 as cv 
import numpy as np 

#------------------------------------------------

'''bgr=np.zeros((300,300,3),dtype=np.uint8)

bgr[:,:,:]=(255,0,127)

cv.imshow('BGR',bgr)'''

#------------------------------------------------

'''image = cv.imread('pitogue.jpg')
CH1B=image[:,:,0]
CH2G=image[:,:,1]
CH3R=image[:,:,2]
cv.imshow('BGR',np.hstack([CH1B,CH2G,CH3R]))

rgb=cv.cvtColor(image,cv.COLOR_BGR2RGB)
CH1B=rgb[:,:,0]
CH2G=rgb[:,:,1]
CH3R=rgb[:,:,2]
cv.imshow('RGB',np.hstack([CH1B,CH2G,CH3R]))'''

#------------------------------------------------

image=cv.imread('pitogue5.jpg')

gris=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

cv.imshow('GRIS',gris)

cv.imshow('Original', image)

cv.waitKey(0)

cv.destroyAllWindows()