from numpy import *
import pylab as pl
class barycentric:
	"""docstring for barycentric"""
	def __init__(self, x, y):
		super(barycentric, self).__init__()
		self.x = x
		self.y = y
		self.n = len(x)
		self.w = self.pesos_baricen()
		
	def pesos_baricen(self):
		w = zeros(self.n)
		for j in range(self.n):
			l = 1.
			for k in range(self.n):
				if k == j:
					continue
				l*=x[j]-x[k]
			w[j] = 1./l
		return w
	
	def p(self, x0):
		nume  = 0.
		denom = 0.
		w = self.w
		for j in range(self.n):
			if x0 == self.x[j]:
				return self.y[j]
			nume  += (w[j]*self.y[j])/(x0-self.x[j])
			denom += (w[j])/(x0-self.x[j])

		return nume/denom
	def eval(self, x):
		n = len(x)
		y=zeros(n)
		for i in range(n):
			y[i] = self.p(x[i])
		return y
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




x = chebPuntos(-1., 1., 1e6)
y = sin(1e5*x)
pol = barycentric(x,y)

t = linspace(0., 1., 1e5)
yy = pol.eval(t)

pl.plot(x,y, '--r', t,yy)
pl.show()

# [Finished in 23.8s]