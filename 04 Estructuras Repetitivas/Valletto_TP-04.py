# Trabajo Práctico 4 - Estructuras Repetitivas
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumno: Marianela Valletto
# Comisión 25

# Ej. 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (101):
    print (i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
# Solicitar al usuario un número entero
numero = int(input("Ingresá un número entero: "))
# Convertir a valor absoluto para evitar problemas con números negativos
numero_absoluto = abs(numero)
# Contar la cantidad de dígitos convirtiendo a cadena
cantidad_digitos = len(str(numero_absoluto))
# Mostrar el resultado
print(f"El número tiene {cantidad_digitos} dígito(s).")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
# Pedimos al usuario que ingrese los valores
valor1 = int(input("Ingresa el primer valor entero: "))
valor2 = int(input("Ingresa el segundo valor entero: "))

total = 0
for i in range(valor1+1, valor2):
    total += i
print(f"La suma de los números entre {valor1} y {valor2} es: {total}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero1= int(input("Ingresá un número entero: "))

suma = 0
while numero1 != 0:
    suma = suma+numero1
    numero1= int(input("Ingresá otro número entero o 0 si deseas terminar: "))

print(f"La suma acumulada entre los numeros ingresados es: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero5= int(input("Juguemos a las adivinanzas, tenes que adivinar el numero que estoy pensando, te doy una ayuda: esta en 0 y 9. A jugar! Ingresá tu prediccion: "))
numero_aleatorio = random.randint(0, 9)
intentos = 1 

while numero5 != numero_aleatorio:
    intentos += 1
    numero5 = int(input("Tu prediccion no es correcta, intentá otro numero:")) 
print(f"¡Adivinaste en {intentos} intentos!")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print ("Imprimiremos por pantalla todos los números pares que estan comprendidos entre 0 y 100, en orden descendente")
for numero in range (100,-1,-2):
    print (numero)