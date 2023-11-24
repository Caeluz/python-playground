import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

df = pd.read_csv("csv/titanic.csv")

df['Male'] = df['Sex'] == 'male'

X = df[['Pclass', 'Male', 'Age', 'Siblings/Spouses',
        'Parents/Children', 'Fare']].values
y = df['Survived'].values

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)

# Total number of correct predictions / total number of passengers
# print((y == y_pred).sum() / y.shape[0]) // long
# short
print(model.score(X, y))
