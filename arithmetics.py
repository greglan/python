from math import *

## Basics
def divisorsList(n):
	""" Returns the list of divisors of n """
	return [d for d in range(1, n//2 +1) if n%d==0]+[n];

def oddList(n):
	""" Returns the list of n first odd numbers """
	return [2*k-1 for k in range(1,n+1)];
	
def evenList(n):
	""" Returns the list of n first even numbers"""
	return [2*k for k in range(0,n)];

def isPrime(n):	
	if n==2:
		return True
	elif n==0 or n==1 or n%2==0:
		return False
	else:
		i = 3
		while (i <= int(sqrt(n))):
			if n%i==0:
				return False
			i+=2
		return True

def isPerfect(n):
	return sum(divisorsList(n))-n == n;

##
# Retourne la liste des entiers compris entre a et b non-multiples de p
def non_multiples(a, b, p):
	return [k for k in range(a,b+1) if k%p != 0];

def prime_factors(n):
	l = []
	i=2
	while i <= n:
		if n%i==0:
			l.append(i)
			n = n / i
		i+=1
	return l

## PGCD
def pgcd_rec(a,b):
	if b==0:
		return a;
	else:
		return pgcd_recursif(b,a%b);

def pgcd(a,b):
	while (b > 0):
		a,b = b,a%b;
	return a;
	
def euclide_extended_rec(a,b):
	if b == 0:
		return(a,1,0)
	else:
		q,r = divmod(a,b)
		d,u,v = etendu(b,r)
		return(d,v,u-q*v)

def euclide_extended(a0,b0): # invariant : a0*u + b0*v = a et a0*x + b0*y = b
	a, u, v, b, x, y = a0, 1, 0, b0, 0, 1
	while b != 0:
		q, r = divmod(a, b)
		a, u, v, b, x, y = b, x, y, r, u - x*q, v - y*q
	return(a,u,v)