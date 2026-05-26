class CazadorError(Exception):
    """Clase base para las excepciones del juego."""
    pass

class LongitudInvalidaError(CazadorError):
    """Lanzada cuando la longitud es menor a 8 caracteres."""
    pass

class DatoNoNumericoError(CazadorError):
    """Lanzada cuando la entrada no es un número."""
    pass

class ContrasenaIncorrectaError(CazadorError):
    """Lanzada si la contraseña no cumple los criterios técnicos."""
    pass
