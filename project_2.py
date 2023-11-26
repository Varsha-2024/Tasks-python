# importing library
import cv2

#Orginal image
img=cv2.imread(r'C:\Users\harsh\OneDrive\Desktop\ncstc logo.JPG',1)
cv2.imshow('Original Image', img)
cv2.waitKey(0)

#Gray Scale image
image=cv2.imread(r'C:\Users\harsh\OneDrive\Desktop\ncstc logo.JPG',0)
cv2.imshow('original', img)
cv2.imshow('GrayScale Image', image)
cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('original', img)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# Median Blur 
median = cv2.medianBlur(img, 9)
cv2.imshow('original', img)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Bilateral Blur 
bilateral = cv2.bilateralFilter(img, 14, 45, 75)
cv2.imshow('original', img)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)

#Edge Detection
# Setting parameter values
t_lower = 50  # Lower Threshold
t_upper = 150  # Upper threshold

# Applying the Canny Edge filter
edge = cv2.Canny(img, t_lower, t_upper)

cv2.imshow('original', img)
cv2.imshow('edge', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()