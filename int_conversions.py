from math import floor


def formatBin(x):
    """ Add bits to get a byte and add spaces every 4 digits """
    n = len(x)
    r = n % 8
    if r!=0:
        k = 8-r
        s = k*'0'+x
    else:
        s = x
    s = ' '.join(s[i:i+4] for i in range(0,len(s),4))
    return s

def formatHex(x):
    """ Add bits to get a byte and add spaces every 4 digits """
    n = len(x)
    r = n % 4
    if r!=0:
        k = 4-r
        s = k*'0'+x
    else:
        s = x
    s = s[::-1]
    s = ' '.join(s[i:i+4] for i in range(0,len(s),4))
    s = s[::-1]
    return s

def toBin(x):
    if type(x)==int:
        return twoComplement(x)

def twoComplement(x):
    """ Not fully working """
    s = bin(x)
    
    if x>=0:
        return '0b'+formatBin(s[2:])
    else:
        # Strip '-' char
        s = s[3:]
        
        # Add missing bits
        n = len(s)
        r = n%4
        if r != 0:
            s = (4-r)*'0'+s
        
        print(s)

        # Logical not
        s=logicalNot(s)
        print(s)

        s = int(s,2) + 1
        print(bin(s))
        return '0b'+formatBin(bin(s)[2:])

def logicalNot(s):
    ss = ''
    for c in s:
        if c == '0':
            ss += '1'
        else:
            ss += '0'
    return ss

def toHex(x):
    if type(x)==int:
        if x>=0:
            s = hex(x)
            return '0x'+formatHex(s[2:])

def fromHex(n):
    if type(n)==int:
        if n>=0:
            return n