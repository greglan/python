class polynome(object):
    def __init__(self, *a):
        self.coeffs = list(a);

    def __eq__(self, other):
        equal = True;
        n = len(self.coeffs);
        m = len(other.coeffs);
        d = min(n, m);
        i = d;
        equal = (self.coeffs[:d] == other.coeffs[:d]);
        if equal:
            if (n < m):
                while (i < m):
                    if other.coeffs[i] != 0:
                        equal = False
                    i += 1;
            elif (m < n):
                while (i < n):
                    if (self.coeffs[i] != 0):
                        equal = False;
                    i += 1;
        return equal;

    def __repr__(self):
        n = len(self.coeffs);
        res = '';
        k = 0;
        while (k < n):
            while (k < n) and (self.coeffs[k] == 0):
                k += 1;
            if (k < n):
                if (k == 0):
                    res = str(self.coeffs[k]);
                elif (self.coeffs[k] == 1):
                    res = res + ' + X^' + str(k);
                elif (self.coeffs[k] == -1):
                    res = res + ' - X^' + str(k);
                elif (self.coeffs[k] < 0):
                    res = res + ' - ' + str(-self.coeffs[k]) + 'X^' + str(k);
                else:
                    res = res + ' + ' + str(self.coeffs[k]) + 'X^' + str(k);
                k += 1;
            if res == '':
                res = '0';
        return res;

    def __add__(self, other):
        n = len(self.coeffs);
        m = len(other.coeffs);
        l = [];
        if n < m:
            for i in range(0, n):
                l.append(self.coeffs[i] + other.coeffs[i]);
            for i in range(n, m):
                l.append(other.coeffs[i]);
        else:
            for i in range(0, m):
                l.append(self.coeffs[i] + other.coeffs[i]);
            for i in range(m, n):
                l.append(self.coeffs[i]);
        return polynome(*l);

    def __sub__(self, other):
        n = len(self.coeffs);
        m = len(other.coeffs);
        l = [];
        if n < m:
            for i in range(0, n):
                l.append(self.coeffs[i] - other.coeffs[i]);
            for i in range(n, m):
                l.append(-other.coeffs[i]);
        else:
            for i in range(0, m):
                l.append(self.coeffs[i] - other.coeffs[i]);
            for i in range(m, n):
                l.append(self.coeffs[i]);
        return polynome(*l);

    def __rmul__(self, a):
        n = len(self.coeffs);
        l = [];
        for x in self.coeffs:
            l.append(a * x);
        return polynome(*l);
