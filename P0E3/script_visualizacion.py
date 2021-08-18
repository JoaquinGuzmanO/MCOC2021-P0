import matplotlib.pylab as plt

			  ##############################
			          #Numpy Single#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_numpy_float32_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Numpy-Single]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			          #Numpy Double#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_numpy_float64_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(2)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Numpy-Double]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			        #Scipy-False Half#
			  ##############################
ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_false_float16_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(3)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_False-Half]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			       #Scipy-False Single#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_false_float32_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(4)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_False-Single]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			       #Scipy-False Double#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_false_float64_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(5)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_False-Double]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			     #Scipy-False LongDouble#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_false_longdouble_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(6)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_False-LongDouble]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()
			  ##############################
			        #Scipy-True Half#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_true_float16_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(7)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_True-Half]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			       #Scipy-True Single#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_true_float32_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(8)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_True-Single]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			       #Scipy-True Double#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_true_float64_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(9)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_True-Double]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()

			  ##############################
			     #Scipy-True LongDouble#
			  ##############################

ns = []
dts = []
mems = []

#Lectura de archivos

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_scipy_true_longdouble_"+str(i)+".txt","r") # cambiar aca!
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

# Informacion de xticks e yticks

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

# Graficar ambas figuras

plt.figure(10)
plt.subplot(2,1,1)
plt.title("Rendimiento inversion matriz [Scipy_True-LongDouble]") #Cambiar aca!!
plt.ylabel("Tiempo transcurrido [s]")
plt.loglog(ns[0],dts[0],marker="o")
plt.loglog(ns[1],dts[1],marker="o")
plt.loglog(ns[2],dts[2],marker="o")
plt.loglog(ns[3],dts[3],marker="o")
plt.loglog(ns[4],dts[4],marker="o")
plt.loglog(ns[5],dts[5],marker="o")
plt.loglog(ns[6],dts[6],marker="o")
plt.loglog(ns[7],dts[7],marker="o")
plt.loglog(ns[8],dts[8],marker="o")
plt.loglog(ns[9],dts[9],marker="o")
plt.yticks(dy1,ly1)


plt.subplot(2,1,2)
plt.ylabel("Uso de memoria [bytes]")
plt.loglog(ns[0],mems[0],marker="o")
plt.plot(ns[0],ram,'--',color="k")
plt.yticks(dy2,ly2)
plt.xticks(ns[0],lx)
plt.show()