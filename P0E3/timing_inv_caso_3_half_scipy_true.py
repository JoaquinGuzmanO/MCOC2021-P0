from time import perf_counter
from numpy import zeros
from scipy.linalg import inv
from Laplaciana import laplaciana
from numpy import float16, float32 , float64, longdouble

#Tamaño
for i in range(1,11):
	text = open("rendimiento_scipy_true_float16_"+str(i)+".txt","w") # cambiar nombre

	ns= [5,10,20,50,100,200,500,1000,2000,5000]

	for N in ns:

		A = laplaciana(N, dtype = float16) # hay que variar los float

		t1 = perf_counter()
		Am1 = inv(A, overwrite_a=True) #variar la funcion con la que invertir
		t2 = perf_counter()
		dt = t2-t1
		uso_memoria_t = A.nbytes+Am1.nbytes
		print(f"dt = {dt} s ; uso_memoria_t = {uso_memoria_t} bytes")
		text.write(f"{N} {dt} {uso_memoria_t}\n")

text.close()