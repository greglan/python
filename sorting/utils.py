# -*- coding: utf-8 -*-

from random import randint


def swap(l, i, j):
	"""
		Swap elements at indexes i and j
	"""
	l[i], l[j] = l[j], l[i]


def randomize(l):
	N = len(l)-1
	for i in range(N**2):
		swap(l, randint(0, N), randint(0, N))
	return l


class Complexity(object):
	def __init__(this):
		this.comparisons = 0
		this.swaps = 0
		this.assignements = 0
	
	def increase_comparisons(this, i=1):
		this.comparisons += i
		
	def increase_assignements(this, i=1):
		this.assignements += i
		