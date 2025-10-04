class validadorBiblioteca:
    @staticmethod
    def validar_titulo(titulo):
        if not titulo.strip() or len(titulo) < 2:
            raise ValueError("Error: Título inválido")

    @staticmethod
    def validar_autor(autor):
        if not autor.strip() or len(autor) < 3:
            raise ValueError("Error: Autor inválido")

    @staticmethod
    def validar_isbn(isbn):
        if not isbn or len(isbn) < 10:
            raise ValueError("Error: ISBN inválido")

    @staticmethod
    def validar_usuario(usuario):
        if not usuario or len(usuario) < 3:
            raise ValueError("Error: Nombre de usuario inválido")