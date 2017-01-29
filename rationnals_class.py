def pgcd(a, b):
    u = a;
    v = abs(b);
    while (v != 0):
        r = u%v;
        u = v;
        v = r;
    return u;


from math import floor;

class ratio(object):
    def __init__(self, p, q = 1):
        if q == 0:
            raise(ArithmeticError);
        d = pgcd(p, q);
        self.numer = p // d;
        self.denom = q // d;
        if q < 0:
            self.numer = - self.numer;
            self.denom = - self.denom;
    
    def __repr__(self):
        return str(self.numer)+" / "+str(self.denom);
    
    def __float__(self):
        return self.numer / self.denom;
    
    def __add__(self, other):
        if isinstance(other, ratio):
            return ratio( self.numer * other.denom + self.denom * other.numer, self.denom * other.denom);
        elif isinstance(other, int):
            return ratio( self.denom * other + self.numer, self.denom);
        else:
            return NotImplemented;
            
    def __radd__(self, other):
        return ratio( self.denom * other + self.numer, self.denom);
    
    def __sub__(self, other):
        if isinstance(other, ratio):
            return ratio( self.numer * other.denom - self.denom * other.numer, self.denom * other.denom);
        elif isinstance(other, int):
            return ratio( self.numer -  self.denom * other, self.denom);
        else:
            return NotImplemented;
        
    def __rsub__(self, other):
        return ratio( self.denom * other - self.numer, self.denom);

            
    def __neg__(self):
        return ratio( -self.numer, self.denom);
    
    def __mul__(self, other):
        if isinstance(other, ratio):
            return ratio( self.numer * other.numer, self.denom * other.denom);
        elif isinstance(other, int):
            return ratio( self.numer * other, self.denom);
        else:
            return NotImplemented;
    
    def __rmul__(self, other):
        return ratio( self.numer * other, self.denom);
    
    def __truediv__(self, other):
        if isinstance(other, ratio):
            return ratio( self.numer * other.denom, self.denom * other.numer);
        elif isinstance(other, int):
            return ratio( self.numer, self.denom * other);
        else:
            return NotImplemented;
            
    def __rtruediv__(self, other):
        return ratio( self.numer, self.denom * other);
    
    def __lt__(self, other):
        return (self - other).numer < 0;
    
    def __le__(self, other):
        return (self - other).numer <= 0;
    
    def __gt__(self, other):
        return (self - other).numer > 0;
    
    def __ge__(self, other):
        return (self - other).numer >= 0;
    
    def __eq__(self, other):
        return (self - other).numer == 0;
        
        
    def dd(self, n): #Développement décimal à n chiffres après la virgule
        temp = str( float(self) );
        return temp[:n + len( str( floor( float(temp) ) ) ) + 1];
    

def listToStr(l):
    s = "";
    for x in l:
        s+= str(x);
    return s;

def nbrChiffres(x):
    if type(x) == type("string"):
        return len( str(x) ) - 1;
    else:
        return len( str(x) );
    
def toRatio(l):
    return ratio( float(listToStr(l))*nbrChiffres( float(listToStr(l)) ), nbrChiffres(float(listToStr(l))) );