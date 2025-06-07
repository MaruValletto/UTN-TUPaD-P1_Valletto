# Trabajo Práctico N° 7 - Datos Complejos  
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumno: Marianela Valletto
# Comisión 25

#Ejercicio 1
# Diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el resultado
print(precios_frutas)

# Ejercicio 2
# Diccionario actualizado hasta el punto anterior
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el resultado
print(precios_frutas)

# Ejercicio 3
# Diccionario de frutas con precios actualizado
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear una lista con solo las frutas (las claves del diccionario)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print(lista_frutas)

# Ejercicio 4
# Crear diccionario vacío para los contactos
agenda = {}

# Cargar 5 contactos
print("Cargá 5 contactos con su número telefónico:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero

# Consultar un número por nombre
consulta = input("\nIngresá el nombre del contacto que querés consultar: ")

# Mostrar el número si existe
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}' en la agenda.")

# Ejercicio 5
# Solicitar al usuario una frase
frase = input("Ingresá una frase: ")

# Convertir la frase a minúsculas y separar las palabras
palabras = frase.lower().split()

# Mostrar palabras únicas usando un set
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

# Contar la frecuencia de cada palabra con un diccionario
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# Mostrar el diccionario de frecuencia
print("\nCantidad de veces que aparece cada palabra:")
for palabra, cantidad in frecuencia.items():
    print(f"'{palabra}': {cantidad}")

# Ejercicio 6
# Crear diccionario para almacenar nombres y sus notas
alumnos = {}

# Pedir datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)

# Calcular y mostrar promedios
print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Ejercicio 7
# Conjuntos de estudiantes que aprobaron Parcial 1 y Parcial 2
parcial1 = {"Ana", "Bruno", "Carla", "Diego", "Elena"}
parcial2 = {"Bruno", "Carla", "Felipe", "Gabriela", "Diego"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Estudiantes que aprobaron ambos parciales:", ambos)
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)
print("Estudiantes que aprobaron al menos un parcial:", al_menos_uno)

# Ejercicio 8
# Diccionario inicial de productos y su stock
stock_productos = {
    "leche": 20,
    "pan": 35,
    "huevos": 50
}

# Mostrar opciones al usuario
print("Bienvenido al sistema de stock.")
print("Opciones:")
print("1. Consultar stock")
print("2. Agregar unidades al stock")
print("3. Agregar un nuevo producto")

opcion = input("Elegí una opción (1, 2 o 3): ")

# Consultar stock
if opcion == "1":
    producto = input("Ingresá el nombre del producto: ").lower()
    if producto in stock_productos:
        print(f"El stock de '{producto}' es: {stock_productos[producto]}")
    else:
        print(f"El producto '{producto}' no está en el sistema.")

# Agregar unidades al stock
elif opcion == "2":
    producto = input("Ingresá el nombre del producto: ").lower()
    if producto in stock_productos:
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]}")
    else:
        print(f"El producto '{producto}' no está en el sistema. Podés agregarlo como nuevo.")

# Agregar nuevo producto
elif opcion == "3":
    producto = input("Ingresá el nombre del nuevo producto: ").lower()
    if producto in stock_productos:
        print("Ese producto ya existe. Usá la opción 2 para agregar unidades.")
    else:
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = unidades
        print(f"Producto '{producto}' agregado con stock de {unidades} unidades.")

else:
    print("Opción inválida.")

# Ejercicio 9
# Creamos una agenda vacía
agenda = {}

# Cargar eventos en la agenda
cantidad_eventos = int(input("¿Cuántos eventos querés agendar?: "))

for i in range(cantidad_eventos):
    print(f"\nEvento {i+1}:")
    dia = input("Ingresá el día (por ejemplo, 'Lunes'): ").capitalize()
    hora = input("Ingresá la hora (por ejemplo, '14:00'): ")
    evento = input("Ingresá el evento: ")
    clave = (dia, hora)
    agenda[clave] = evento

# Mostrar toda la agenda
print("\nAgenda completa:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# Consultar una actividad específica
print("\nConsulta de actividad:")
consulta_dia = input("Ingresá el día que querés consultar: ").capitalize()
consulta_hora = input("Ingresá la hora que querés consultar (ej: 14:00): ")
clave_consulta = (consulta_dia, consulta_hora)

if clave_consulta in agenda:
    print(f"En {consulta_dia} a las {consulta_hora} tenés: {agenda[clave_consulta]}")
else:
    print(f"No hay ningún evento agendado para {consulta_dia} a las {consulta_hora}.")

#Ejercicio 10
# Diccionario original: país -> capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Invertir el diccionario: capital -> país
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print("Diccionario invertido (capitales como claves):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")

