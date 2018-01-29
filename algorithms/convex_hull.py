""" Bug """

import matplotlib.pyplot as plt
from random import randint
from random import random

def min_point(tab,n):
    l_min = []
    min = tab[1][0]
    
    for j in range(n):
        if tab[1][j] < min:
            l_min = [j]
        elif tab[1][j] == min:
            l_min.append(j)
    
    # Minimum abscissa of the min point
    min = tab[0][l_min[0]]
    i = l_min[0]
    
    for j in l_min:
        if tab[0][j] < min:
            i = j
    
    return i


def orient(tab, i, j, k):
    a = tab[0][j]-tab[0][i]
    b = tab[1][j]-tab[1][i]
    c = tab[0][k]-tab[0][i]
    d = tab[1][k]-tab[1][i]
    
    # Déterminant
    r = 0.5*(a*d-b*c)
    
    if r == 0:
        return 0
    elif r>0:
        return 1
    else:
        return -1


# Next point, assuming the current one is i
def nextPoint(t,n,i):
    if i==0:
        k = 1
    else:
        k = 0
    
    for j in range(n):
        if j!=i and orient(t,i,j,k) > 0:
            k = j
    return k


def Jarvis_march(points):
    n = len(points[0])
    l = [min_point(points,n)]
    j = nextPoint(points,n,l[0])
    
    while j != l[0]:        
        l.append(j)
        j = nextPoint(points,n,l[-1])
    
    return l


def draw(points):
    # Draw cloud
    plt.scatter(points[0],points[1])
    
    env = Jarvis_march(points)
    x = []
    y = []
    for i in env:
        x.append(points[0][i])
        y.append(points[1][i])
    
    n = len(env)
    for i in range(n-1):
        plt.plot([x[i],x[i+1]], [y[i],y[i+1]])
            
    print("Points list:",points)
    print("Convex hull:",env)
    
    # First and last points
    plt.plot([x[-1],x[0]], [y[-1],y[0]])


def random_points(n,x,y):
    a = []
    b = []
    l = []
    for i in range(n):
        u = randint(-x,x) #random()*2*x-x
        v = randint(-y,y) #random()*2*y-y
        
        # If new point doesn't exist already
        if l.count([u,v]) == 0:
            l.append([u,v])
            a.append(u);
            b.append(v);
        else:
            i = i-1
    
    return [a,b]


a=10
points = random_points(20,a,a)
draw(points)
