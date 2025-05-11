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