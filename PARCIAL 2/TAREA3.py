def listas():
    Nombre = validarNombre()
    Edad = validarEdad()
    lista.append([Nombre, Edad])
    promedio = sum(edad for nombre, edad in lista) / len(lista)
    res = input("Deseas otra persona s/n \n")
    if res == "S" or res == "s":
        return listas()
    else:
        for i in lista:
            print(i)
        print(f"El promedio de las edades es: {promedio}")
    res = input("Deseas otra persona s/n \n")
    if res == "S" or res == "s":
        return listas()
    else:
        for i in lista:
            print(i)


def validarNombre():
    c = 0
    a = input("Escribe un nombre con apellidos\n")
    for i in a:
        if (
            (ord(i) >= 97 and ord(i) <= 122)
            or (ord(i) >= 65 and ord(i) <= 90)
            or (ord(i) == 32)
        ):
            c += 1
    if c == len(a):
        return a
    else:
        print("Error... el nombre se escribio mal")
        return validarNombre()


def validarEdad():
    c = 0
    e = input("Escribe la edad de una persona\n")
    for i in e:
        if ord(i) >= 48 and ord(i) <= 57:
            c += 1
    if c == len(e):
        return int(e)
    else:
        print("Error de edad")
        return validarEdad


Nombre = "Nombre completo"

lista = []


if __name__ == "__main__":  # METODO PRINCIPAL
    listas()
