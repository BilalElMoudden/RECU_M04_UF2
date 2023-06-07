def comparar_numeros():
    # Pedir al usuario que inserte los números
    num1 = float(input("Inserta el primer número: "))
    num2 = float(input("Inserta el segundo número: "))

    # Comparar los números
    if num1 > num2:
        print("El número", num1, "es el más grande y el número", num2, "es el más pequeño.")
    elif num1 < num2:
        print("El número", num2, "es el más grande y el número", num1, "es el más pequeño.")


# Llamar a la función
comparar_numeros()
