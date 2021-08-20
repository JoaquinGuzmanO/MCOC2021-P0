from time import perf_counter
from numpy.linalg import inv
from scipy.linalg import eigh, solve
from numpy import double, zeros, eye, ones, float32

def laplaciana(N,tipo):
	e = eye(N)-eye(N,N,1)
	return tipo(e+e.T)

tiempos=[]
promedios=[]
text = open("rendimiento_SFC3.txt","w") #Cambiar nombre

for i in range(1,11):
	ns= [2,5,10,20,50,100,500,1000,2000,5000]
	t = []
	for N in ns:
		A = laplaciana(N, float32) ### hay que variar el tipo de dato
		b = ones(N)
		t1 = perf_counter()
		s = solve(A,b,assume_a="pos") ### cambiarrrr
		t2 = perf_counter()
		dt = t2-t1
		t.append(dt)	
	tiempos.append(t)

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
p10 = 0

for i in tiempos:
	p1 += i[0]
	p2 += i[1]
	p3 += i[2]
	p4 += i[3]
	p5 += i[4]
	p6 += i[5]
	p7 += i[6]
	p8 += i[7]
	p9 += i[8]
	p10 += i[9]

promedios.append(p1/len(tiempos))
promedios.append(p2/len(tiempos))
promedios.append(p3/len(tiempos))
promedios.append(p4/len(tiempos))
promedios.append(p5/len(tiempos))
promedios.append(p6/len(tiempos))
promedios.append(p7/len(tiempos))
promedios.append(p8/len(tiempos))
promedios.append(p9/len(tiempos))
promedios.append(p10/len(tiempos))

for i in range(len(promedios)):
	text.write(f"{ns[i]} {promedios[i]} \n")

text.close()