

def main():
    global c
    nombres = input('Escribe un nombre')
    nombre.append(nombres)
    c +=1
    if c>3:
        print("El numero de nombre fueron ",nombre)
    else:
        main()

nombre =[]
global c
c = 0
if __name__ == "__main__":
    main()