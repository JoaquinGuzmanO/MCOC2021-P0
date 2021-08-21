import matplotlib.pylab as plt

			  ##############################
			          #Eight Caso 1#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso1/rendimiento_EDC1.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso1/rendimiento_EFC1.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 1 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

 			  ##############################
			 #Eight Caso 2 overwrite_a=False#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso2/rendimiento_EDfC2.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso2/rendimiento_EFfC2.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 2 overwrit_a=False[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 #Eight Caso 2 overwrite_a=True#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso2/rendimiento_EDtC2.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso2/rendimiento_EFtC2.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 2 overwrit_a=True[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

 			  ##############################
			 #Eight Caso 3 overwrite_a=False#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso3/rendimiento_EDfC3.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso3/rendimiento_EFfC3.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 3 overwrit_a=False[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 #Eight Caso 3 overwrite_a=True#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso3/rendimiento_EDtC3.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso3/rendimiento_EFtC3.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 3 overwrit_a=True[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

 			  ##############################
			 #Eight Caso 4 overwrite_a=False#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso4/rendimiento_EDfC4.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso4/rendimiento_EFfC4.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 4 overwrit_a=False[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 #Eight Caso 4 overwrite_a=True#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso4/rendimiento_EDtC4.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso4/rendimiento_EFtC4.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 4 overwrit_a=True[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

 			  ##############################
			 #Eight Caso 5 overwrite_a=False#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso5/rendimiento_EDfC5.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso5/rendimiento_EFfC5.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 5 overwrit_a=False[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 #Eight Caso 5 overwrite_a=True#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Eigh_double_Caso5/rendimiento_EDtC5.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Eigh_float_Caso5/rendimiento_EFtC5.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Eight Caso 5 overwrit_a=True[double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 1#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso1/rendimiento_SDC1.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso1/rendimiento_SFC1.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 1 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 2#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso2/rendimiento_SDC2.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso2/rendimiento_SFC2.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 2 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 3#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso3/rendimiento_SDC3.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso3/rendimiento_SFC3.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 3 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 4#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso4/rendimiento_SDC4.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso4/rendimiento_SFC4.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 4 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 5#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso5/rendimiento_SDC5.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso5/rendimiento_SFC5.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 5 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 6#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso6/rendimiento_SDC6.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso6/rendimiento_SFC6.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 6 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()

			  ##############################
			 	     #Solve Caso 7#
			  ##############################

ns = []
dts1 = []
dts2 = []

#Lectura de archivos

n = []
dt = []
text = open("Solve_double_Caso7/rendimiento_SDC7.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	n.append(int(sl[0]))
	dt.append(float(sl[1]))
		
ns.append(n)
dts1.append(dt)

text.close()

dt = []
text = open("Solve_float_Caso7/rendimiento_SFC7.txt","r") # cambiar aca!
for line in text:
	sl = line.split()
	dt.append(float(sl[1]))
dts2.append(dt)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

# Graficar figura

plt.title("Rendimiento Solve Caso 7 [double vs float]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.xlabel("Tamaño de N")
plt.loglog(ns[0],dts1[0],marker="o")
plt.loglog(ns[0],dts2[0],marker="o")
plt.yticks(dy1,ly1)
plt.legend(["double","float"])
plt.show()