# -*- coding: utf-8 -*-
"""Untitled50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RsCDAR0ppysF5J4VltDBbLnDPXnLRFzD
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3,5,100)

y=[]
x=[]
h=[]

for i in t:
  if (i>=-2 and i<-1):
    y.append(2)
  elif (i>=-1 and i<2): 
    y.append(-1) 
  else:
    y.append(0)

for i in t:
  if (i>=0):
    x.append(1)
  else:
    x.append(0)    

plt.plot(t,x)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.title('input')
plt.show()

plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title('output')
plt.show()