import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# 原圖片 BGR
img = cv2.imread('1.jpg')
plt.imshow(img)
plt.plot([100,200,300], [300,200,300])
plt.show()


# 方法一 RGB顯示

img = mpimg.imread('1.jpg')
plt.imshow(img)
plt.plot([100,200,300], [300,200,300])
plt.show()


# 方法二
img = cv2.imread('1.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.plot([100,200,300], [300,200,300])
plt.show()