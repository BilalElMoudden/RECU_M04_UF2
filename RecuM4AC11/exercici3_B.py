def verificar_declaracion():
    # Preguntar al usuario que ponga su edad y sus ingresos mensuales
    edad = int(input("Pon tu edad: "))
    ingresos = float(input("Indica tus ingresos mensuales: "))

    # Comprobar si cumple la condición para hacer la declaración de Hacienda
    if edad >= 18 and ingresos > 1200:
        print("Tienes que hacer la declaración de Hacienda.")
    else:
        print("Aún no puedes hacer la declaración de Hacienda.")

# Llamar a la función
verificar_declaracion()
