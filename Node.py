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
	return 1/(1+math.exp(-x))

#derivatives of the sigmoids respectively	
def dsigmoidTanh(y):
	return 1.0 - y**2

def dsigmoidStandard(y):
	return sigmoidStandard(y)*(1-sigmoidStandard(y))


class NN:
	def __init__(self,ni,nh,no):
		#number of inputs,hidden nodes, output nodes
		self.ni=ni+1 #+1 for bias node, it has been added
		#in the example code so I will keep it but I am not sure why
		#it is necessary
		self.nh = nh
		self.no = no


		#activations for nodes
		self.ai = [1.0]*self.ni
		self.ah = [1.0]*self.nh
		self.ao = [1.0]*self.no


		#weights
		self.wi = makeMatrix(self.ni, self.nh)
		self.wo = makeMatrix(self.nh, self.no)

		#setting the weight to random values
		for i in range(self.ni):
			for j in range(self.nh):
				self.wi[i][j] = rand(-1.0,1.0)
		for j in range(self.nh):
			for k in range(self.no):
				self.wo[j][k] = rand(-2.0,2.0)

		#last change in weight for moementum???
		#no exactly sure what this means
		self.ci = makeMatrix(self.ni, self.nh)
		self.co = makeMatrix(self.nh, self.no)

	def update(self,inputs):
		if len(inputs) != self.ni-1:
			raise ValueError("Wrong number of inputs")

		#input activations
		for i in range(self.ni-1):
			self.ai[i] = inputs[i]
		print "Activation inputs",self.ai

		#hidden activations
		for j in range(self.nh):
			sum = 0.0
			for i in range(self.ni):
				sum = sum + self.ai[i] * self.wi[i][j]
			self.ah[j] = sigmoidStandard(sum)
		print "Activation hidden",self.ah

		#output activations
		for k in range(self.no):
			sum = 0.0
			for j in range(self.nh):
				sum = sum + self.ah[j] * self.wo[j][k]
		return self.ao[:]

n = NN(1,2,1)
n.update([1])








