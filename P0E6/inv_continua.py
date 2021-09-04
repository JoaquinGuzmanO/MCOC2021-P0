import numpy as np 
from time import perf_counter

def matriz_laplaciana(N, t=np.double):
	e = np.eye(N)-np.eye(N,N,1)
	return t(e+e.T)

tiempos=[]
promedios=[]
text = open("rendimiento_inv_continua.txt","w")

for i in range(1,11):
	ns= [2,5,10,20,50,100,500,1000,5000,6000]
	t = []
	for N in ns:
		A = matriz_laplaciana(N)
		t1 = perf_counter()
		inv = np.linalg.inv(A)                          
		t2 = perf_counter()
		dt = t2-t1
		t.append(dt)	
	tiempos.append(t)

for i in range(len(tiempos[0])):
	suma = 0
	for j in range(len(tiempos)):
		suma += tiempos[j][i]
	promedios.append(suma/len(tiempos[0]))

print("Promedios por N")
for i in range(len(promedios)):
	text.write(f"{ns[i]} {promedios[i]} \n")
	print(f"{ns[i]} {promedios[i]} \n")
text.close()