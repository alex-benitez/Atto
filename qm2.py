import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import pi as pi, cos as cos, sin as sin
from math import exp as exp
import seaborn as sns

'''
What the fuck is a localized particle raaaaah!
'''



x = np.linspace(-5,5,1000)
psi_0 = [exp(-(i**2)/2) for i in x]
psi_1 = [((2**0.5)*i*exp(-(i**2)/2)) for i in x]

psi_2 = [exp(-(i**2)/2)*(((-2*i**2)+1)/(2**0.5)) for i in x]

# plt.plot(x,psi_0)
# plt.plot(x,psi_1)
# plt.plot(x,psi_2)


psi_0 = np.array(psi_0)
psi_1 = np.array(psi_1)
psi_2 = np.array(psi_2)
superpose = ((psi_0 + 2*psi_1 + psi_2)/(6**0.5))**2
plt.plot(x,superpose)





plt.xlabel('Position (m)')
plt.ylabel('Relative Amplitude')
plt.grid()

plt.savefig('/home/alex/Desktop/Python/Atto/Plots/{}.png'.format('qmproblemclass.jpg'),dpi=400) 