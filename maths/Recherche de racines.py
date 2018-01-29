from math import sqrt

f = lambda x: x**2 - 2
df = lambda x: 2*x

h = 10**-12
a = 1
b = 2

def dicho(a,b):
    i = 0
    while abs(b-a) > h:
        i += 1
        c = (a+b)/2
        if f(c) > 0:
            b = c
        else:
            a = c
    return (b+a)/2, i

def newton():
    i = 0
    a = 2
    while abs(a - sqrt(2))>h:
        i += 1
        a = a - f(a)/df(a)
    return a,i

#print(dicho(a,b), newton())

def recherche_dico(l,a):
    n = len(l)
    if n==1:
        return l[0] == a            
    else:
        if l[n//2] > a:
            return recherche_dico(l[:n//2], a)
        else:
            return recherche_dico(l[n//2:], a)

def rec_dico(l,a):
    n = len(l)
    while n>1:
        if l[n//2] > a:
            l = l[:n//2]
        else:
            l = l[n//2:]
        n = len(l)
    return l[0]==a