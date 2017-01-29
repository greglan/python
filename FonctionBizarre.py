##Fonction (-a)^x = exp(x*ln(-a))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cmath import *
from math import pi

fig = plt.figure()
ax = fig.add_subplot( 111, projection = '3d' )
i = complex(0,1);
a = -0.8;
pas = 0.01;
max = 30;

plt.title("$f(x) = \,("+str(a)+")^x = \, a + ib$");

ax.set_xlabel('$x$')
ax.set_ylabel('Partie reelle $a$')
ax.set_zlabel('Partie imaginaire $b$')


def fct(pas, max):
    x = [ -k * pas for k in range(1, int( max / pas ) + 1 ) ] + [ k * pas for k in range(0, int( max / pas ) + 1 ) ];
    x.sort();
    y = [ exp(k * log(a, e)).real for k in x ];
    z = [ exp(k * log(a, e)).imag for k in x ];
    return x,y,z;

Lx, Ly, Lz = fct(pas, max);
ax.plot3D(Lx, Ly, Lz, c='r', marker='o');
plt.show();

