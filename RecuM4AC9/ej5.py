areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

# Imprimir el segundo
print(areas[1])

# Imprimir el último
print(areas[-1])

# Imprimir el área de la terrassa
print(areas[areas.index("terrassa") + 1])

# Imprimir del primero al tercero
print(areas[:3])

# Imprimir del tercero al ultimo
print(areas[2:])

# Imprimir el total de área de las dos habitaciones
area_habitaciones = areas[areas.index("habitació1") + 1] + areas[areas.index("habitació2") + 1]
print("El total del área de las dos habitaciones es:", area_habitaciones)

# Modificar el área del lavabo e imprimir la nueva lista
areas[areas.index("lavabo") + 1] = 5.0
print("La nueva lista de áreas después de modificar el lavabo:", areas)

# Añadir el área de pati interior y 2.78 a las últimas posiciones e imprimir
areas.append("pati interior")
areas.append(2.78)
print("La nueva lista de áreas después de agregar 'pati interior' y 2.78:", areas)
