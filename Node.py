import math
import random
import string

#return a number between a and b
def rand(a,b):
	return (b-a)*random.random()+ a

#make a matrix 
def makeMatrix(I,J,fill=0.0):
	m=[]
	for i in range(I):
		m.append([fill]*J)
	return m

