#Detalles del programa
#Lineaminetos 
# Juego: Cazador de Contraseñas
Este proyecto es una aplicación interactiva desarrollada en Python como parte de la evaluación final (Fase 5) del curso de Programación.
#El software simula un sistema donde el usuario asume el rol de un cazador que debe generar contraseñas seguras para abrir diversos cofres y acumular puntos
Características Principales
El sistema aplica de forma rigurosa los pilares de la Programación Orientada a Objetos (POO) y el manejo avanzado de excepciones.
Generación Aleatoria: Las contraseñas se generan sin un orden predecible

Validación Estricta:
Longitud mínima de 8 caracteres

Inclusión obligatoria de: mayúsculas, minúsculas, números y caracteres especiales (¿¡?=)(/¨*+-%&$#!)

Sin caracteres repetidos, garantizando la integridad de la clave

Sistema de Recompensas: Apertura de cofres de tipo Común (+10), Raro (+25) y Legendario (+50)

Penalizaciones: Uso de "Cofres Malditos" (-20 puntos) cuando la entrada no cumple los requisitos técnicos

# Arquitectura del Software (POO)
El código sigue el principio DRY (Don't Repeat Yourself) y una estructura modular para facilitar el mantenimiento

Clase Contrasena: Gestiona la lógica de creación y validación de claves mediante métodos de encapsulamiento

Clase Cofre: Implementa el polimorfismo para asignar recompensas según la validez del intento

Clase JuegoCazador: Orquesta el flujo principal, las rondas de juego y el control de excepciones
Estructura de Archivos (Modular)
Para cumplir con estándares de calidad y portabilidad, el proyecto se distribuye en:
main.py: Punto de entrada de la aplicación.
motor_juego.py: Lógica del flujo del juego.
logica_cazador.py: Definición de clases de negocio.
excepciones_cazador.py: Definición de errores personalizados.
Manejo de Excepciones
El sistema es robusto y resiliente, utilizando excepciones personalizadas que heredan de la clase base Exception
:
LongitudInvalidaError: Se activa si el usuario solicita menos de 8 caracteres.
DatoNoNumericoError: Captura errores cuando la entrada de longitud no es un entero

#ContrasenaIncorrectaError: Error interno si la clave generada falla las pruebas de validación

# Instrucciones de Ejecución
Asegúrese de tener instalado Python 3.10 o superior

# Clone el repositorio:
Navegue a la carpeta del proyecto y ejecute el archivo principal:
# Integración Continua (CI)
Este repositorio incluye un flujo de trabajo automatizado mediante GitHub Actions que verifica la sintaxis del código en cada push, asegurando que el software esté siempre listo para producción
# Autor
# Estudiante: Ivan Darío Saenz Lugo
#Grupo: 213023_308
#Curso: Programación (213023A_2201)
#Institución: Universidad Nacional Abierta y a Distancia (UNAD)