# -*- coding: utf-8 -*-
"""SimpleLineFunction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p5M8-o9U22NPgztsVDfqBQDkP_fekRyr
"""

def SimpleLineFunction(x,y):
  import pandas as pd
  import matplotlib.pyplot as plt
  import math
 
  dataset=pd.DataFrame()
  dataset['x']=x
  dataset['y']=y
  #print(dataset)
  plt.scatter(dataset['x'],dataset['y'])
  plt.title("Visualising X, Actual Y")
  plt.show()
  x_mean = dataset['x'].mean()
  y_mean = dataset['y'].mean()
  #print(x_mean,y_mean)
  dataset['x - x_mean'] = dataset['x'] - x_mean
  dataset['y - y_mean'] = dataset['y'] - y_mean
  dataset['(x - x_mean)^2'] = dataset['x - x_mean']*dataset['x - x_mean']
  dataset['(x - x_mean) * (y - y_mean)']=dataset['x - x_mean']*dataset['y - y_mean']
  slope= dataset['(x - x_mean) * (y - y_mean)'].sum()/dataset['(x - x_mean)^2'].sum()
  intercept=y_mean - slope*x_mean
  print("\nLinear Regression model equ.: y = ",slope,"x + ",intercept)
  dataset['Est_y']=(slope*dataset['x']) + intercept
  dataset['y - Est_y'] = dataset['y'] - dataset['Est_y']
  dataset['(y - Est_y)^2'] = dataset['y - Est_y']*dataset['y - Est_y']
  mse=dataset['(y - Est_y)^2'].mean()
  rmse=math.sqrt(mse)
  print('\n',dataset)
  plt.scatter(dataset['x'],dataset['y'])
  plt.plot(dataset['x'],dataset['Est_y'])
  plt.title("Equ. of line")
  plt.show()
  print("\nMSE : ",mse,"\nRMSE :",rmse)

#sample input 1

x=[1,2,3,4,5,6]
y=[0,1,2,3,4,5]
SimpleLineFunction(x,y)

#sample input 2

a=[1,2,3,4,5,6]
b=[10,8,6,4,2,0]
SimpleLineFunction(a,b)

#sample input 3

c=[1,2,3,4,5,6]
d=[4,4,4,4,4,4]
SimpleLineFunction(c,d)

#sample input 4
# for same value of input, output is different in each scenario

e=[3,3,3,3,3,3]
f=[1,2,3,4,5,6]
SimpleLineFunction(e,f)

#sample input 5

g=[21,23,24,26,27]
h=[7,9,10,15,14]
SimpleLineFunction(g,h)

#data from file

from google.colab import files 
 
file_upload=files.upload()

import io 
import pandas as pd

ds = pd.read_csv(io.BytesIO(file_upload['goldprice.csv']))

i,j=ds['x'],ds['y'];
SimpleLineFunction(i,j)