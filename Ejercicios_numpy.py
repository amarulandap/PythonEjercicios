# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:12:38 2021

@author: Andres Marulanda
"""

"""EJERCICIOS CON NUMPY"""

import numpy as np

def suma_elementos_filas(m_1,n_1):

    mat_1 = np.random.randint(1, 20, size=(m_1,n_1))
    vec_1  = np.empty(m_1)

    vec_1 = mat_1.sum(axis = 1) #Sumar las filas
    
    print("\n",mat_1)
    print("\nVector suma filas: ",vec_1)


def triangulo_pascal(m_1):
    
    mat = np.zeros((m_1,m_1), dtype=np.int32)

    for i in range(0, m_1):
        for j in range(0, i+1):
            if j == 0:
                mat[i,j] = 1
            elif i == j:
                mat[i,j] = 1
            else:
                mat[i,j] = mat[i-1,j-1] + mat[i-1,j]
            
    print("\nTriángulo de pasacal: ")
    print(mat)


def pesos(n_1):
    mat_2 = np.empty((n_1, n_1))

    for i in range(n_1):
        for j in range(n_1):
            mat_2[i,j] = float(input("Ingrese el peso en Kg: "))
        
    print(mat_2)

    for i in range(1, n_1-1):
        for j in range(1, n_1-1):
            peso = mat_2[i,j]
            promedio = (mat_2[i-1,j] + mat_2[i+1,j] + mat_2[i,j-1] + mat_2[i,j+1])/4
        
            if peso > promedio:
                print(f'Peso de {mat_2[i,j]} Kgs es mayor que el promedio de sus cuatro lados')
            else:
                print(f'Peso de {mat_2[i,j]} Kgs es menor o igual que el promedio de sus cuatro lados')


def matriz_dominante(n_2):
#mat = np.array([[20,10,5,4], [30,50,15,25], [48,5,95,84], [1,2,3,4]])
#n_2 = mat.shape[0]
    
    mat = np.random.randint(1, 50, size=(n_2,n_2))
    
    print("\nMatriz Diagonal Dominante: ")
    print(mat)

    vec_mayores = mat.max(axis = 1)
    print("\nMayor valor en cada fila: ",vec_mayores)

    i = 0
    k = 0
    count = 0
    while i < n_2:
        if i >= n_2:
            break
        for j in range(0, n_2):
            if i == j:
                if vec_mayores[k] > mat[i,j]:
                    print("\nNo es un Matriz dominante")
                    i = 4
                    break  
                else:
                    k += 1
                    count += 1
    i += 1
    
    if count == n_2:
        print("\nSi es un Matriz dominante")


def matriz_cuadrado_magico():  
    
    listo = False
    count = 0
    while listo != True:
        mat_1 = np.random.randint(1,9, size=(4,4))
        sum_1 = 0
        sum_2 = 0
        for i in range(0,4):
            for j in range(0,4):
                if i == j:
                    sum_1 += mat_1[i,j]
                elif i+j == 3:
                    sum_2 += mat_1[i,j]
    
        count += 1            
        if sum_1 == sum_2:
            print("\nMatriz cuadrado mágico: ")
            print(mat_1)
            #print("\nNúmero de intentos: ",count)
            listo = True

    return count 
    

m_1 = int(input("Ingrese el número de filas de la matriz: "))
n_1 = int(input("Ingrese el número de columnas de la matriz: "))
n_2 = int(input("Ingrese la dimensión de la matriz: "))

suma_elementos_filas(m_1, n_1)
triangulo_pascal(m_1)
pesos(n_1)
matriz_dominante(n_2)

numero_intentos = matriz_cuadrado_magico()
print("\nNúmero de intentos: ",numero_intentos)





