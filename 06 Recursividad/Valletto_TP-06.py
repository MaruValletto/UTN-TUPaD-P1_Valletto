# Trabajo Práctico N° 6 - Recursividad
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumno: Marianela Valletto
# Comisión 25

# Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla 
# el factorial de todos los números enteros entre 1 y el número que indique el usuario 
# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Función para mostrar los factoriales desde 1 hasta n
def mostrar_factoriales_hasta(n):
    for i in range(1, n + 1):
        print(f"El factorial de {i} es: {factorial(i)}")

# Solicitar al usuario un número
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero > 0:
    mostrar_factoriales_hasta(numero)
else:
    print("Por favor, ingrese un número mayor que cero.")

# Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa 
# hasta la posición que el usuario especifique.
# Función recursiva para calcular el valor de Fibonacci

# Función recursiva para calcular el valor de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Función para mostrar la serie de Fibonacci hasta la posición indicada
def mostrar_serie_fibonacci(hasta):
    print(f"Serie de Fibonacci hasta la posición {hasta}:")
    for i in range(hasta + 1):  # Incluye la posición indicada
        print(fibonacci(i), end=" ")
    print()  # salto de línea final

# Solicitar al usuario una posición
posicion = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))

# Validar que sea un número no negativo
if posicion >= 0:
    mostrar_serie_fibonacci(posicion)
else:
    print("Por favor, ingrese un número mayor o igual a cero.")

# Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general. 

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero positivo): "))

# Validación
if exponente >= 0:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")
else:
    print("El exponente debe ser un número entero no negativo.")

# Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. 

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))

# Validación y uso
if numero >= 0:
    binario = decimal_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")
else:
    print("Por favor, ingrese un número entero positivo.")

# Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo 
# o False si no lo es. 

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primera y última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva sin la primera y última letra
    return es_palindromo(palabra[1:-1])

# Programa principal
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if texto.isalpha():
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")
else:
    print("Solo se permiten letras sin espacios ni tildes.")

# Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

# Función recursiva para sumar los dígitos de un número entero positivo
def suma_digitos(n):
    # Caso base: si n es 0, la suma de sus dígitos también es 0
    if n == 0:
        return 0
    else:
        # - Se suma el último dígito con el resultado de la llamada recursiva
        return (n % 10) + suma_digitos(n // 10)

# Programa principal
# Se solicita al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))  

# Validamos que el número sea positivo (o cero)
if numero >= 0:
    # Llamamos a la función y mostramos el resultado
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")    
else:
    # Si el número ingresado no es válido, se muestra un mensaje de error
    print("Por favor, ingrese un número entero positivo.")

# Ejercicio 7: Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques 
# que necesita para construir toda la pirámide.

# Función recursiva para contar la cantidad total de bloques necesarios
def contar_bloques(n):
    # Caso base: si hay solo 1 nivel, se necesita 1 bloque
    if n == 1:
        return 1
    else:
        # Suma los bloques del nivel actual (n) con los de los niveles superiores
        return n + contar_bloques(n - 1)

# Programa principal
nivel_inferior = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

if nivel_inferior >= 1:
    total = contar_bloques(nivel_inferior)
    print(f"Se necesitan {total} bloques para construir la pirámide.")
else:
    print("Por favor, ingrese un número entero positivo mayor o igual a 1.")

# Ejercicio 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número. 
def contar_digito(numero, digito):
    # Caso base: si el número es 0, no quedan dígitos para contar
    if numero == 0:
        return 0
    
    # Comprobar si el último dígito del número es igual al dígito buscado
    if numero % 10 == digito:
        # Contamos 1 y seguimos con el resto del número
        return 1 + contar_digito(numero // 10, digito)
    else:
        # Si no es igual, seguimos sin contar y continuamos recursivamente
        return contar_digito(numero // 10, digito)

# Solicitamos al usuario un número entero positivo y un dígito
num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a contar (0-9): "))

if num >= 0 and 0 <= dig <= 9:
    resultado = contar_digito(num, dig)
    print(f"El dígito {dig} aparece {resultado} veces en el número {num}.")
else:
    print("Por favor, ingrese valores válidos.")
    
