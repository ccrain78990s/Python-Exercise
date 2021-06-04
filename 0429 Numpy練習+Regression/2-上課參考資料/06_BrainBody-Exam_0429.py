import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Body']]
y_values = dataframe[['Brain']]
x_test =pd.DataFrame([80])
#訓練
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#預測
pre=body_reg.predict(x_values)
y_test_predict= body_reg.predict(x_test)

print(body_reg.predict( pd.DataFrame(data=[[170]])))

#圖形化
plt.scatter(x_values, y_values)
plt.scatter(x_test, y_test_predict, color='red')
plt.plot(x_values,pre )
plt.show()
