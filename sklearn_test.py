import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

df = pd.read_csv("csv/titanic.csv")

df['Male'] = df['Sex'] == 'male'

X = df[['Fare', 'Age']].values
y = df['Survived'].values

model = LogisticRegression()
model.fit(X, y)

# Get the coefficients and intercept
coef = model.coef_
intercept = model.intercept_

# Plot the scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)

# Plot the decision boundary
a = coef[0][0]          # Coefficient for 'Fare'
b = coef[0][1]          # Coefficient for 'Age'
c = intercept[0]        # Intercept

# Range of x values for which you want to calculate y values
x1 = range(30, 120, 5)
# Calculate corresponding y values based on the line equation - y = (-ax - c) / b
y1 = (-a * x1 - c) / b

plt.plot(x1, y1, '-b', label='')


plt.xlabel('Fare')
plt.ylabel('Age')
plt.title('Logistic Regression Decision Boundary')
plt.show()
