# MCOC2021-P0

# Desempeño de inv

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 

Numpy => solve(A,I) con la idnetidad como I.
Scipy => pivoteo y factorizacion en LU

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 
 
   El paralelismo ayuda en el trabajo de los procesadores, ya que al implementar esta funcion distribuye el trabajo entre todos los procesadores a la vez, por lo que todos trabajan al mismo tiempo, para asi evitar el sobre trabajo de cualquiera de estos. pero de todas formas utiliza el cache primero ya que es memoria a corto plazo para que no acumular memoria.
   
*Es importante notar que que al usar la inversa con numpy, no se puede utilizar float16 ni LongDouble, dado que numpy trabaja con 2048 dijitos por lo que no puede procesarlos sin instalar algo externo.

*Tambien notar que los tiempos de ejecucion fueron mas rapidos con overwrite_a = True, dado que trabaja sobre A, en vez de crear una matriz completamente nueva como lo hace overwtrite_a = False.



# Desempeño MATMUL

![Graficos](https://user-images.githubusercontent.com/62270417/128526810-e252aaa7-3dab-4414-8a6b-9f5e272022f3.png)

* ¿Cómo difiere del gráfico del profesor/ayudante?
  En la primera operación, el tiempo de arranque es significativamente mayor, otra diferencia es que entre la matriz de tamaño 50 a 500 la dispercion de los puntos es menor que en el grafico del enunciado, ademas despues de la matriz 500 los tiempos pasan a variar poco entre corridas.
* ¿A qué se pueden deber las diferencias en cada corrida?
 Al rendimiento de la memoria, en especial en los puntos que difiere más es porque se esta cambiando la memoria utilizada, pasando de trabajar en los registros a hacer la operacion sobre el cache.
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
 esto se debe a que la memoria usada depende de la cantiadad de operaciones que se ejecutan, por lo que siempre sera igual para la misma multiplición de matrices (por el tamaño de estas, independiente de los numeros que estas posean), en cambio el tiempo transcurrido depende de varios factores, cantidad de uso del pc, programas abiertos, ya que se ocupa la memoria para hacer los trabajos, por lo que mientras menos memoria se este usando y mayor sea la capacidad de esta, trabajará en un tiempo menor.
* ¿Qué versión de python está usando?
 3.9
* ¿Qué versión de numpy está usando?
 1.21.1
* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 

![rendimiento](https://user-images.githubusercontent.com/62270417/128532198-ae66b7e1-9a90-44cd-84a6-66894e12ba1f.PNG)

  Se utilizan los 4 procesadores disponibles.

# Mi computador principal

* Marca/modelo: HP 14-bp0xx
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Core i5-7200U
  * Velocidad Base: 2.50 GHz
  * Velocidad Máxima: 2.70 GHz
  * Numero de núcleos: 2 
  * Numero de hilos: 4
  * Arquitectura: x64
  
* Tamaño de las cachés del procesador
  * L1 Data: 2x32KB
  * L1inst Data: 2x32KB
  * L2: 2x256KB
  * L3: 3MB
  
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 1867 MHz
  
* Tarjeta Gráfica
  * Marca / Modelo: AMD Radeon R7 M340
  * Memoria dedicada: 2 GB
  * Resolución: 1366 x 768

  
* Disco 0: 
  * Marca: Kingston
  * Tipo: SSD
  * Tamaño: 224 GB
  * Particiones: 1

  
* Dirección MAC de la tarjeta wifi: B0-52-16-54-4C-C1
* Dirección IP (Interna, del router): 192.168.1.254
* Dirección IP (Externa, del ISP): 181.226.201.125
* Proveedor internet: Telsur.




