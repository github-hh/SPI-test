from scipy import misc
import matplotlib.pyplot as plt

image = misc.imread("Tulips.jpg",flatten=True)
plt.figure()
plt.gray()
plt.imshow(image)
plt.show()

import cv2

image = cv2.imread("Tulips.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# plt.imshow(mpimg.imread('Tulips.png'))


cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - gray", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

si=gray_image.shape

for ii in range(si[0]):
    for jj in range(si[1]):
        gray_image[ii,jj]=ii*jj/si[0]/si[1]*256


cv2.imshow("test", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.colormaps()
# plt.imshow(gray_image,cmap='gray')
plt.imshow(gray_image, cmap=cm.gray)
plt.show()

from numpy import *
a=array([[2,3,4],[1,2,3]])
c=array([1,2, 3, 4, 5, 6, 7, 8])
c.reshape(-1,2)

