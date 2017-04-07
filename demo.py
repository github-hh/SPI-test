import cv2

image = cv2.imread("Tulips.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - gray", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

si=gray_image.shape

for ii in range(si[0]-1):
    for jj in range(si[1]-1):
        gray_image[ii,jj]=int(ii*jj/si[0]/si[1]*256)


cv2.imshow("test", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
