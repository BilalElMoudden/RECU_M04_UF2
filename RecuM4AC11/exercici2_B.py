def Es_Par():
    # Preguntar al usuario que indique un número
    num = int(input("Indica un número: "))

    # Mirar si el número es par o impar
    if num % 2 == 0:
        print("El número", num, "es par.")
    else:
        print("El número", num, "es impar.")

# Llamar a la función
Es_Par()
