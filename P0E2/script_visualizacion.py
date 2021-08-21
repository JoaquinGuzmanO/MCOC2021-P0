import matplotlib.pylab as plt

ns = []
dts = []
mems = []

for i in range (1,11):
	n = []
	dt = []
	mem = []
	text = open("rendimiento_"+str(i)+".txt","r")
	for line in text:
		sl = line.split()
		n.append(int(sl[0]))
		dt.append(float(sl[1]))
		mem.append(int(sl[2]))
		
	ns.append(n)
	dts.append(dt)
	mems.append(mem)

text.close()

ly1 = ["0,1 ms", "1 ms", "10 ms", "0,1 s", "1 s", "10 s", "1 min", "10 min"]
lx = ["5","10","20","50","100","200","500","1000","2000","5000"]
dy1 = [1*10**(-4), 0.001,0.01,0.1,1,10,60,600]

ly2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "16 GB"]
dy2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,16000000000]
ram = [16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000,16000000000]

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
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


print(ns)
print(dts)


