import matplotlib.pylab as plt

			  ##############################
			  ########### Solve ############
			  ##############################

ns1 = []
ns2 = []
dts1 = []
dts2 = []

#Lectura de archivos

n1 = []
dt1 = []
text = open("rendimiento_solve_continua.txt","r") 
for line in text:
	sl = line.split()
	n1.append(int(sl[0]))
	dt1.append(float(sl[1]))
		
ns1.append(n1)
dts1.append(dt1)

text.close()

dt2 = []
n2=[]
text = open("rendimiento_solve_dispersa.txt","r") 
for line in text:
	sl = line.split()
	n2.append(int(sl[0]))
	dt2.append(float(sl[1]))
ns2.append(n2)
dts2.append(dt2)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve [Continua vs Dispersa]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns1[0],dts1[0],marker="o")
plt.loglog(ns2[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["Continua","Dispersa"])
plt.show()


			  ##############################
			  ############ Inv #############
			  ##############################

ns1 = []
ns2 = []
dts1 = []
dts2 = []

#Lectura de archivos

n1 = []
dt1 = []
text = open("rendimiento_inv_continua.txt","r") 
for line in text:
	sl = line.split()
	n1.append(int(sl[0]))
	dt1.append(float(sl[1]))
		
ns1.append(n1)
dts1.append(dt1)

text.close()

dt2 = []
n2=[]
text = open("rendimiento_inv_dispersa.txt","r") 
for line in text:
	sl = line.split()
	n2.append(int(sl[0]))
	dt2.append(float(sl[1]))
ns2.append(n2)
dts2.append(dt2)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Inv [Continua vs Dispersa]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns1[0],dts1[0],marker="o")
plt.loglog(ns2[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["Continua","Dispersa"])
plt.show()