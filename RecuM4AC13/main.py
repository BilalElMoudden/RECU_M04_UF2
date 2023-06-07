#User
from user import User

usuario = User("Bilal", 30, "Pau Claris 21", "183926475", "belel22@jaumebalmes.net", "Ingeniero")
usuario.saludo()
print("-----------------------------------------------")


#Book

from book import Book

libro = Book("Curso Java", "Faro", 2022, "9781890567890", "Editorial Balmes", "Programacion")
libro.info()
print("-----------------------------------------------")

#University

from university import University

universidad = University("Jaume Balmes", "Barcelona", 1939, 687, ["Ingeniería informatica", "Fisica"], 3)
universidad.info()
print("-----------------------------------------------")