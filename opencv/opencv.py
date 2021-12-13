# Modules
import cv2

#############################################################################################

# Read image 
IN_image= cv2.imread('../assets/rick.jpg',cv2.IMREAD_COLOR)

# Converts the RGB image to Grayscale
OUT_gray= cv2.cvtColor(IN_image,cv2.COLOR_BGR2GRAY)

# Image binarization ; any value greater than the threshold thresh is replaced with maxval and the other values are replaced with 0.
result,OUT_bin_image  = cv2.threshold(OUT_gray, 128, 255, cv2.THRESH_BINARY)

# Display image
cv2.imshow('window',OUT_bin_image)

# Waits infinitely for the window to close
cv2.waitKey(0)

# Destroys all the windows
cv2.destroyAllWindows()
