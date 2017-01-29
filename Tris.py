# -*- coding: utf-8 -*-

from random import randint;

## Permutation aléatoire
def perm_al(L):
	n = len(L);
	for k in range(n-1):
		m = randint(k,n-1)
		L[k],L[m] = L[m],L[k]

L = [k for k in range(0,1000)];


## Tri par insertion
# Principe: on insère au fur et à mesure les éléments dans une liste triée
def tri_ins(L):
	n = len(L);
	#t = clock()
	for k in range(1,n):
		a = L[k];
		j = k-1;
		while j >= 0 and L[j] > a:
			L[j+1] = L[j];
			j-=1;
		L[j+1] = a;
	#print(clock()-t)
	return L


## Tri rapide
# Hors place
def tri_rapide(l):
	if l == []:
		return l
	else:
		x = l[0]
		l = l[1:]
		a = [k for k in l if k<x]
		b = [k for k in l if k>x]
		return tri_rapide(a)+[x]+tri_rapide(b)

# En place


## Tri fusion
