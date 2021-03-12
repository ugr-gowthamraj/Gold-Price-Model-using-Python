# -*- coding: utf-8 -*-
"""GoldPrice Statistical model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qx7puM4jNmW4htNSpjQLHkG2suFwVw4y
"""

#uploading file to ide - colab
 
from google.colab import files 
 
file_upload=files.upload()

#storing the file as dataset

import io 
import pandas as pd

dataset = pd.read_csv(io.BytesIO(file_upload['goldprice.csv'])) 
print(dataset)

#Modeling starts
#for simple line equ. model we need to find slope and intercept...claculation of other variable needed to compute slope and intercept

#Calculating mean of x,y

x_mean = dataset['x'].mean()
y_mean = dataset['y'].mean()

#calculating x-x_mean and storing it in the same dataset

dataset['x - x_mean'] = dataset['x'] - x_mean
print(dataset)

#calculating y-y_mean and storing it in the same dataset

dataset['y - y_mean'] = dataset['y'] - y_mean
print(dataset)

#calculating (x - x_mean)^2 and storing it in the same dataset

dataset['(x - x_mean)^2'] = dataset['x - x_mean']*dataset['x - x_mean']
print(dataset)

#calculating (x - x_mean) * (y - y_mean) and storing it in the same dataset

dataset['(x - x_mean) * (y - y_mean)']=dataset['x - x_mean']*dataset['y - y_mean']
print(dataset)

#Formulating line equ. y = mx + c

slope= dataset['(x - x_mean) * (y - y_mean)'].sum()/dataset['(x - x_mean)^2'].sum()
intercept=y_mean - slope*x_mean
print("Linear Regression model equ.: y = ",slope,"x + ",intercept)

#calculating the estimated y values

dataset['Est_y']=(slope*dataset['x']) + intercept
print(dataset)

#calculating error to check the acceptance of the model

dataset['y - Est_y'] = dataset['y'] - dataset['Est_y']
print(dataset)

dataset['(y - Est_y)^2'] = dataset['y - Est_y']*dataset['y - Est_y']
print(dataset)

#calculating Mean Square Error and Root Mean Square Error

import math

mse=dataset['(y - Est_y)^2'].mean()
rmse=math.sqrt(mse)
print("MSE : ",mse,"\nRMSE :",rmse)

#Visualisation
#plotting x,y

import matplotlib.pyplot as plt

plt.scatter(dataset['x'],dataset['y'])
plt.title("Visualising X, Actual Y")
plt.show()

#Line equation for the dataset

plt.scatter(dataset['x'],dataset['y'])
plt.plot(dataset['x'],dataset['Est_y'])
plt.title("Equ. of line")
plt.show()
print("\nLinear Regression model equ.: y = ",slope,"x + ",intercept)
print("MSE : ",mse,"\nRMSE :",rmse)