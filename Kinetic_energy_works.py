import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import pi as pi, cos as cos, sin as sin
import seaborn as sns
import time as tm
from math import copysign as cps

'''
The next step is to plot the kinetic energy in general depending on the moment when the electron is released
'''

angular_v = 2*pi*(3*10**8)/(800*10**(-9)) # Most formulas use angular velocity, which is 2pi/lambda

charge = -1.602176*10**(-19) # Coulombs
mass = 9.1093837*10**(-31) # Kg

Intensity =(10**14)/10000 # W/m² 
E_0 = (2*(1.2566*10**(-6)*(3*10**8)*Intensity)) # V/m 

 


precision_time = 1000 # Number of time points to plot
n_wl = 1 # Number of full oscilations the electric field completes
time = np.linspace(0,(2*pi*n_wl)/angular_v,precision_time) # All of the graphs share the same time
dt = time[2] - time[1]
phase_i = pi/2# Until what phase to plot

E_t = -E_0*np.cos(angular_v*time)
electrons = 50
maximumK = np.zeros([electrons,2])
lines = [i for i in range(electrons)]


fig, axs = plt.subplots(3,1,sharex=True,gridspec_kw={'height_ratios': [1, 3,1]}) # Declare what Im going to plot
fig.set_size_inches((9.5,8.5))
axs[0].plot(time,E_t,color=[0.2,0.9,0.7])
axs[0].grid()
kinetic_graph = np.zeros([electrons,3])

for i in range(electrons):
    
      # Automatically increases the displacement of the initial electrons
    timestart = np.where(time >= (i/electrons)*(phase_i/(n_wl*2*pi))*time[-1])[0][0] # What position in the time array is the starting time
    # print(timestart)
    time_electron = time[timestart:]
    energy = E_t[timestart:]
    

    acceleration = charge*energy/mass
    velocity = np.zeros(len(acceleration))
    position = np.zeros(len(acceleration))
    kinetic = np.zeros(len(acceleration))
    
    '''
    Numerically integrate Newton's equations of motion for every point
    '''
    
    for pos,val in enumerate(acceleration):
        if pos == 0:
            pass
        else:
            velocity[pos] = (val*dt)/2 + velocity[pos-1] # This is technically slightly wrong but womp womp
            position[pos] = (velocity[pos]*dt)/2 + position[pos-1]
            kinetic[pos] = 0.5*mass*velocity[pos]**2
    
    
    
    for pos,val in enumerate(position): # Find the kinetic energy when it recombines
        if pos == 0 or pos == 1:
            pass
        else:
            if cps(1,val) + cps(1,position[pos-1]) == 0: # This breaks if the electron goes past the 0 point more than once (I think)
                # print(val)
                position = position[:pos]
                time_electron = time_electron[:pos]
                energy = energy[:pos]
                kinetic = kinetic[:pos]
                
                break

    maximumK[i]= [max(kinetic),time_electron[0]]
    
    lines[i]  = axs[1].plot(time_electron,position) # Store the lines so you can change the colour depending on kinetic energy
    
    kinetic_graph[i,0] = time_electron[0]
    kinetic_graph[i,1] = time_electron[-1]
    kinetic_graph[i,2] = maximumK[i,0]
        

# print(kinetic_graph)
'''
Need to create an array that stores the position the electron is released and it's max kinetic energye
'''

# for i in range(kinetic):
#     axs[1].plot(kinetic,time)
axs[2].plot(kinetic_graph[:,0],kinetic_graph[:,2],color=[0.85,0.2,0.3])
axs[2].plot(kinetic_graph[:,1],kinetic_graph[:,2],color=[0.85,0.2,0.3])

maximumK = maximumK[:,0]
biggestK = max(maximumK)
for i in range(electrons):
    ratio = maximumK[i]/biggestK

    color = [0.1+ratio*0.7,0.2,0.8]
    #[ratio,ratio,ratio]
    lines[i][0].set_color(color)
    
axs[0].set_title('Electric Field Amplitude')
axs[1].set_title('Electron Displacement')
axs[2].set_title('Maximum Kinetic Energy of electrons at ionization and recombination time')
axs[2].grid()

fig.text(0.05, 0.8, 'Relative Amplitude',fontsize=7.5,va='center', rotation='vertical')
fig.text(0.05, 0.5, 'Distance from the atom (m)',fontsize=8,va='center', rotation='vertical')
fig.text(0.05, 0.2, 'Max Kinetic Energy (J)',fontsize=8,va='center', rotation='vertical')

axs[1].grid()
plt.xlabel('Time(s)')
# plt.ylabel('Distance of the electron from the nucleus (m)')
plt.savefig('/home/alex/Desktop/Python/Atto/Plots/kineticplot.png',dpi=400)
