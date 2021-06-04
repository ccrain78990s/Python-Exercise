# pip install scikit-learn

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# 第一題 : 找出迴歸的三個函數
print("---------------------------------------")
# 第二題 : 1個蘋果 5 塊錢   2 個蘋果 10 塊錢   3 個蘋果 15 塊錢 ,
#         請問 10 個蘋果 多少錢
# 第三題:  1個蘋果和1個西瓜 100 塊錢   2 個蘋果和2個西瓜 200 塊錢,  3 個蘋果和3個西瓜 300 塊錢,
# 第四題:  用圖形的方法把  第二題 的情況畫出來
# 第五題:  把  第二題 的  reg.coef_ 係數    reg.singular_ 單數  印出
# 第六題: 透過 練習題資料.xlsx 來訓練迴歸, 請問 當以下資料匯入 Label 預測為多少?



# 練1
"""
linear_model.LinearRegression()  初始化
fit                              訓練/擬合
predict                          預測
"""

print("====練2====")
x_values =pd.DataFrame([[1],  [2],  [3],  [4]])
y_values =pd.DataFrame([5,10,15,20])
x_test =pd.DataFrame([10])

#train model on data
body_reg = linear_model.LinearRegression()    # 初使化
body_reg.fit(x_values, y_values)              # 訓練

y_test_predict= body_reg.predict(x_test)      # 預測
print(" 預測值",y_test_predict)
# 練4 畫圖
#visualize results
plt.title("4.plt")
plt.scatter(x_values, y_values)
plt.scatter(x_test, y_test_predict, color='red')
# plt.plot(x_test,y_test_predict, color='blue')

plt.show()

print("====練3====")
x_values =pd.DataFrame([[1,1], [2,2] , [3,3] ])
y_values =pd.DataFrame([100,200,300])
x_test =pd.DataFrame([[10,10]])

#train model on data
body_reg = linear_model.LinearRegression()    # 初使化
body_reg.fit(x_values, y_values)              # 訓練

y_test_predict= body_reg.predict(x_test)      # 預測
print(" 預測值",y_test_predict)

print("====練5====")
print('Coefficients: \n', body_reg.coef_)
print('singular: \n', body_reg.singular_ )

print("====練6====")
df=pd.read_excel('練習題資料.xlsx','Sheet1')
df=df.to_numpy()

# Use only one feature
df_X = df[:,:10]  # BMI~S6
# Split the data into training/testing sets
df_X_train = df_X[:-20]
df_X_test = df_X[-20:]

df_Y=df[:,10:]
# Split the targets into training/testing sets
df_Y_train = df_Y[:-20]
df_Y_test = df_Y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(df_X_train, df_Y_train)
print(regr.predict(df_X_test))

