import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import pi as pi, cos as cos, sin as sin
import seaborn as sns



'''
Declare the variables
---------------------------------------------------------------------------------------------------
'''

angular_v = 2*pi*(3*10**8)/(800*10**(-9)) # Most formulas use angular velocity, which is 2pi/lambda

charge = -1.602176*10**(-19) # Coulombs
mass = 9.1093837*10**(-31) # Kg
E_0 = 1 # V/m



'''
Short code to plot the trajectory of the electron as you increase the phase
-------------------------------------------------------------------------------------------------------
'''


time = np.linspace(0,(2*pi)/angular_v,1000) # All of the graphs share the same time
dt = time[2] - time[1] # Time interval for 'integration'


for i in range(20):
    phase = i*pi/80-pi/4 # It cycles until it reaches a quarter of a wavelength
    energy = E_0*np.cos(angular_v*time + phase)
    
    
    acceleration = -charge*energy/mass
    velocity = np.zeros(len(acceleration))
    position = np.zeros(len(acceleration))
    
    for pos,val in enumerate(acceleration):
        if pos == 0:
            pass
        velocity[pos] = (val*dt)/2 + velocity[pos-1]
        position[pos] = (velocity[pos]*dt)/2 + position[pos-1]
    
    for pos,val in enumerate(position):
        if val <0:
            time = time[:pos]
            position = position[:pos]
            break
    
    plt.plot(time,position,color=[0,0.05*i,0.805])
    
plt.grid()
plt.xlabel('Time(s)')
plt.ylabel('Distance of the electron from the nucleus (m)')
plt.savefig('/home/alex/Desktop/Python/Atto/Plots/Electrondistance.png',dpi=400)