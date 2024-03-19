from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,accuracy_score,r2_score
import pandas as pd
import numpy as np

#Getting the Data
X = np.arange(20).reshape(20,1)
y = [[x[0]*2 + 0.4] for x in X]    



x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=101)
model = LinearRegression()
print(f"X : {x_train}")
print(f"Y : {y_train}")

model.fit(x_train,y_train)


y_pred = model.predict(x_test)

print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))
print(model.coef_) #slope of the equation
print(model.intercept_) #bias of the equation

df = pd.read_csv("USA_Housing.csv")



