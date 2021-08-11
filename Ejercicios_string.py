# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:54:53 2021

@author: Andres Marulanda
"""

"""EJERCICIOS CADENAS DE CARACTERES"""

"""1. programa para contar vocales y buscar palabras en una frase

Método alternativo:
a = frase.count('a') a_1 = frase.count('á') e = frase.count('e') e_1 = frase.count('é')
i = frase.count('i') i_1 = frase.count('í') o = frase.count('o') o_1 = frase.count('ó')
u = frase.count('u') u_1 = frase.count('ú')


frase = input("Ingrese una frase: ").lower()
palabra = input("Ingrese la palabra a buscar: ")

buscar_palabra = palabra in frase
if buscar_palabra:
    print(f'La palabra {palabra} si está en la frase')
else:
    print(f'La palabra {palabra} no está en la frase')
    
a = 0
e = 0
i = 0
o = 0
u = 0
for i_1 in frase:
    if i_1 == 'a' or i_1 == 'á':
        a += 1
        new_frase = frase.replace('a', ' ')
        frase = new_frase
        new_frase = frase.replace('á', ' ')
        frase = new_frase
    elif i_1 == 'e' or i_1 == 'é':
        e += 1
        new_frase = frase.replace('e', ' ')
        frase = new_frase
        new_frase = frase.replace('é', ' ')
        frase = new_frase
    elif i_1 == 'i' or i_1 == 'í':
        i += 1
        new_frase = frase.replace('i', ' ')
        frase = new_frase
        new_frase = frase.replace('í', ' ')
        frase = new_frase
    elif i_1 == 'o' or i_1 == 'ó':
        o += 1
        new_frase = frase.replace('o', ' ')
        frase = new_frase
        new_frase = frase.replace('ó', ' ') 
        frase = new_frase
    elif i_1 == 'u' or i_1 == 'ú':
        u += 1
        new_frase = frase.replace('u', ' ')
        frase = new_frase
        new_frase = frase.replace('ú', ' ')
        frase = new_frase

total_vocales = a + e + i + o + u  
print(f'El total de vocales es: {a} a, {e} e, {i} i ,{o} o, {u} u = {total_vocales} vocales')
print("\nFrase sin vocales: ",new_frase)"""


"""2. Programa para enmascarar vocales

frase_1 = input("Ingrese la frase: ").upper()

for i_2 in frase_1:
    if i_2 == 'A':
        new_frase = frase_1.replace('A','*')
        frase_1 = new_frase
    elif i_2 == 'E':
        new_frase = frase_1.replace('E','-')
        frase_1 = new_frase
    elif i_2 == 'I':
        new_frase = frase_1.replace('I','?')
        frase_1 = new_frase
    elif i_2 == 'O':
        new_frase = frase_1.replace('O','&')
        frase_1 = new_frase
    elif i_2 == 'U':
        new_frase = frase_1.replace('U','#')
        frase_1 = new_frase
        

print("\nFrase enmascarada: ",frase_1.lower().capitalize())"""










    





      
      