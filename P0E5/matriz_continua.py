import numpy as np
import scipy.sparse as sparse
from time import perf_counter

def laplaciana(N,t= np.double):
	e = np.eye(N)-np.eye(N,N,1)
	return t(e+e.T)

for i in range(1,11):
	text = open("rendimiento_matriz_llena"+str(i)+".txt","w")

	ns= [5,10,20,50,100,200,500,1000,2000,5000,10000]

	for N in ns:

		t1 = perf_counter()
		A = laplaciana(N)
		B = laplaciana(N)
		t2 = perf_counter()
		C = A@B
		t3 = perf_counter()

		dt_e = t2 - t1
		dt_s = t3 - t2

		print(f"N = {N} dt_ensamblaje = {dt_e} s ; dt_solucion = {dt_s} s")
		text.write(f"{N} {dt_e} {dt_s}\n")
	

text.close()