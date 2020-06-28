'''
Tarea 3 
Álvaro Alfaro Miranda 
B70224
Modelos Probabilísticos de Señales y Sistemas

'''
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
#Para mayor facilidad, el documento con los datos, que está en Excel, se trabajará como documento en formato csv (valores separados por comas).
import csv
import pandas as pd            #se usa el paquete panda para leer los datos del archivo csv 
from scipy.optimize import curve_fit

datos=pd.read_csv('xy.csv')  #se lee el documento 


#Se crea una matriz con los registros del archivo para poder utilizar cada dato en los cálculos.  
archivo = 'xy.csv'
matriz_datos = []
with open(archivo) as csvfile:
    dato = csv.reader(csvfile) 
    for lista in dato: # Cada fila es una lista
        matriz_datos.append(lista)

df=pd.DataFrame(datos)

filas=len(matriz_datos) - 1    #numero de filas (sin encabezado)
columnas= len(matriz_datos [0]) - 1  #numero de columnas (sin encabezado)
matriz_num = numpy.zeros((filas, columnas))

for i in range (0, filas):
  for j in range (0,columnas):
    matriz_num [i][j] = float (matriz_datos [i+1][j+1])  

x = numpy.linspace(5, 15, num=filas)
y = numpy.linspace(5, 25, num=columnas)

fx = numpy.sum(matriz_num, axis=1)
fy = numpy.sum(matriz_num, axis=0)

def gaussiana (x, mu, sigma):
  return 1/(numpy.sqrt(2*numpy.pi*sigma**2))*numpy.exp(-(x-mu)**2/(2*sigma**2))


paramX, _ = curve_fit(gaussiana, x, fx)

muX = paramX [0]
sigmaX = paramX [1]

print ("muX =", muX)
print ("sigmaX =", sigmaX)


gaussX = 1/(numpy.sqrt(2*numpy.pi*sigmaX**2))*numpy.exp(-(x-muX)**2/(2*sigmaX**2))

paramY, _ = curve_fit(gaussiana, y, fy)

muY = paramY [0]
sigmaY = paramY [1]

print ("muY =", muY)
print ("sigmaY =", sigmaY)


gaussY = 1/(numpy.sqrt(2*numpy.pi*sigmaY**2))*numpy.exp(-(y-muY)**2/(2*sigmaY**2))


#Correlación
correlacion=0
for a in range (0, len(x)):
  for b in range (0, len(y)):
    correlacion += x[a] * y[b] * matriz_num [a][b]
print ("Correlación =", correlacion)

#Covarianza 
covarianza=0
for c in range (0, len(x)):
  for d in range (0, len(y)):
    covarianza += (x[a] - muX) * (y[b] - muY) * matriz_num [a][b]
print ("Covarianza =", covarianza)

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

s=[1,3,5,6,3,6,5]
d=[1,2,3,6,7,4]
k=[1,2,5,5,4,4,4]

for q in range (0, len(x)):
  for w in range (0, len(y)):
    ax.scatter(x[q], y[w], matriz_num[q][w])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('fx,y(x,y)')

plt.plot (y, gaussY, 'r--', label='Curva de ajuste')

plt.plot (y, fy, label='FDM de X') #FDM: funcion de densidad marginal
plt.xlabel("x")   
plt.ylabel("fx(X)") 
plt.legend(loc="upper right") 
plt.show()