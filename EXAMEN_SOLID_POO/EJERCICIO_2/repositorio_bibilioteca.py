"""
En esta clase se maneja el repositorio de la biblioteca. No solo se encarga de guardar y cargar los datos, sino que también me parecio que podria guardar los libros y prestamos en memoria, para no dejar expuestos estos metodos y atributos a la clase de servicio.
"""

class repositorioBiblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.libros = []
        self.prestamos = []
        self.archivo = archivo

    def guardar_en_archivo(self):
        with open(self.archivo, 'w') as f:
            f.write(f"Libros: {len(self.libros)}\n")
            f.write(f"Préstamos: {len(self.prestamos)}\n")
    
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                data = f.read()
            return True
        except:
            return False
        
#SE ME OCURRIO USAR PROPERTES PARA NO ESTAR ACTUALIZANDO CONTADORES MANUALMENTE

    @property
    def contador_libro(self):
        return len(self.libros)
    
    @property
    def contador_prestamo(self):
        return len(self.prestamos)