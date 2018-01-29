#######################
## Résolution exacte ##
#######################

## Librairies
import numpy as np;
import scipy.integrate as int;
import matplotlib.pyplot as plt;

## Principe
# Prototype: int.odeint(equation, CI, temps_simulation) pour une équation y' = f(y,t)
# Résout seulement les équations du premier ordre.
# Résout les équations vectorielles


## Equation linéaire du premier ordre: y' + y/tau = 0
# Mise sous forme 'canonique': y' + y/tau = 0 <-> y' = -y/tau

tau = 10**-3

def equ(y,t):
	return -y/tau;

t = np.linspace(0,10*tau, 100)

sol = int.odeint(equ, 5, t)

#plt.plot(t, sol)


## Equation linéaire du second ordre: y'' + w/Q y' + w²y = 0
# On vectorise l'équation. On pose Y = [y, y'].
# Forme canonique:  Y' + [ [0] [1], [w²] [w/Q] ] Y = 0
#
w = 2
Q = 10

def equ(Y,t):
	return [Y[1], -w/Q*Y[1] - w*w*Y[0]]

t = np.linspace(0, 15*w, 1000)

sol = int.odeint(equ, [5, 0], t)

plt.plot(t, sol[:,0])
plt.grid()













#####################
## Méthode d'Euler ##
#####################
# Equation du type: y' = F(y,t)
# y' = (y[i+1]-y[i])/h
# Donc: y[i+1] = y[i] + h * F(y[i], t)


## Librairies
import matplotlib.pyplot as plt;
import numpy as np


## Equation linéaire du premier ordre: y' + y/tau = 0
tau = 2

def F(y,t):
	return -y/tau

def euler():
	n = 100
	tf = 5
	h = tf/n

	t = np.linspace(0, tf, n+1)
	y = np.zeros(n+1)

	y[0] = 5

	for k in range(n):
		y[k+1] = y[k] + h*F(y[k], t[k])

	plt.plot(t,y)


## Equation linéaire du second ordre: y'' + w/Q y' + w²y = 0
w = 2.
Q = 10.


def euler():
	n = 10000
	tf = 15*w
	h = tf/n

	t = np.linspace(0, tf, n+1)
	y = np.zeros(n+1)
	dy = np.zeros(n+1)

	y[0] = 5
	dy[0] = 0

	for k in range(n):
		y[k+1] = y[k] + h*dy[k]
		dy[k+1] = dy[k] - h * w**2 * y[k] - h * w/Q * dy[k]

	plt.plot(t,y)
