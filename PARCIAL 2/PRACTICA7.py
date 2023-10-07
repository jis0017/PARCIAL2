# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:25:24 2023

@author: jdavi
"""

def agregarLista():
    a.append(int(input('Escribe un numero\n')))


def menu():
    print('1.- Agregar')
    print('2.- Eliminar con pilas')
    print('3.- Elinar con colas')
    print('4.- Mostrar lista')
    print('5.- Salir')
    opt = int(input('Elige una opcion\n'))
    if opt == 1:
        agregarLista()
        return menu ()
    if opt == 4: print(a)
    if opt != 5:
        return menu()
    if opt == 2:
        aplicarPila(a)    
    if opt == 3: 
        eliminarcola(a)


def aplicarPila(a):
    res =  input('Quierres eliminar un elemento?/n')
    if res == 'SI' or res == 'si':
        a.pop(len(a)-1)
        print(a)
        return aplicarPila(a)
    else:
        print(a)






def eliminarcola(a):
    res = input('Quieres eliminar otro?\n')
    if res == 'SI' or res == 'si':
        a.pop(0)
        return eliminarcola(a)
    else:
        print(a)

#tarea implemntar opciones 2, y 3

a = []
if __name__ == "__main__":
        menu()
    