import numpy as np
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
M = 1.4

# find del
cps=2/(gamma*M**2)*(((gamma+1)/2)**(-gamma/(gamma-1))*(((gamma+1)**2*M**2)/(4*gamma*M**2-2*(gamma-1)))**(gamma/(gamma-1))*(1-gamma+2*gamma*M**2/(gamma-1))-1)
cpmax=2/(gamma*M**2)*((((gamma+1)**2*M**2)/(4*gamma*M**2-2*(gamma-1)))**(gamma/(gamma-1))*(1-gamma+2*gamma*M**2/(gamma-1))-1)

beta=np.pi/2-np.arcsin(np.sqrt(cps/cpmax))
theta=np.pi/2-beta

delta=beta**2/(theta**2*np.cos(beta))*np.sqrt((2+(gamma-1)*M**2)/(2*gamma*M**2-gamma+1))



# Calculate shock shape as in Hida
lam=0.5*(1-3*(M**2-1)/(3*M**2-1))
b=delta+1
eps=np.linspace(-np.pi/2,np.pi/2,200)
r=b*(1+lam*eps**2)

# Translate answers to x and y

x=-r*np.cos(eps)
y=r*np.sin(eps)


# Plot pretty pictures
global fig, ax
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
global l
l, = plt.plot(x,y,'g-')

global circ
circ=mpatches.Circle((0, 0), 1, color='b', fill=False)
ax.add_patch(circ)


axlim=1.2*3
ax.grid(linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlim(-axlim,axlim)
ax.set_ylim(-axlim,axlim)
ax.set_aspect('equal',adjustable='box')



# Make parameter sliders and locate them nicely
axcolor = 'lightgoldenrodyellow'
axG = plt.axes([0.25, 0.16, 0.65, 0.03], facecolor=axcolor)
axM = plt.axes([0.25, 0.11, 0.65, 0.03], facecolor=axcolor)

sgam = Slider(axG, 'Gamma', 1.2, 1.8, valinit=gamma)
sM = Slider(axM, 'Upstream Mach No', 1.1, 3, valinit=M)



# Define slider functions & provide trace functionality
def update(val):
	gamma 	= sgam.val
	M 	= sM.val
	
	cps=2/(gamma*M**2)*(((gamma+1)/2)**(-gamma/(gamma-1))*(((gamma+1)**2*M**2)/(4*gamma*M**2-2*(gamma-1)))**(gamma/(gamma-1))*(1-gamma+2*gamma*M**2/(gamma-1))-1)
	cpmax=2/(gamma*M**2)*((((gamma+1)**2*M**2)/(4*gamma*M**2-2*(gamma-1)))**(gamma/(gamma-1))*(1-gamma+2*gamma*M**2/(gamma-1))-1)

	beta=np.pi/2-np.arcsin(np.sqrt(cps/cpmax))
	theta=np.pi/2-beta

	delta=beta**2/(theta**2*np.cos(beta))*np.sqrt((2+(gamma-1)*M**2)/(2*gamma*M**2-gamma+1))
	print(beta)
	lam=0.5*(1-3*(M**2-1)/(3*M**2-1))
	b=delta+1
	eps=np.linspace(-np.pi/2,np.pi/2,200)
	r=b*(1+lam*eps**2)

	# Translate answers to x and y

	x=-r*np.cos(eps)
	y=r*np.sin(eps)

	l.set_ydata(y)
	l.set_xdata(x)

	fig.canvas.draw_idle()

sgam.on_changed(update)
sM.on_changed(update)

# Make reset button
# Only resets inital params! Not window!
resetax = plt.axes([0.08, 0.01, 0.1, 0.04])
reset_button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
	sgam.reset()
	sM.reset()


reset_button.on_clicked(reset)

plt.show()