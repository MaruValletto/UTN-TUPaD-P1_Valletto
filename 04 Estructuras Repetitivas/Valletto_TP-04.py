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

## Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print ("Calcularé la suma de todos los números comprendidos entre 0 y un número entero positivo que me indiques")
numero7 = int(input("Ingresá un número entero positivo: "))
suma = 0
if numero7 < 0:
    print ("El número ingresado no es positivo")
else:
    for i in range (0, numero7+1):
        suma += i   
print (f"La suma de los números comprendidos entre 0 y {numero7} es: {suma}")

## Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print ("Si me indicas 100 numeros enteros, voy a contarte cuántos de ellos son pares, cuántos impares, cuántos positivos y cuántos negativos.")
cont_ingresos = 0
cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0
cont_ceros = 0

while cont_ingresos < 10:
    numero8 = int(input("Ingresá un número entero: "))
    cont_ingresos += 1
    print (f"Has ingresado {cont_ingresos} números enteros.")
    if numero8 % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
    if numero8 > 0:
        cont_positivos += 1
    elif numero8 < 0:
        cont_negativos += 1
    else:
        cont_ceros += 1
print (f"En los números ingresados tenemos {cont_pares} numeros pares, {cont_impares} numeros impares, {cont_positivos} positivos, {cont_negativos} negativos y {cont_ceros} son ceros.")

## Ejericio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

print ("Si me indicas 100 numeros enteros, calcularé la media de esos valores..")
contador = 0
numero9 = 0
suma = 0

while contador < 5:
    numero9 = int(input("Ingresá un número entero: "))
    contador += 1
    print (f"Has ingresado {contador} números enteros.")
    suma += suma + numero9
media = suma / contador
print (f"La media de los números ingresados es: {media}")

## Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print ("Si me indicas un numero entero, voy a invertir el orden de los digitos")
numero10 = int(input("Ingresá tu número: "))
if numero10 > 0:
    numero10 = str(numero10)
    numero10 = numero10[::-1]
else:
    numero10 = str(numero10)
    numero10 = numero10[1:][::-1]
    numero10 = "-" + numero10
print (f"El número invertido es: {numero10}")
