#IMPORTAR MÓDULO "RANDOM".
import random

#Establecemos el numero de puntos 
Puntos= int(input("Ingrese el número de puntos :"))
pi11=3.14159265359 #11 decimales  
puntoscirculo= 0 #PUNTOS DENTRO DEL CÍRCULO 
puntoscuadrado= 0 #PUNTOS DENTRO DEL CUADRADO
  
for i in range(Puntos):

    #GENERACIÓN DE PUNTOS
    rand_x= random.uniform(-1, 1)
    rand_y= random.uniform(-1, 1)
  
    #DISTANCIA DE CADA PUNTO DEL ORIGEN
    origen_dist= (rand_x**2 + rand_y**2)**0.5
  
    #COMPROBAR SI EL PUNTO ESTÁ DENTRO DEL CÍRCULO.
    if origen_dist<= 1:
        puntoscirculo+= 1
  
    puntoscuadrado+= 1

    #OBTENCIÓN DEL VALOR DE PI, se hace la equivalencia entre el área del círculo circunscrito en el cuadrado de lado R
    pi = 4* puntoscirculo/ puntoscuadrado

#ESTIMACIÓN FINAL.
print("PI 11 decimales: ", pi11)
print("PI : ", pi)
print('PUNTOS TOTALES: ',puntoscuadrado)
print('ERROR:',(pi-pi11)*100/pi11,'%')
