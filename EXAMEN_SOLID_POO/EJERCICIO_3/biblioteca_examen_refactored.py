import buscador
from repositorio_bibilioteca import IrepositorioBiblioteca, repositorioArchivo
from servicio_notificaciones import servicioNotificaciones
from validador_biblioteca import validadorBiblioteca

class Libro:
    def __init__(self, id, titulo, autor, isbn, disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

class Prestamo:
    def __init__(self, id, libro_id, usuario, fecha):
        self.id = libro_id
        self.libro_id = libro_id
        self.usuario = usuario
        self.fecha = fecha
        self.devuelto = False

# VIOLACIÓN: Esta clase hace DEMASIADAS cosas (SRP)
# VIOLACIÓN: Búsqueda con if/elif (OCP)
# VIOLACIÓN: Dependencia directa de implementación (DIP)
class SistemaBiblioteca:
    def __init__(self, archivo: IrepositorioBiblioteca):
        self._repositorio = repositorioArchivo(archivo)
    
    # VIOLACIÓN SRP: Mezcla validación + lógica de negocio + persistencia
    def agregar_libro(self, titulo, autor, isbn):
        try:
            validadorBiblioteca.validar_titulo(titulo)
            validadorBiblioteca.validar_autor(autor)
            validadorBiblioteca.validar_isbn(isbn)
        except ValueError as e:
            return str(e)
        
        libro = Libro(self._repositorio.contador_libro, titulo, autor, isbn)
        self._repositorio.libros.append(libro)
        
        self._repositorio.guardar()
        
        return f"Libro '{titulo}' agregado exitosamente"
    
    def buscar_libro(self, busqueda: buscador.Buscador, valor: str):
        return busqueda.buscar(valor, self._repositorio.libros)
    
    def realizar_prestamo(self, libro_id, usuario):
        try:
            validadorBiblioteca.validar_usuario(usuario)
            libro = None
            for l in self._repositorio.libros:
                if l.id == libro_id:
                    libro = l
                    break
            
            if not libro:
                return "Error: Libro no encontrado"
            
            if not libro.disponible:
                return "Error: Libro no disponible"
            
            # Lógica de negocio
            from datetime import datetime
            prestamo = Prestamo(
                self._repositorio.contador_prestamo,
                libro_id,
                usuario,
                datetime.now().strftime("%Y-%m-%d")
            )
            
            self._repositorio.prestamos.append(prestamo)
            libro.disponible = False
            

            self._repositorio.guardar()
            
            servicioNotificaciones.enviar_notificacion(usuario, libro.titulo)
            
            return f"Préstamo realizado a {usuario}"
        except ValueError as e:
            return str(e)
    def devolver_libro(self, prestamo_id):
        prestamo = None
        for p in self._repositorio.prestamos:
            if p.id == prestamo_id:
                prestamo = p
                break
        
        if not prestamo:
            return "Error: Préstamo no encontrado"
        
        if prestamo.devuelto:
            return "Error: Libro ya devuelto"
        
        for libro in self._repositorio.libros:
            if libro.id == prestamo.libro_id:
                libro.disponible = True
                break
        
        prestamo.devuelto = True
        self._repositorio.guardar()
        
        return "Libro devuelto exitosamente"
    
    def obtener_todos_libros(self):
        return self._repositorio.libros
    
    def obtener_libros_disponibles(self):
        return [libro for libro in self._repositorio.libros if libro.disponible]
    
    def obtener_prestamos_activos(self):
        return [p for p in self._repositorio.prestamos if not p.devuelto]


# VIOLACIÓN DIP: Dependencia directa de implementación
def main():
    sistema = SistemaBiblioteca("biblioteca.txt")
    
    print("=== AGREGANDO LIBROS ===")
    print(sistema.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", "9780060883287"))
    print(sistema.agregar_libro("El Principito", "Antoine de Saint-Exupéry", "9780156012195"))
    print(sistema.agregar_libro("1984", "George Orwell", "9780451524935"))
    print("Agregar su propio libro (test):")
    titulo, autor, isbn = input("Título: "), input("Autor: "), input("ISBN: ")
    print(sistema.agregar_libro(titulo, autor, isbn))

    print("\n=== BÚSQUEDA POR AUTOR ===")
    keyword = input("Ingrese palabra clave para buscar por autor: ")
    resultados = sistema.buscar_libro(buscador.BuscadorPorAutor(), keyword)
    print(f"Resultados para '{keyword}':")
    for libro in resultados:
        print(f"- {libro.titulo} por {libro.autor}")
    if not resultados:
        print("No se encontraron libros.")
    
    print("\n=== REALIZAR PRÉSTAMO ===")
    nombre = input("Ingrese su nombre de la persona para el préstamo: ")
    print(sistema.realizar_prestamo(1, nombre))
    
    print("\n=== LIBROS DISPONIBLES ===")
    disponibles = sistema.obtener_libros_disponibles()
    for libro in disponibles:
        print(f"- {libro.titulo}")
    
    print("\n=== DEVOLVER LIBRO ===")
    print(sistema.devolver_libro(1))
    
    print("\n=== PRÉSTAMOS ACTIVOS ===")
    activos = sistema.obtener_prestamos_activos()
    print(f"Total de préstamos activos: {len(activos)}")


if __name__ == "__main__":
    main()
