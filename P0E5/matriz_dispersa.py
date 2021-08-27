import numpy as np
import scipy.sparse as sparse
from time import perf_counter

def matriz_laplaciana(N, t=np.double):
	return sparse.eye(N,dtype=t)-sparse.eye(N,N,1,dtype=t)

for i in range(1,11):
	text = open("rendimiento_matriz_dispersa"+str(i)+".txt","w")

	ns= [5,10,50,100,500,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000,50000000]

	for N in ns:

		t1 = perf_counter()
		A = matriz_laplaciana(N)
		B = matriz_laplaciana(N)
		t2 = perf_counter()
		C = A@B
		t3 = perf_counter()

		dt_e = t2 - t1
		dt_s = t3 - t2

		print(f"N = {N} dt_ensamblaje = {dt_e} s ; dt_solucion = {dt_s} s")
		text.write(f"{N} {dt_e} {dt_s}\n")
	

text.close()