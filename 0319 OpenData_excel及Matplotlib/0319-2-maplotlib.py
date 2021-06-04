# 參考網址: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
# 0319 圖表是函式庫

import matplotlib.pyplot as plt     #<---要裝這個


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [35, 35, 30, 35, 27]
women_means = [35, 20, 34, 20, 25]
men_std = [5, 3, 4, 1, 2]
women_std = [5, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='girl')

ax.set_ylabel('Scores')                      #y軸標題
ax.set_title('Scores by group and gender')  #圖表標題
ax.legend()

plt.show()