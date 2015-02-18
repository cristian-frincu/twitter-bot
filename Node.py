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

#the standard way to calculate the sigmoid is the 1/(1+x^-x), but tanh gives a close aprozimation
# and it will chose whichever gives better results
def sigmoidTanh(x):
	return math.tanh(x)

def sigmoidStandard(x):
	return 1/(1+exp(-x))

#derivatives of the sigmoids respectively
def dsigmoidTanh(y):
	return 1.0 - y**2

def dsigmoidStandard(y):
	return sigmoidStandard(y)*(1-sigmoidStandard(y))