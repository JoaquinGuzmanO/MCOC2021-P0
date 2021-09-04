import numpy as np 
import scipy.sparse.linalg as lin
import scipy.sparse as sparse
from time import perf_counter

def matriz_laplaciana(N, t=np.double):
	return sparse.eye(N,dtype=t)-sparse.eye(N,N,1,dtype=t)

tiempos=[]
promedios=[]
text = open("rendimiento_solve_dispersa.txt","w")

for i in range(1,11): #  corro 10 veces el solve
	ns= [2,5,10,20,50,100,500,1000,10000,100000,500000,1000000,5000000,10000000]
	t = []
	for N in ns:
		A = matriz_laplaciana(N) 
		b = np.ones(N)
		t1 = perf_counter()
		solution = lin.spsolve(A,b) 
		t2 = perf_counter()
		dt = t2-t1
		t.append(dt)	
	tiempos.append(t)

for i in range(len(tiempos[0])): #calculo promedios
	suma = 0
	for j in range(len(tiempos)):
		suma += tiempos[j][i]
	promedios.append(suma/len(tiempos[0]))

for i in range(len(promedios)): #escribo archivos
	text.write(f"{ns[i]} {promedios[i]} \n") 
	print(f"{ns[i]} {promedios[i]} \n")
text.close()