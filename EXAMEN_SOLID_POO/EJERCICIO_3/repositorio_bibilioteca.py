from abc import ABC, abstractmethod
# import redis
import json

"""
En esta clase se maneja el repositorio de la biblioteca. No solo se encarga de guardar y cargar los datos, sino que también me parecio que podria guardar los libros y prestamos en memoria, para no dejar expuestos estos metodos y atributos a la clase de servicio.
"""

class IrepositorioBiblioteca(ABC):
    def __init__(self):
        self.libros = []
        self.prestamos = []

    @abstractmethod
    def guardar(self):
        pass

    @abstractmethod
    def cargar(self):
        pass
        
    @property
    def contador_libro(self):
        return len(self.libros)
    
    @property
    def contador_prestamo(self):
        return len(self.prestamos)
    
class repositorioArchivo(IrepositorioBiblioteca):
    def __init__(self, archivo="biblioteca.txt"):
        super().__init__()
        self.archivo = archivo

    def guardar(self):
        with open(self.archivo, 'w') as f:
            f.write(f"Libros: {len(self.libros)}\n")
            f.write(f"Préstamos: {len(self.prestamos)}\n")
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                data = f.read()
            return True
        except:
            return False
        
"""
Aqui se implementa guardar y cargar en memoria con Redis
Dejar el codigo comentado si no se tiene Redis instalado y no se utilizara esta clase
si se desea utilizar, correr "pip install -r requirements.txt" para instalar la libreria, recomiendo
usar un entorno virtual. Asegurarse tambien de tener el servidor de Redis corriendo localmente.
"""
# class repositorioMemoria(IrepositorioBiblioteca):
#     def __init__(self, port=6379, host='localhost', db=0):
#         super().__init__()
#         self._redis_client = redis.Redis(host=host, port=port, db=db)

#     def guardar(self):
#         self._redis_client.set('libros', json.dumps(self.libros))
#         self._redis_client.set('prestamos', json.dumps(self.prestamos))
    
#     def cargar(self):
#         try:
#             libros_data = self._redis_client.get('libros')
#             prestamos_data = self._redis_client.get('prestamos')
#             if libros_data:
#                 self.libros = json.loads(libros_data)
#             if prestamos_data:
#                 self.prestamos = json.loads(prestamos_data)
#             if not libros_data and not prestamos_data:
#                 self.libros = []
#                 self.prestamos = []
#             return True
#         except:
#             return False