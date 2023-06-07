class Book:
    def __init__(self, titulo, autor, año_publicacion, isbn, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.isbn = isbn
        self.editorial = editorial
        self.genero = genero

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_año_publicacion(self):
        return self.año_publicacion

    def establecer_año_publicacion(self, año_publicacion):
        self.año_publicacion = año_publicacion

    def obtener_isbn(self):
        return self.isbn

    def establecer_isbn(self, isbn):
        self.isbn = isbn

    def obtener_editorial(self):
        return self.editorial

    def establecer_editorial(self, editorial):
        self.editorial = editorial

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def info(self):
        print("Información del Libro:")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año de Publicación:", self.año_publicacion)
        print("ISBN:", self.isbn)
        print("Editorial:", self.editorial)
        print("Género:", self.genero)


libro = Book("Curso Java", "Faro", 2022, "9781890567890", "Editorial Balmes", "Programacion")

# Mostrar toda la información
libro.info()