class User:
    def __init__(self, nombre, edad, direccion, telefono, email, profesion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.profesion = profesion

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_profesion(self):
        return self.profesion

    def set_profesion(self, profesion):
        self.profesion = profesion

    def saludo(self):
        print("Información del Usuario:")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Dirección:", self.direccion)
        print("Teléfono:", self.telefono)
        print("Email:", self.email)
        print("Profesión:", self.profesion)


# Crear una instancia de la clase User
usuario = User("Bilal", 30, "Pau Claris 21", "183926475", "belel22@jaumebalmes.net", "Ingeniero")


# Mostrar toda la información
usuario.saludo()
