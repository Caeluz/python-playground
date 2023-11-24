import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

arr = df[['Age', 'Fare']].values

# calculate the sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 1/(1+e^(-x))  x can be (ax+by+c)
sigmoid()