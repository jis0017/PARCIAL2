# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:16:30 2023

@author: jdavi
"""

    

def aplicarcola():
    res = input('Quieres eliminar otro?\n')
    if res == 'SI' or res == 'si':
        a.pop(0)
        return aplicarcola()
    else:
        print(a)


def colas():
    a.append(int(input('Escribe un numero\n')))
    res = input("Quieres otro numero?\n")
    if res == 'SI' or res == 'si':
        return colas()
    else:
        print(a)
        aplicarcola() #metodo 
        
    
    


a = []
if __name__ == "__main__":
        colas()
    