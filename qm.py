import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import pi as pi, cos as cos, sin as sin
from math import exp as exp
import seaborn as sns

'''
What the fuck is a localized particle raaaaah!
'''

fig, axs = plt.subplots(3,1,sharex=True) # Declare what Im going to plot
fig.suptitle("Various wavefunctions", fontsize=14)
fig.tight_layout(pad=1.5)

x = np.linspace(-5,5,1000)
psi_0 = [exp(-(i**2)/2) for i in x]
psi_1 = [((2*i**2-1)/(2**0.5))*exp(-(i**2)/2) for i in x]

psi_2 = [((-2*i**2+1)/(2**0.5))*exp(-(i**2)/2) for i in x]




axs[0].plot(x,psi_0,'-',color=[0,0.86,0.805])
axs[0].set_title('Wavefunction $\\psi_0$')

axs[1].plot(x,psi_1,'-r')
axs[1].set_title('Wavefunction $\\psi_1$')


axs[2].plot(x,psi_2,'-k',markersize=0.5)
axs[2].set_title('Wavefunction $\\psi_2$')



plt.xlabel('Position (m)')
fig.text(0.01, 0.5, 'Relative Amplitude', va='center', rotation='vertical')
for i in range(3):
    axs[i].grid()


plt.savefig('/home/alex/Desktop/Python/Atto/Plots/{}.png'.format('qmp3.jpg'),dpi=400) 




