"""
Validar precios, que debe de incluir el signo de pesos del 0 al 8 
, solo un punto decimal
mostrar si esta mal el precio ejemplo 45r.23

"""


def validar_precio(precio):
    if precio[0] != "$":
        return False

    try:
        precio = float(precio[1:])
        if precio < 0 or precio > 8:
            return False

        if precio.count(".") != 1:
            return False

        for caracter in precio:
            if not caracter.isdigit():
                return False

        return True
    except ValueError:
        return False


def main():
    precio = input("Ingresa el precio: ")

    if not validar_precio(precio):
        print("El precio ingresado no es válido.")
        return

    print("El precio es válido.")


if __name__ == "__main__":
    main()
