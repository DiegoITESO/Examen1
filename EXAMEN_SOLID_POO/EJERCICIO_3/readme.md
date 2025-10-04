# COMO CORRER

Si se utilizara la clase repositorio memoria, instalar redis
```bash
pip install -r requirements.txt
```
y descomentar el codigo e importacion en repositorio_biblioteca.py


Independientemente de lo anterior, correr de la siguiente manera:

```bash
python biblioteca_examen_refactored.py
```

Se abrira una interaccion en el menu para probar añadir un libro, buscar un autor, etc...
Seguir las instrucciones como vayan saliendo. E.j.:
```bash
=== AGREGANDO LIBROS ===
Libro 'Cien Años de Soledad' agregado exitosamente
Libro 'El Principito' agregado exitosamente
Libro '1984' agregado exitosamente
Agregar su propio libro (test):
Título: Luna de pluton
Autor: Dross
ISBN: 1298450152314
Libro 'Luna de pluton' agregado exitosamente

=== BÚSQUEDA POR AUTOR ===
Ingrese palabra clave para buscar por autor: Dross
Resultados para 'Dross':
- Luna de pluton por Dross

=== REALIZAR PRÉSTAMO ===
Ingrese su nombre de la persona para el préstamo: Juan perez
[NOTIFICACIÓN] Juan perez: Préstamo de 'El Principito'
Préstamo realizado a Juan perez

=== LIBROS DISPONIBLES ===
- Cien Años de Soledad
- 1984
- Luna de pluton

=== DEVOLVER LIBRO ===
Libro devuelto exitosamente

=== PRÉSTAMOS ACTIVOS ===
Total de préstamos activos: 0
```