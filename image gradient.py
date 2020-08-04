import cv2
import numpy as np

img=cv2.imread('window.png')
img=cv2.resize(img, (400,400))

#Lets use laplacian gradient
lap=cv2.Laplacian(img, cv2.CV_64F,ksize=3) #so this laplacian gradient which give the directional change in intensity
lap=np.uint8((np.absolute(lap)))

#now lets try sobelX and sobelY
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)#it will find the directional change in x direction
sobelX=np.uint8((np.absolute(sobelX)))
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)#it will detect the change in y direction
sobelY=np.uint8((np.absolute(sobelY)))

cv2.imshow("lap",lap)
cv2.imshow("org",img)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY",sobelY)

cv2.waitKey(0)
cv2.destroyAllWindows()
