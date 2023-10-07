def validarNombre():
    c = 0
    a=input('Escribe Un Nombre con Apellidos: ')
    for i in a:
        if ord(i) >= 90 and ord(i) <= 122 or (ord(i) >= 65 and ord(i) <= 90 or ord(i) == 32 or ord(i) == 165 or ord(i) == 164):
            c +=1
            if c == len(a):
                return a
            else:
                print('Error, el nombre se escribio mal: ')
                return validarNombre()
        
def validarEdad():
    c =0
    e=input('Escribe la edad de una persona: ')
    for  i in e:
        if ord(i)>=48 and ord(i)<=57: #Metodo para validar, codigo ascii.
            c+= 1
        if c==len(e):
            return int(e)
        else:
            print('Error')
            return validarEdad()
           
def listas():#print(nombre[0:3])#Muestra los datos que estan la posicion desde la cero hasta la tres.
    nombre = validarNombre()#Para llenar la lista
    edad = validarEdad()#Llena la lista
    lista.append(nombre)
    lista.append(edad)
    res= input('Deseas introducir a otra persona: ')
    if res =='s' or res =='s':
       return listas()
    else:
       print(lista)
       nombre = 'nombre completo'
       lista=[]

lista = []

if __name__=="__main__":
    listas()
                