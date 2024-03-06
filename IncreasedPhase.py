import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import pi as pi, cos as cos, sin as sin
import seaborn as sns
import time as tm
from math import copysign as cps


'''
Declare the variables
---------------------------------------------------------------------------------------------------
'''

angular_v = 2*pi*(3*10**8)/(800*10**(-9)) # Most formulas use angular velocity, which is 2pi/lambda

charge = -1.602176*10**(-19) # Coulombs
mass = 9.1093837*10**(-31) # Kg

Intensity =(10**14)/10000 # W/m² 
E_0 = (2*(1.2566*10**(-6)*(3*10**8)*Intensity)) # V/m 



'''
Short code to plot the trajectory of the electron as you increase the phase
Currently facing a problem where I think Im getting the wrong result because Im looking for the wrong max kinetic energy (doesnt seem to actually be the problem)
-------------------------------------------------------------------------------------------------------
'''

n_wl = 1 # Number of full oscilations the electric field completes
time = np.linspace(0,(2*pi*n_wl)/angular_v,1000) # All of the graphs share the same time
dt = time[2] - time[1] # Time interval for 'integration'
phase = 0.5 # Multiples of pi/2 the maximum phase gets to
electrons = 10
lines = [i for i in range(electrons)]
lines2 = [i for i in range(electrons)]




phase = np.linspace(0,phase*0.5*pi,electrons)
maximumK = np.zeros(electrons) # Store the values of  maximum kinetic energy

fig, axs = plt.subplots(2,1,sharex=True,gridspec_kw={'height_ratios': [1, 3]}) # Declare what Im going to plot
fig.set_size_inches((7,5.5))

for i in range(electrons):
    energy = E_0*np.cos(angular_v*time + phase[i])
    
    

    acceleration = -charge*energy/mass
    velocity = np.zeros(len(acceleration))
    position = np.zeros(len(acceleration))
    kinetic = np.zeros(len(acceleration))
    
    for pos,val in enumerate(acceleration):
        if pos == 0:
            pass
        
        velocity[pos] = (val*dt)/2 + velocity[pos-1]
        position[pos] = (velocity[pos]*dt)/2 + position[pos-1]
        kinetic[pos] = 0.5*mass*velocity[pos]**2
    
    
    
    for pos,val in enumerate(position): # Find the kinetic energy when it recombines
        if pos == 0:
            pass
        if cps(1,val) + cps(1,position[pos-1]) == 0: # This breaks if the electron goes past the 0 point more than once
            maximumK[i] = kinetic[pos]
    
    position[position<0] = 0            
    lines2[i] = axs[0].plot(time,energy)    
    lines[i]  = axs[1].plot(time,position) # ,color=[0.3,i/electrons,0.805])
    
print(maximumK)
print(phase)

biggestK = max(maximumK)
for i in range(electrons):
    ratio = maximumK[i]/biggestK
    print(ratio)
    lines[i][0].set_color([ratio,1-ratio,0])
    lines2[i][0].set_color([ratio,1,0])
    

axs[0].set_title('Electric Field Amplitude')
axs[1].set_title('Electron Displacement')

fig.text(0.05, 0.8, 'Relative Amplitude',fontsize=7.5,va='center', rotation='vertical')
fig.text(0.05, 0.4, 'Distance from the atom (m)',fontsize=8,va='center', rotation='vertical')





'''
For next time, calculate the kinetic energy, and change the colour depending on that,
try to mimic the graph on the paper
'''

plt.grid()
plt.xlabel('Time(s)')
# plt.ylabel('Distance of the electron from the nucleus (m)')
plt.savefig('/home/alex/Desktop/Python/Atto/Plots/Electrondistance.png',dpi=400)