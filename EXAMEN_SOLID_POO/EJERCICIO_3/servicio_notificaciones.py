class servicioNotificaciones:
    @staticmethod
    def enviar_notificacion(usuario, libro):
        """
        En este caso se me ocurrio hacer el metodo abstracto, para no gastar memoria en una instancia
        que no guarda nada.
        """
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{libro}'")