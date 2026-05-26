import random
import string
from excepciones_cazador import LongitudInvalidaError, ContrasenaIncorrectaError

class Contrasena:
    def __init__(self):
        self.especiales = "¿¡?=)(/¨*+-%&$#!"
    
    def generar(self, longitud):
        if longitud < 8:
            raise LongitudInvalidaError("La longitud mínima permitida es de 8 caracteres.")
        
        # Lógica de generación aleatoria sin repeticiones [10]
        req_mayus = random.choice(string.ascii_uppercase)
        req_minus = random.choice(string.ascii_lowercase)
        req_num = random.choice(string.digits)
        req_esp = random.choice(self.especiales)
        
        password_base = [req_mayus, req_minus, req_num, req_esp]
        todos = string.ascii_letters + string.digits + self.especiales
        pool = "".join([c for c in todos if c not in password_base])
        
        password_base += random.sample(pool, longitud - 4)
        random.shuffle(password_base)
        return "".join(password_base)

class Cofre:
    def __init__(self):
        self.tipos = {"Común": 10, "Raro": 25, "Legendario": 50, "Maldito": -20}
    
    def abrir_aleatorio(self, es_valida):
        if not es_valida:
            return "Maldito", self.tipos["Maldito"]
        seleccion = random.choice(["Común", "Raro", "Legendario"])
        return seleccion, self.tipos[seleccion]