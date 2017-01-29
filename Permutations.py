# X 2011
# Permutations: de 0 à n

def estPermutation(t):
    n = len(t)
    occurences = [0 for k in range(n)]
    i=0
    while i<n:
        if t[i] > n or occurences[t[i]] > 1:
            return False
        
        occurences[t[i]] += 1
        
        i += 1
    return True

def composer(t,u):
    return [ t[u[k]] for k in range(len(u))]

def inverser(t):
    n = len(t)
    i = [0 for k in range(n)]
    
    for k in range(n):
        i[t[k]] = k
    
    return i

# Plus petit entier k non-nul tel que t^k = id
def ordre(t):
    n = len(t)
    k = 1
    u = t
    id = [i for i in range(n)]
    
    while u != id:
        k = k + 1
        u = composer(u,t)
    
    return k


# Période d’un indice i pour la permutation t: plus petit entier k non nul tel 
# que t^k (i) = i.
def periode(t,i):
    k = 1
    u = t[i]
    
    while u != i:
        k = k + 1
        u = t[u]
    
    return k


# L’orbite de i pour la permutation t est l’ensemble des indices j tels qu’il 
# existe k avec: t^k (i) = j.
def orbite(t,i):
    u = t[i]
    orbite = []
    
    while u != i:
        orbite.append(u)
        u = t[u]
    
    orbite.append(i)
    return orbite

def estDansOrbite(t,i,j):
    ind = t[i]
    while ind != i and ind != j:
        ind = t[ind]
    return ind == j

# On suppose que t est au moins un permutation. On calcule le nombre d'indices 
# ou t diffère de l'identité.
def estTransposition(t):
    n = len(t)
    indices = []
    
    for i in range(n):
        if t[i] != i:
            indices.append(i)
    
    # Puisqu'il s'agit d'une permutation, les deux indices qui sont différents 
    # sont nécessairement tels que t[i]=j et t[j]=i
    if len(indices)>2:
        return False
    else:
        return True

def orbites(t):
    n = len(t)
    orbites = []
    for i in range(n):
        orbites.append(orbite(t,i))
    
    # On élimine les doublons

def periodes(t):
    n = len(t)
    per = n*[0]
    for indice in range(n):
        if êr[indice] == 0: #On a pas encore déterminé la période
            p = 1
            j = t[indice]
            while j != indice: #Détermine la période
                p+= 1 # p de indice
                j = t[j]
            ind = indie
            for q in range(p): #Recopie la valeur d
                per[ind] = p #Long de l'orbite de 
                ind = t[ind]
    return per
    
def estCycle(t):
    t1 = t[:]
    n ) len(t)
    debut = 0
    while debut < n and t1<(debut<) == debut:
        deb += 1 #Début d'un cycle
    if debut == n:
        return False # t = id
    fixs = len([k for k in range(n) if t[k] == k])
    return n == fixes+ periode(t,debut)

def iter(t, k):
    per = periodes(t)
    n = len(t)
    tpk = n*[-1] #Représente t**k
    for indice in range(n):
        if tpk[indice] == -1:
            P = PER[INDICE]
            EXPOSANT = K % P
            IMAGE = INDICE
            FOR Q in range(exposant):
                image = t[image]    #Calcul de tpk[indice]
            ind = indice
            for q in range(p): #Construction de tpk
                tpk[ind] = image    #Sur l'orbite de indice
                ind = t[ind]
                image = t[image]
    
# Retourne la liste de toutes les permutations de n entiers (0 exclu)
def perm(n):
    if n==1:
        return [[1]]
    else:
        l = perm(n-1)
        q = []
        for p in l: #Pour chaque permutation de longueur n-1
            for k in range(n):
                q.append(p[:k]+[n]+p[k:])
        return q