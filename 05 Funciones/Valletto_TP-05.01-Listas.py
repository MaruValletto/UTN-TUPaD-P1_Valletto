# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_de_4 = list(range(4, 101, 4)) #Terminamos en el 101 porque range no incluye el ultimo nro.
print(multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

# Creamos una lista con cinco elementos
comidas_favoritas = ["pizza", "helado", "milanesas", "empanadas", "tarta de frutilla"]
# Mostramos el penúltimo elemento utilizando índice negativo
print("El penúltimo elemento de la lista es:", comidas_favoritas[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#Creamos la lita vacia
lista_vacia = []

# Agregamos la primera palabra
lista_vacia.append("Amarillo")

# Agregamos la primera palabra
lista_vacia.append("Fucsia")

# Agregamos la primera palabra
lista_vacia.append("Celeste")

#Imprimimos por pantalla
print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos el segundo elemento (índice 1) por "loro"
animales[1] = "loro"

# Reemplazamos el último elemento (índice -1) por "oso"
animales[-1] = "oso"

# Mostramos la lista modificada
print("Lista modificada:", animales)

## Ejercicio 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#Paso 1: se crea una lista de numeros, asignando valores a la lista
numeros = [8, 15, 3, 22, 7]
#Paso 2: se elimina el valor maximo de la lista 
numeros.remove(max(numeros))
#Paso 3: se imprime la lista sin el valor maximo
print(numeros)


## Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista6 = []
for i in range(10, 31, 5):
    lista6.append(i)
print(f"Los dos primeros números de la lista son: {lista6[0]} y {lista6[1]}")


## Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

import random
autos = ["sedan", "polo", "suran", "gol"]
print(f"Tu lista inicial es: {autos}. Ahora reemplazaremos los dos valores centrales.")
autos[1] = random.randint(1, 100)
autos[2] = random.randint(1, 100)
print(f"Tu lista final es: {autos}")


## Ejercicio 8 Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

doble = []
opciones = [5, 10, 15]
print(f"Partiendo de la lista: {opciones}")
for i in opciones:
    doble.append(i * 2)
print(f"La lista de dobles es: {doble}")


## Ejercicio 9: Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(f"A partir de la siguiente lista de listas de clientes: {compras}")
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
print(f"Se agregó 'jugo' a la lista del tercer cliente: {compras}")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
print(f"Se reemplazó 'fideos' por 'tallarines' en la lista del segundo cliente: {compras}")
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
print(f"Se eliminó 'pan' de la lista del primer cliente: {compras}")
#d) Imprimir la lista resultante por pantalla
print(f"Finalmente tenemos la siguiente lista de listas: {compras}")

## Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#Posición lista_anidada[0]: 15 | Posición lista_anidada[1]: True | Posición lista_anidada[2][0]: 25.5
#Posición lista_anidada[2][1]: 57.9 | Posición lista_anidada[2][2]: 30.6 | Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista10 = []
lista10.append([15])
lista10.append([True])
lista10.append([25.5, 57.9, 30.6])
lista10.append([False])   
print(f"Tu lista anidada es: {lista10}")