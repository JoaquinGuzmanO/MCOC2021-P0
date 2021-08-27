import matplotlib.pylab as plt

					#############################
					##########CONTINUA###########
					#############################

ns = []
dts_e = []
dts_s = []

for i in range (1,11):
	n = []
	dt_e = []
	dt_s = []
	text = open("rendimiento_matriz_llena"+str(i)+".txt","r")
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt_e.append(float(sl[1]))
		dt_s.append(float(sl[2]))
		
	ns.append(n)
	dts_e.append(dt_e)
	dts_s.append(dt_s)

text.close()

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000","10000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento Matrices Continuas")
plt.ylabel("Tiempo de ensamblaje [s]")
plt.loglog(ns[0],dts_e[0],marker="o")
plt.loglog(ns[1],dts_e[1],marker="o")
plt.loglog(ns[2],dts_e[2],marker="o")
plt.loglog(ns[3],dts_e[3],marker="o")
plt.loglog(ns[4],dts_e[4],marker="o")
plt.loglog(ns[5],dts_e[5],marker="o")
plt.loglog(ns[6],dts_e[6],marker="o")
plt.loglog(ns[7],dts_e[7],marker="o")
plt.loglog(ns[8],dts_e[8],marker="o")
plt.loglog(ns[9],dts_e[9],marker="o")

plt.loglog(ns[0],[dts_e[0][10]]*11,'--',color="b",label="constante")

plt.yticks(dy1,ly1)

plt.subplot(2,1,2)
plt.ylabel("Tiempo de solución [s]")
plt.loglog(ns[0],dts_s[0],marker="o")
plt.loglog(ns[1],dts_s[1],marker="o")
plt.loglog(ns[2],dts_s[2],marker="o")
plt.loglog(ns[3],dts_s[3],marker="o")
plt.loglog(ns[4],dts_s[4],marker="o")
plt.loglog(ns[5],dts_s[5],marker="o")
plt.loglog(ns[6],dts_s[6],marker="o")
plt.loglog(ns[7],dts_s[7],marker="o")
plt.loglog(ns[8],dts_s[8],marker="o")
plt.loglog(ns[9],dts_s[9],marker="o")

plt.loglog(ns[0],[dts_s[0][10]]*11,'--',color="b",label="constante")

plt.yticks(dy1,ly1)
plt.xticks(ns[0],lx,rotation=45)
plt.show()

					#############################
					##########DISPERSA###########
					#############################

ns = []
dts_e = []
dts_s = []

for i in range (1,11):
	n = []
	dt_e = []
	dt_s = []
	text = open("rendimiento_matriz_dispersa"+str(i)+".txt","r")
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt_e.append(float(sl[1]))
		dt_s.append(float(sl[2]))
		
	ns.append(n)
	dts_e.append(dt_e)
	dts_s.append(dt_s)

text.close()

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","50","100","500","1000","5000","10000","500000","100000","500000","1000000","5000000","10000000","50000000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento Matrices Dispersas")
plt.ylabel("Tiempo de ensamblaje [s]")
plt.loglog(ns[0],dts_e[0],marker="o")
plt.loglog(ns[1],dts_e[1],marker="o")
plt.loglog(ns[2],dts_e[2],marker="o")
plt.loglog(ns[3],dts_e[3],marker="o")
plt.loglog(ns[4],dts_e[4],marker="o")
plt.loglog(ns[5],dts_e[5],marker="o")
plt.loglog(ns[6],dts_e[6],marker="o")
plt.loglog(ns[7],dts_e[7],marker="o")
plt.loglog(ns[8],dts_e[8],marker="o")
plt.loglog(ns[9],dts_e[9],marker="o")

plt.loglog(ns[0],[dts_e[0][14]]*15,'--',color="b",label="constante")

plt.yticks(dy1,ly1)

plt.subplot(2,1,2)
plt.ylabel("Tiempo de solución [s]")
plt.loglog(ns[0],dts_s[0],marker="o")
plt.loglog(ns[1],dts_s[1],marker="o")
plt.loglog(ns[2],dts_s[2],marker="o")
plt.loglog(ns[3],dts_s[3],marker="o")
plt.loglog(ns[4],dts_s[4],marker="o")
plt.loglog(ns[5],dts_s[5],marker="o")
plt.loglog(ns[6],dts_s[6],marker="o")
plt.loglog(ns[7],dts_s[7],marker="o")
plt.loglog(ns[8],dts_s[8],marker="o")
plt.loglog(ns[9],dts_s[9],marker="o")

plt.loglog(ns[0],[dts_s[0][14]]*15,'--',color="b",label="constante")

plt.yticks(dy1,ly1)
plt.xticks(ns[0],lx,rotation=45)
plt.show()
