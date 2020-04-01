import cv2
import tensorflow as tf
img="../Cat/tesla-cat.jpg"
img=cv2.imread(img,-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

