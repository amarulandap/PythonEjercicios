# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 11:09:04 2021

@author: Andres Marulanda
"""

"""EJERCICIOS CON LISTAS Y VECTORES - FUNCIONES"""

import random

"""1. programa para determinar que articulos se pueden comprar"""

dinero_dispo = int(input("Ingrese la cantidad de dinero disponible: "))
num_articulos = int(input("Ingrese el número de articulos: "))
vec_precios = [0] * num_articulos

vec_precios = [random.randint (10000, 100000) for i in range(num_articulos)]

for i in range(num_articulos):
    if vec_precios[i] <= dinero_dispo:
        puede_comprar = dinero_dispo // vec_precios[i]
        
        print(f'Puede comprar {puede_comprar} unidades del articulo en la posición {i}')
        
        
"""2. programa para determinar el rango de los pesos de los articulos de una bodega"""

num_art_bodega = int(input("Ingrese el número de articulos en bodega: "))

vec_pesos = [] * num_art_bodega

for i in range(num_art_bodega):
    peso_art_bod = float(input("Ingrese el peso del articulo: "))
    vec_pesos.append(peso_art_bod)

vec_pesos.sort()
print(f'El rango de pesos va desde {vec_pesos[0]} hasta {vec_pesos[num_art_bodega-1]}')


"""3. programa para asignar un paquete a un inspector"""

num_paquetes = int(input("Ingrese el número de paquetes: "))
num_inspectores = num_paquetes

vec_paquetes = [] * num_paquetes
vec_inspectores = [] * num_inspectores

vec_paquetes = [i for i in range (num_paquetes)]
vec_inspectores = [j for j in range(num_inspectores)]

vec_parejas = list(zip(vec_paquetes, vec_inspectores))
print(vec_parejas)


"""4. Programa para eliminar de un vector todos los números menor a uno generado aleatoriamente"""

cant_num = int(input("Ingrese el tamaño del vector: "))
vec_num_one = [0] * cant_num
num_aleatorio = 0
vec_num_mayor = []

for i in range(cant_num):
    vec_num_one[i] = random.randint(0, 9)
    
print(vec_num_one)
    
num_aleatorio = random.randint(0, 9)

for i in range(cant_num):
    if vec_num_one[i] > num_aleatorio:
        vec_num_mayor.append(vec_num_one[i])
        
print(vec_num_mayor)


"""5. programa para determinar el número de cajas a ser inspeccionadas"""

bodega_1 = int(input("Ingrese el número de cajas de la bodega 1: "))
bodega_2 = int(input("Ingrese el número de cajas de la bodega 2: "))
codigos = int(input("Ingrese el número de codigos a inspeccionar: "))

cod_inspeccionar = [0] * codigos
cajas_inspeccionar_1 = 0
cajas_inspeccionar_2 = 0

cod_bodega_1 = [random.randint(1, 10) for i in range(bodega_1)]
cod_bodega_2 = [random.randint(1, 10) for i in range(bodega_2)]

for i in range(0, codigos):
    cod_inspeccionar[i] = int(input("Código: "))
    
i = 0
while i < codigos:
    cod = cod_inspeccionar[i]
    
    for j in range(bodega_1):
        if cod_bodega_1[j] == cod:
            cajas_inspeccionar_1 += 1
    
    for j in range(bodega_2):
        if cod_bodega_2[j] == cod:
            cajas_inspeccionar_2 += 1
            
    i += 1

print("El total de cajas a inspeccionar en la bodega 1 es: ",cajas_inspeccionar_1) 
print("El total de cajas a inspeccionar en la bodega 2 es: ",cajas_inspeccionar_2)   
print("El total de las cajas a inspeccionar es: ",cajas_inspeccionar_1 + cajas_inspeccionar_2)


"""6. programa competencia de salto rana"""

num_ranas = int(input("Ingrese el número de ranas: "))
vec_saltos = [0] * num_ranas
vec_acum_saltos = [0] * num_ranas
distancia_pista = float(input("Ingrese el largo de la pista: "))

distancia_inicial = 0
saltos = 0
while distancia_inicial < distancia_pista:
    #vector de distancia alcanzada en cada uno de los saltos
    vec_acum_saltos = [random.randint(0,2) for i in range(num_ranas)]
    
    for j in range(num_ranas):
        vec_saltos[j] += vec_acum_saltos[j]
        
    for j_1 in range(num_ranas):
        if vec_saltos[j_1] >= distancia_pista:
            rana_ganadora = j_1
            distancia_inicial = distancia_pista
            break
        else:
            distancia_inicial = 0
            
    saltos += 1
            
print(f'La rana {rana_ganadora} es la ganadora, después de {saltos} saltos')
















        

        


    







  

    
            
            
    






