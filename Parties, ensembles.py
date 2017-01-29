def card(p):
    n = 0
    for i in p:
        n += 1
    return n

def delta(p,q):
    if p == []:
        return q
    if q == []:
        return p

    a = p[0]
    b = q[0]

    if a == b:
        return (p[1:],q[1:])

    if a < b:
        return [a] + delta(p[1:], q)

    if b < a:
        return [b] + delta(p, q[1:])

def delta(p,q):
    r = []
    n = len(p); m = len(q)
    ind1, ind2 = 0, 0

    while ind1 < n and ind2 < m:
        a = p[ind1]
        b = q[ind2]

        if a < b:
            r.append(a)
            ind1 += 1
        if b < a:
            r.append(b)
            ind2 += 1
        if a == b:
            ind1 += 1
            ind2 += 1
    if ind1 == p:
        r += q[ind2:]
    else:
        r += p[ind1:]

    return r

def test(p,q):
    return delta(p,q)
