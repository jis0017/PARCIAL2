
#def ascii():
 #   a = input ('Escribe un dato')
   # for i in a:
     #   if (ord(i)>97 and ord(i)<=122) or ord (i)==32:
       #      print(ord(i))
       # else:
         #   print('no es letra miniscula o espacio en blanco')
    

#if __name__ == "__main__":
   # ascii()
    
# Hacer un programa que mediante un metodo recursivo valide nombre con apellidos
c = 0
def ascii():
    a = input ('Escribe un nombre con apellidos')
    for i in a:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90) or (ord(i)==32):
            c += 1
    if c == len(a):
        print(a)
    else:
        print ('Error... el nombre se escribio mal')
        ascii()
            