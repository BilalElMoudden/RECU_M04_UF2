class University:
    def __init__(self, nombre, ubicacion, año_fundacion, total_estudiantes, facultades, ranking):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.año_fundacion = año_fundacion
        self.total_estudiantes = total_estudiantes
        self.facultades = facultades
        self.ranking = ranking

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_ubicacion(self):
        return self.ubicacion

    def establecer_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def obtener_año_fundacion(self):
        return self.año_fundacion

    def establecer_año_fundacion(self, año_fundacion):
        self.año_fundacion = año_fundacion

    def obtener_total_estudiantes(self):
        return self.total_estudiantes

    def establecer_total_estudiantes(self, total_estudiantes):
        self.total_estudiantes = total_estudiantes

    def obtener_facultades(self):
        return self.facultades

    def establecer_facultades(self, facultades):
        self.facultades = facultades

    def obtener_ranking(self):
        return self.ranking

    def establecer_ranking(self, ranking):
        self.ranking = ranking

    def info(self):
        print("Información de la Universidad:")
        print("Nombre:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Año de Fundación:", self.año_fundacion)
        print("Total de Estudiantes:", self.total_estudiantes)
        print("Facultades:", self.facultades)
        print("Ranking:", self.ranking)


# Crear una instancia de la clase University
universidad = University("Jaume Balmes", "Barcelona", 1939, 687, ["Ingeniería informatica", "Fisica"], 3)

# Mostrar toda la información
universidad.info()
