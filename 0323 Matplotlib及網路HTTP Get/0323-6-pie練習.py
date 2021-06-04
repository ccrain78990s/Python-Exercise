
#參考網址 ↓
#https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
import matplotlib.pyplot as plt


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'more than 5 years', '6 months', '1 year', '2 years', '3 years', '4 years'
sizes = [16, 10, 12, 28,20,14]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()