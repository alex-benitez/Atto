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
phase_i = pi*0.8# Very specific value for aesthetic reasons

charge = -1.602176*10**(-19) # Coulombs
mass = 9.1093837*10**(-31) # Kg

Intensity =(10**14)/10000 # W/m² 
E_0 = (2*(1.2566*10**(-6)*(3*10**8)*Intensity)) # V/m 

 



n_wl = 1.2 # Number of full oscilations the electric field completes
time = np.linspace(0,(2*pi*n_wl)/angular_v,1000) # All of the graphs share the same time
dt = time[2] - time[1]


energy = E_0*np.cos(angular_v*time + phase_i)
electrons = 50
maximumK = np.zeros([electrons,2])
lines = [i for i in range(electrons)]


fig, axs = plt.subplots(3,1,sharex=True,gridspec_kw={'height_ratios': [1, 3,1]}) # Declare what Im going to plot
fig.set_size_inches((9.5,8.5))
axs[0].plot(time,energy,color=[0.2,0.9,0.7])
axs[0].grid()

for i in range(electrons):
    
     # Automatically increases the displacement of the initial electrons
    timestart = (2*pi*n_wl*i)/(angular_v*electrons)
    print(timestart)
    time_electron = time[time >= timestart]
    energy = E_0*np.cos(angular_v*time_electron)
    

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
            break

    maximumK[i]= [max(kinetic),time_electron[0]]
    
    # time_electron = time_electron[position>0]
    # energy = energy[position>0]
    # position = position[position>0]
    
    lines[i]  = axs[1].plot(time_electron,position) # Store the lines so you can change the colour depending on kinetic energy
    

print(kinetic)


# for i in range(kinetic):
#     axs[1].plot(kinetic,time)
axs[2].plot(maximumK[:,1],maximumK[:,0],color=[0.85,0.2,0.3])

maximumK = maximumK[:,0]
biggestK = max(maximumK)
for i in range(electrons):
    ratio = maximumK[i]/biggestK

    color = [0.1+ratio*0.7,0.2,0.8]
    #[ratio,ratio,ratio]
    lines[i][0].set_color(color)
    
axs[0].set_title('Electric Field Amplitude')
axs[1].set_title('Electron Displacement')
axs[2].set_title('Maximum Kinetic Energy of electrons released at t')
axs[2].grid()

fig.text(0.05, 0.8, 'Relative Amplitude',fontsize=7.5,va='center', rotation='vertical')
fig.text(0.05, 0.5, 'Distance from the atom (m)',fontsize=8,va='center', rotation='vertical')
fig.text(0.05, 0.2, 'Max Kinetic Energy (J)',fontsize=8,va='center', rotation='vertical')

axs[1].grid()
plt.xlabel('Time(s)')
# plt.ylabel('Distance of the electron from the nucleus (m)')
plt.savefig('/home/alex/Desktop/Python/Atto/Plots/Electrondistance.png',dpi=400)

