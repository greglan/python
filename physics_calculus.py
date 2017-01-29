from math import log,cos,sin,pi

def degToRad(d):
    return pi*d/180

def radToDeg(d):
    return d*180/pi

def kmhToms(v):
    return v/3.6

def intTodB(x):
    return 10*log(x,10)
    
def dBToInt(x):
    return 10**(x/10)

def intTodBm(x):
    return 10*log(x*10**3,10)

def dBmtoInt(x):
    return 10**(x/10-3)

def doppler(f, v, c):
    return abs(f-f/(1-v/c))

c=3*10**8