# 0319
import matplotlib.pyplot as plt     #<---要裝這個



#畫點畫線
plt.plot([1,2,3,4], [1,4,9,16], 'ys',label='apple')       # Y軸
plt.plot([8,2,7,4], [1,4,7,9], 'k-',label='banana')
plt.plot([5,6,7,4], [2,3,8,10], 'cv',label='pineapple')
plt.ylabel('some')
plt.axis([0,6,0,20])            #圖表範圍 x 0到6 y 0到20
plt.title('0319 train 2 ')
plt.legend()
plt.show()
