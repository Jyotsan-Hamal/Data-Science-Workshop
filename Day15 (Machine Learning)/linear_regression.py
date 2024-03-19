from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,accuracy_score,r2_score
import pandas as pd
import numpy as np

df = pd.read_csv("USA_Housing.csv")




X = df.drop(columns=['Address','Price'],axis=1)
Y = df['Price']

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=101)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(model.coef_)
print(r2_score(y_test,y_pred))

