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
If anybody uses this code (They wont) be careful about changing variables in the below section since the main 
loop will break if you change the initial variables
'''

n_wl = 1 # Number of full oscilations the electric field completes
time = np.linspace(0,(2*pi*n_wl)/angular_v,1000) # All of the graphs share the same time
dt = time[2] - time[1] # Time interval for 'integration'
phase = 0.8 # Multiples of pi/2 the maximum phase gets to
electrons = 20
lines = [i for i in range(electrons)] # This is the list that stores all of the matplotlib line objects to change the colour later




maximumK = np.zeros(electrons) # Store the values of  maximum kinetic energy
energy = E_0*np.cos(angular_v*time)

fig, axs = plt.subplots(2,1,sharex=True,gridspec_kw={'height_ratios': [1, 3]}) # Declare what Im going to plot
fig.set_size_inches((7,5.5))
axs[0].plot(time,energy,color=[0.2,0.6,0.7])
axs[0].grid()

for i in range(electrons):
    time = np.linspace(0,(2*pi*n_wl)/angular_v,1000)
    
    timestart = i*0.5*pi*phase/(electrons*angular_v) # Automatically increases the displacement of the initial electrons
    
    time = time[time  >=  timestart]
    energy = E_0*np.cos(angular_v*time)
    

    acceleration = -charge*energy/mass
    velocity = np.zeros(len(acceleration))
    position = np.zeros(len(acceleration))
    kinetic = np.zeros(len(acceleration))
    
    '''
    Numerically integrate Newtons equations of motion for every point
    '''
    
    for pos,val in enumerate(acceleration):
        if pos == 0:
            pass
        
        velocity[pos] = (val*dt)/2 + velocity[pos-1]
        position[pos] = (velocity[pos]*dt)/2 + position[pos-1]
        kinetic[pos] = 0.5*mass*velocity[pos]**2
    
    
    
    for pos,val in enumerate(position): # Find the kinetic energy when it recombines
        if pos == 0:
            pass
        if cps(1,val) + cps(1,position[pos-1]) == 0: # This breaks if the electron goes past the 0 point more than once (I think)
            maximumK[i] = kinetic[pos]
    
    time = time[position>0]
    energy = energy[position>0]
    position = position[position>0]

 
    lines[i]  = axs[1].plot(time,position) # Store the lines so you can change the colour depending on kinetic energy
    

biggestK = max(maximumK)
for i in range(electrons):
    ratio = maximumK[i]/biggestK

    color = [0.1+ratio*0.7,0.2,0.8]
    #[ratio,ratio,ratio]
    lines[i][0].set_color(color)

    

axs[0].set_title('Electric Field Amplitude')
axs[1].set_title('Electron Displacement')

fig.text(0.05, 0.8, 'Relative Amplitude',fontsize=7.5,va='center', rotation='vertical')
fig.text(0.05, 0.4, 'Distance from the atom (m)',fontsize=8,va='center', rotation='vertical')





'''
Something on the long term plan is to take the electric field code and put it into a funtion you can import later
'''

plt.grid()
plt.xlabel('Time(s)')
# plt.ylabel('Distance of the electron from the nucleus (m)')
plt.savefig('/home/alex/Desktop/Python/Atto/Plots/Electrondistance.png',dpi=400)