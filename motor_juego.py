from logica_cazador import Contrasena, Cofre
from excepciones_cazador import CazadorError, DatoNoNumericoError

class JuegoCazador:
    def __init__(self):
        self.puntaje_total = 0
        self.generador = Contrasena()
        self.cofre_sistema = Cofre()
    
    def iniciar(self):
        print("--- BIENVENIDO AL JUEGO: CAZADOR DE CONTRASEÑAS ---")
        while True:
            try:
                print(f"\nPuntaje Actual: {self.puntaje_total}")
                entrada = input("Longitud (mínimo 8) o 'S' para salir: ")
                
                if entrada.upper() == 'S': break
                if not entrada.isdigit():
                    raise DatoNoNumericoError("Debe ingresar un valor numérico entero.")
                
                longitud = int(entrada)
                psw = self.generador.generar(longitud)
                
                tipo, puntos = self.cofre_sistema.abrir_aleatorio(True)
                self.puntaje_total += puntos
                print(f"Contraseña: {psw}\n¡HAS ABIERTO UN COFRE {tipo.upper()}! +{puntos} pts.")

            except CazadorError as e:
                tipo, puntos = self.cofre_sistema.abrir_aleatorio(False)
                self.puntaje_total += puntos
                print(f"ERROR: {e}\n¡OH NO! COFRE {tipo.upper()}. {puntos} pts.")