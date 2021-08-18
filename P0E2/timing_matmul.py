from numpy import zeros
from time import perf_counter



#Tamaño
for i in range(1,11):
	text = open("rendimiento_"+str(i)+".txt","w")

	ns= [5,10,20,50,100,200,500,1000,2000,5000]

	for N in ns:

		A = zeros((N, N))+1
		B = zeros((N, N))+2


		t1 = perf_counter()
		C = A@B
		t2 = perf_counter()


		dt = t2 - t1
		uso_memoria_t = A.nbytes + B.nbytes + C.nbytes

		print(f"dt = {dt} s ; uso_memoria_t = {uso_memoria_t} bytes")
		text.write(f"{N} {dt} {uso_memoria_t}\n")

text.close()