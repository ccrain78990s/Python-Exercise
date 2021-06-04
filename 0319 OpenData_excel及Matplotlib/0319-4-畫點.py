# 0319
import matplotlib.pyplot as plt     #<---要裝這個

#畫點
plt.plot([1,2,3,4], [1,4,9,16], 'ys')       # Y軸
#綠色 虛線樣式  g:
#黃色 方形標記  ys
plt.ylabel('some')
plt.axis([0,6,0,20])            #圖表範圍 x 0到6 y 0到20
plt.title('0319 train 2 ')
plt.show()
