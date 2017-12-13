import numpy as np
import scipy.optimize as spop
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, Button, RadioButtons
"""
Andrew McLean 
Last Updated: 05/12/17
https://github.com/TropicalIsland/bow_shock_solver_ideal
Available under the MIT license
"""

# Define flow parameters and upstream boundary conditions
gamma = 1.4
n=400
M = np.linspace(1.1,6,n)

# Hida first
b=np.zeros(n)
del_hida=np.zeros(n)

lam=0.5*(1-3*(M**2-1)/(3*M**2-1))

C=3*(M**2-1)**2/((3*M**2-1)*(1+(gamma+1)/2*M**2))

# Zero finder for b
def f(b,C):
	return (C*(C**2-2*C+8)*b**4+4*(C**2-2*C-4)*b**2-4*C**3*b**2*np.log(b)-C**2*(2+C))
for i in range(0,n):
	b[i]=spop.brentq(f,0.1,10,xtol=1e-12,args=(C[i]))
	del_hida[i]=b[i]-1

# find del
cps=2/(gamma*M**2)*((((gamma+1)/2)**(gamma/(1-gamma)))*((((gamma+1)**2*M**2)/(4*gamma*M**2-2*(gamma-1)))**(gamma/(gamma-1)))*((1-gamma+2*gamma*M**2)/(gamma-1))-1)
cpmax=2/(gamma*M**2)*((((gamma+1)**2*M**2)/(4*gamma*M**2-2*(gamma-1)))**(gamma/(gamma-1))*((1-gamma+2*gamma*M**2)/(gamma-1))-1)

print(cpmax[n-1])
print(cps[n-1])
plt.plot(M,cps,M,cpmax)
"""
beta=np.pi/2-np.arcsin(np.sqrt(cps/cpmax))
theta=np.pi/2-beta

del_sincui=beta**2/(theta**2*np.cos(beta))*np.sqrt((2+(gamma-1)*M**2)/(2*gamma*M**2-gamma+1))

# Plot pretty pictures
global fig, ax
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
plt.plot(M,del_hida/2,'r--',M,del_sincui/2,'k-')

axlim=1
ax.grid(linestyle='-')
plt.xlabel(r'$M_\infty$')
plt.ylabel(r'$\frac{\delta}{D}$',rotation=0)
ax.set_xlim(1,6)
ax.set_ylim(0,4)
ax.set_aspect('auto',adjustable='box')
"""
plt.show()