# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:14:38 2023

@author: jdavi
"""

"""
Pilas , colas 
"""
def aplicarPila2():
    res =  input('Quierres eliminar un elemento?/n')
    if res == 'SI' or res == 'si':
        a.pop(len(a)-1)
        print(a)
        return aplicarPila2()
    else:
        print(a)

    

def aplicarPila():
    a.pop(len(a)-1)
    res = input('Quieres eliminar otro?\n')
    if res == 'SI' or res == 'si':
        return aplicarPila()
    else:
        print(a)


def pilas():
    a.append(int(input('Escribe un numero\n')))
    res = input("Quieres otro numero?\n")
    if res == 'SI' or res == 'si':
        return pilas()
    else:
        print(a)
        aplicarPila() #metodo 
        
    
    


a = []
if __name__ == "__main__":
        pilas()
    