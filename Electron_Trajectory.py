'''

Despite being a bit confused, I will attempt to plot the graph of the electric field, and other
quantities an electron in high harmonic generation experiences.
On the way, I'll attempt to learn how to make cooler graphs.

---------------------------------------------------------------------------------------------------
First plot E-field (easy) for one cycle then afterwards subgraphs of all the other quantities,
figure out how to make it look sick

'''
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
phase = 0.5 # Radians


'''
Calculate the energy from the field, the position of the electron and the forcce experienced over time
for velocity and position, I simply calculated step by step rather than analitically, sue me.
-------------------------------------------------------------------------------------------------------
'''


time = np.linspace(0,(2*pi)/angular_v,1000) # All of the graphs share the same time
dt = time[2] - time[1] # Time interval for 'integration'



energy = E_0*np.cos(angular_v*time + phase)


acceleration = -charge*energy/mass
velocity = np.zeros(len(acceleration))
position = np.zeros(len(acceleration))

for pos,val in enumerate(acceleration):
    if pos == 0:
        pass
    velocity[pos] = (val*dt)/2 + velocity[pos-1]
    position[pos] = (velocity[pos]*dt)/2 + position[pos-1]



'''
Plot each one individually for clarity
---------------------------------------------------------------------------------------------------
'''

fig, axs = plt.subplots(3,1,sharex=True) # Declare what Im going to plot
fig.suptitle("Various parameters for a tunneled electron", fontsize=14)
fig.tight_layout(pad=1.5)


axs[0].plot(time,energy,'-',color=[0,0.66,0.805])
axs[0].set_title('Energy of the driving wave')

axs[1].plot(time,position,'-r',lw=0.5)
axs[1].set_title('Electron Position')


axs[2].plot(time,velocity,'-g',markersize=0.5)
axs[2].set_title('Velocity of the Electron')


plt.xlabel('Time (s)')
fig.text(0.01, 0.5, 'Relative Amplitude', va='center', rotation='vertical')
for i in range(3):
    axs[i].grid()


plt.savefig('/home/alex/Desktop/Python/Atto/Plots/{}.png'.format('electrontrajphase.jpg'),dpi=400) 

# plt.plot(time,energy)




