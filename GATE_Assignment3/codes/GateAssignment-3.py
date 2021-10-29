# -*- coding: utf-8 -*-
"""Untitled50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RsCDAR0ppysF5J4VltDBbLnDPXnLRFzD
"""

import numpy as np
from matplotlib import pyplot as plt

time = np.linspace(-3,5,10000)
unit_time = np.append(np.zeros(int((3/8)*len(time))),np.ones(int((5/8)*len(time))))
e1 = np.exp(2*time)

#We can find the step response using np.convolve() in the discrete domain as follows:
dt = 0.001 #Time interval for discretization of the continuous signals
Step_response = np.convolve(time*unit_time,e1*unit_time)*dt
print(Step_response)


#Plotting step response
x = ((np.exp(2*time)-2*time-1)/4)*unit_time
plt.plot(time,x,label='x(t)')
plt.xlabel('t')
plt.ylabel('$h(t)$')
plt.grid()
plt.show()

#Plotting g(t)
plt.plot(time,e1*unit_time)
plt.xlabel('t')
plt.ylabel('g(t)')
plt.grid()
plt.show()

#Plotting f(t)
plt.plot(time,time*unit_time)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.show()