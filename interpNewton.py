#!-*- coding:utf-8 -*-
from numpy import *
import pylab as pl
class newton:
	"""docstring for newton"""
	def __init__(self, x, y):
		super(newton, self).__init__()
		self.x = x
		self.y = y
		self.c = self.interpolacion()
		
	def signoOp(self, n):
		if n<=0:return "+"
		if n>0: return ""
	def signo(self, n):
		if n<0:return ""
		return "+"

	def interpolacion(self):
		x = self.x
		y = self.y
		n=len(x)
		c=zeros(n)
		c[0]=y[0]
		for k in range(1,n):
			d=x[k]-x[k-1]
			u=c[k-1]
			for i in range(k-2,-1,-1):
				u=u*(x[k]-x[i])+c[i]
				d*=(x[k]-x[i])
			c[k]=(y[k]-u)/d
		return c	

	def evaluacion(self,x0, i=1):
		c = self.c
		x = self.x
		n=len(x)
		if i==n:
			return c[n-1]
		y=self.evaluacion(x0,i+1)*(x0-x[i-1])+c[i-1]
		return y;
	def eval(self, x):
		n = len(x)
		y=zeros(n)
		for i in range(n):
			y[i] = self.evaluacion(x[i])
		return y

	def mostrarPolinomio(self, x,y,c,variable='x'):
		n=len(x)
		p="P("+variable+")="
		#print "+--------------+"
		#print "|  x   |    y  |"
		#print "+--------------+"
		for i in range(n):
			#print "|%5.3g | %5.3g |"%(x[i],y[i])
			p+=self.signo(c[i])
			p+=str(c[i])
			for j in range(0,i):
				p+="("+variable+" "+self.signoOp(x[j])+""+str(-1.0*x[j])+")"
		#print "+--------------+"
		print("\nEl polinomio es:")
		print (p+"\n")

def aleatorios(a, b, n):
	r = zeros(n)
	for i in range(n):
		ran = random.random()
		r[i] = (1.-ran)*a + ran*b
	return r

def chebPuntos(a,b, n):
	n=int(n)
	cheb=zeros(n)
	for j in range(n):
		k = float(j+1)
		cheb[j]=(b+a)/2.+((b-a)/2.)*cos(pi*(2.*k-1.)/(2.*n))
	return cheb

x = chebPuntos(-1, 1, 1e6)
y = sin(1e5*x)
pol = newton(x,y)

t = linspace(0., 1., 1e5)
yy = pol.eval(t)

pl.plot(x,y, '--r', t,yy)
pl.show()





















#2014 - Jesús A. Mejía D.