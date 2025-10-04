from abc import ABC, abstractmethod

class Buscador(ABC):
    @abstractmethod
    def buscar(self, valor: str, libros: list):
        pass

class BuscadorPorTitulo(Buscador):
    def buscar(self, valor: str, libros: list):
        resultados = []
        for libro in libros:
            if valor.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados
    
class BuscadorPorAutor(Buscador):
    def buscar(self, valor: str, libros: list):
        resultados = []
        for libro in libros:
            if valor.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados
    
class BuscadorPorISBN(Buscador):
    def buscar(self, valor: str, libros: list):
        resultados = []
        for libro in libros:
            if valor.lower() in libro.isbn.lower():
                resultados.append(libro)
        return resultados

class BuscadorPorDisponibilidad(Buscador):
    def buscar(self, valor: str, libros: list):
        resultados = []
        disponible = valor.lower() == "true"
        for libro in libros:
            if libro.disponible == disponible:
                resultados.append(libro)
        return resultados