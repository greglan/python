def DecomposerBase(N,k):
    L = []
    for j in range(N):
        r = k % N
        k = k // N
        L.append(r)
    return L

def DecomposerFact(N,k):
    L = []
    for j in range(N-1,-1,-1):
        q = k // factorial(j)
        k = k % factorial(j)
        L.insert(0,q)
    return L

# Plus efficace
def DecomposerFact(N,k):
    L = []
    for j in range(2, N+1):
        L.append(k % j)
        k = k // j
    return L

# Copie
def retirer(L,j):
    l = []
    for i in range(len(L)):
        if i!=j:
            l.append(L[i])
    return l

def EcrirePermutation(N,k):
    a = DecomposerFact(N,k)
    L = [j for j in range(N)]
    sigma = []
    for j in range(N-1,-1,-1):
        sigma.append(L[a[j]])
        retirer(L, a[j])
    return sigma

def chiffrer(N,k,b):
    sigma = EcrirePermutation(N,k)
    return sigma[b]

def dechiffrer(N, k, b):
    sigma = EcrirePermutation(N,k)
    recip = [0 for j in range(N)]
    for i in range(N):
        recip[sigma[j]] = j
    return recip[b]