def agregarLista(a):
   a.append(int(input('Escribe un numero\n')))



def menu(a):
    print('1.- Agregar')
    print('2.- Eliminar con pilas')
    print('3.- Eliminar con colas')
    print('4.- Mostrar lista')
    print('5.- Salir')
    opt = int(input('Elige una opcion\n'))
    
    if opt == 1:
        agregarLista(a)
        return menu(a)
    
    if opt == 4:
        print(a)
    
    if opt == 2:
        aplicarPila(a)
    
    if opt == 3:
        eliminarCola(a)
    
    if opt != 5:
        return menu(a)

def aplicarPila(a):
    res = input('Quieres eliminar un elemento?\n')
    if res == 'SI' or res == 'si':
        a.pop(len(a)-1)
        print(a)
        return aplicarPila(a)
    else:
        print(a)


def eliminarCola(a):
    res = input('Quieres eliminar otro?\n')
    if res == 'SI' or res == 'si':
        a.pop(0)
        return eliminarCola(a)
    else:
        print(a)

if __name__ == "__main__":
    a = []
    menu(a)
