# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 06:32:26 2021

@author: Andres Marulanda
"""
import math

"""EJERCICIOS DE PROGRAMACIÓN CON CICLOS"""

"""1. Calcular el mayor y el menor peso"""

#variables de entrada
num_paquetes = 0    #n del enunciado
peso_paquete = 0.0

#variables de salida
promedio = 0.0
mayor_peso = 0.0
menor_peso = 0.0

num_paquetes = int(input("Ingrese el número de paquetes: "))

if num_paquetes != 0:
    peso = float(input("Ingrese el peso del paquete en Kgs: "))
    mayor_peso = peso
    menor_peso = peso
    peso_total = peso
    i = 1
    while i < num_paquetes:
        peso = float(input("Ingrese el peso del paquete en Kgs: "))
        peso_total += peso
        
        if peso < menor_peso:
            menor_peso = peso
        else:
            mayor_peso = peso
            
        i += 1
    
    promedio = peso_total / i
    
    print("\nEl peso promedio es: ",promedio, "Kgs")
    print("El peso menor es: ",menor_peso, "Kgs")
    print("El peso mayor es: ",mayor_peso, "Kgs")

else:
    print("La Bodega está vacia")



"""2. Determinar la cantidad de términos en una serie"""

#variable de entrada
x = 0.0

secuencia = 1**2
contador_terminos = 1

x = float(input("Ingrese un numero positivo: "))
i = 2
while secuencia <= x:
    secuencia += i**i
    contador_terminos += 1
    
    i += 1
    
print("El número de términos necesario fue de: ",contador_terminos)


"""3. Determinar el valor aproximado de pi"""

#variable de entrada
cantidad_terminos = 0

#variable de salida
pi = 0.0

cantidad_terminos = int(input("Ingrese la cantidad de términos: "))
secuencia_1 = 1
den = 1
for i in range(2, cantidad_terminos + 1):
    if i % 2 == 0:
        secuencia_1 -= (1 / (i+den))
    else:
        secuencia_1 += (1 / (i+den))
    den += 1
     
pi = 4 * secuencia_1

print("El valor aproximado de pi es: ",pi)


"""4. Distancia de una fabrica a sus puntos de distribución"""

coord_u = 0.0
coord_v = 0.0
coord_x = 0.0
coord_y = 0.0

distancia_mayor = 0.0

coord_u = float(input("Ingrese la primera coordenada de la fabrica: ")) 
coord_v = float(input("Ingrese la segunda coordenada de la fabrica: "))

num_distribuidores = int(input("Ingrese el número de puntos de distribución: "))

for i in range(num_distribuidores):
    coord_x = float(input(f'Ingrese la primera coordenada del distribuidor {i+1}: '))
    
    coord_y = float(input(f'Ingrese la segunda coordenada del distribuidor {i+1}: '))
    
    distancia = math.sqrt((coord_u - coord_x)**2 + (coord_v - coord_y)**2)
    
    if distancia_mayor < distancia:
        distancia_mayor = distancia
        x_mayor = coord_x
        y_mayor = coord_y
        
print("\nla mayor distancia a la fabrica es la de: ", distancia_mayor,
      "de coordenadas (x,y): ",x_mayor, y_mayor)


"""5. Distancia total acumulada al origen"""

distancia_acumulada = 0.0
num_puntos = int(input("Ingrese el número de puntos en el plano: "))  

i = 1
while i <= num_puntos:
    x = float(input(f'Ingrese la coordenada x del punto {i}: '))
    y = float(input(f'Ingrese la coordenada y del punto {i}: '))
    
    dist = math.sqrt(x**2 + y**2)
    distancia_acumulada += dist 
    
    i += 1

print("La distancia acumulada al origen es: ",distancia_acumulada)
                    

"""6. Calcular una sumatoria conjunta para valores de n y m"""

n = int(input("Ingrese el valor de n: ")) 
m = int(input("Ingrese el valor de m: "))

sumatoria = 0
sumatoria_total = 0
j = 1

for i in range(1, n+1):
    sumatoria = (i**2 + j**2 + i*j)
    sumatoria_total += sumatoria 
    j += 1

print("\nLa suma total es: ",sumatoria_total)


"""7. Calcular el cuadrado de un número terminado en 5"""

m_1 = int(input("Ingrese un número entre 1 y 20: "))
numero = 0
cuadrado = 0
decenas = 0
unidades = 0

for i in range (0, m_1):
    numero += 5
    
    if numero <= 100:
        decenas = numero // 10
        unidades = numero - (decenas * 10)
    
    if unidades == 5:
        formula = 10 * decenas * 10 * (decenas + 1) + 25
        cuadrado = numero * numero
            
        if cuadrado == formula:
            print(f'{numero} termina en 5 y cumple con la formula')
    else:
        print(f'{numero} no termina en 5')
                

      
  


        
            
            
            
            

        
        
              
    