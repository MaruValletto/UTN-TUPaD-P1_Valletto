
# Trabajo Práctico 3 - Condicionales
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumno: Marianela Valletto
# Comisión 25

# Ejercicio 1: Escribir un programa que solicite la edad del usuario.

# Solicitar al usuario su edad y convertir la entrada a un entero
edad = int(input("Ingrese su edad: "))

# Comprobar si la edad ingresada es mayor a 18
if edad > 18:
    # Si la edad es mayor que 18, imprimir que es mayor de edad
    print("Es mayor de edad")


# Ejercicio 2: Escribir un programa que solicite su nota al usuario.

# Solicitar al usuario que ingrese su nota y convertir la entrada a un número flotante
nota = float(input("Ingrese su nota: "))

# Comprobar si la nota ingresada es mayor o igual a 6
if nota >= 6:
    # Si la nota es mayor o igual a 6, imprimir "Aprobado"
    print("Aprobado")
else:
    # Si la nota es menor que 6, imprimir "Desaprobado"
    print("Desaprobado")


# Ejercicio 3: Escribir un programa que permita ingresar solo números pares. 

# Solicitamos al usuario que ingrese un número
numero = int(input("Por favor, ingrese un número: "))

# Evaluamos si el número es par o impar usando el operador %
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a que categoria pertenece

# Solicitamos al usuario su edad
edad = int(input("Por favor, ingrese su edad: "))

# Evaluamos la categoría a la que pertenece según la edad
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


## Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 

# Solicitamos al usuario que ingrese una contraseña
contraseña = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")

# Evaluamos la longitud de la contraseña usando la función len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

## Ejercicio 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y 
#su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.

import random
from statistics import mode, median, mean

# Crear una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparar la moda, mediana y media para determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda.")
else:
    print("Sin sesgo.")


## Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. *texto en cursiva*

# Solicitamos al usuario que ingrese una frase o palabra
entrada = input("Por favor, ingrese una frase o palabra: ")

# Comprobamos si la última letra del string es una vocal
if entrada[-1].lower() in 'aeiou':
    entrada += '!'  # Añadimos un signo de exclamación al final

# Imprimimos el resultado
print(entrada)


## Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la acción que desea realizar.

# Solicitar el nombre al usuario
nombre = input("Por favor, ingrese su nombre: ")

# Solicitar la opción de transformación
opcion = int(input("Seleccione una opción: \n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n"))

# Realizar la transformación según la opción seleccionada
if opcion == 1:
    resultado = nombre.upper()  # Convertir a mayúsculas
elif opcion == 2:
    resultado = nombre.lower()  # Convertir a minúsculas
elif opcion == 3:
    resultado = nombre.title()  # Convertir a primera letra mayúscula
else:
    resultado = "Opción inválida."

# Imprimir el resultado
print("Resultado:", resultado)



## Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto y lo clasifique en categorias según la misma.

# Solicitar la magnitud del terremoto al usuario
magnitud = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Richter: "))

# Clasificar la magnitud en categorías
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprimir el resultado
print(f"La magnitud del terremoto es {magnitud}, lo cual es clasificado como: {categoria}")


## Ejercicio 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.

# Solicitar al usuario el hemisferio, mes y día
hemisferio = input("Por favor, ingrese su hemisferio (N para Norte, S para Sur): ").upper()
mes = int(input("Por favor, ingrese el número del mes (1-12): "))
dia = int(input("Por favor, ingrese el día del mes: "))

# Determinar la estación del año según el hemisferio, mes y día
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes < 3) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (3 <= mes < 6) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (6 <= mes < 9) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (9 <= mes < 12) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes < 3) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (3 <= mes < 6) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (6 <= mes < 9) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (9 <= mes < 12) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

# Imprimir la estación del año
print(f"En el hemisferio {hemisferio}, el {dia} de mes {mes} corresponde a la estación: {estacion}.")
