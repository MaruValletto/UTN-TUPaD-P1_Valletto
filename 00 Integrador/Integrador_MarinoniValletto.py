# Trabajo Práctico Integrador
# Tecnicatura Universitaria en Programación a Distancia - UTN
# Alumno: Marinoni Macarena, Valleto Marianela
# Comisión 25

# Definicion para la clase Nodo que representa un nodo en el árbol
# Cada nodo tiene un nombre y una lista de hijos.
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []


# El método agregar_hijo permite añadir un hijo al nodo actual.
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

# El método imprimir permite mostrar el árbol de forma jerárquica.  
    def imprimir(self, prefijo="", es_ultimo=True):
        conector = "└── " if es_ultimo else "├── "
        print(prefijo + conector + self.nombre)
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
        for i, hijo in enumerate(self.hijos):
            ultimo = i == len(self.hijos) - 1
            hijo.imprimir(nuevo_prefijo, ultimo)


# Crear estructura raíz del árbol
anio1 = Nodo("Año 1")

# Cuatrimestres
cuatrimestre1 = Nodo("Primer Cuatrimestre")
cuatrimestre2 = Nodo("Segundo Cuatrimestre")
anio1.agregar_hijo(cuatrimestre1)
anio1.agregar_hijo(cuatrimestre2)

# Materias Cuatrimestre 1
prog1 = Nodo("Programación I")
ayso = Nodo("Arquitectura y Sistemas Operativos")
mate = Nodo("Matemática")
orga = Nodo("Organización Empresarial")
cuatrimestre1.agregar_hijo(prog1)
cuatrimestre1.agregar_hijo(ayso)
cuatrimestre1.agregar_hijo(mate)
cuatrimestre1.agregar_hijo(orga)

# Compromisos por materia Cuatrimestre 1

prog1.agregar_hijo(Nodo("Parcial 1 - Fecha: 10/05 - Modalidad: A distancia"))
prog1.agregar_hijo(Nodo("TP Integrador - Fecha: 09/06"))
prog1.agregar_hijo(Nodo("Parcial 2 - Fecha: 14/06 - Modalidad: A distancia"))

ayso.agregar_hijo(Nodo("Parcial 1 - Fecha: 03/05 - Modalidad: A distancia"))
ayso.agregar_hijo(Nodo("Entrega Proyecto Virtualización - Fecha: 05/06"))
ayso.agregar_hijo(Nodo("Parcial 2 - Fecha: 11/06 - Modalidad: A distancia"))

mate.agregar_hijo(Nodo("TP Integrador - Fecha: 28/04"))
mate.agregar_hijo(Nodo("Parcial 1 - Fecha: 14/05 - Modalidad: A distancia"))
mate.agregar_hijo(Nodo("TP Integrador 2 - Fecha: 13/06"))
mate.agregar_hijo(Nodo("Parcial 2 - Fecha: 25/06 - Modalidad: A distancia"))
mate.agregar_hijo(Nodo("TP Integrador 3 - Fecha: 30/06"))

orga.agregar_hijo(Nodo("TP Individual 1 - Fecha: "))
orga.agregar_hijo(Nodo("TP Individual 2 - Fecha: 27/04"))
orga.agregar_hijo(Nodo("Parcial 1 - Fecha: 17/05 - Modalidad: A distancia"))
orga.agregar_hijo(Nodo("Parcial 2 - Fecha: 07/06 - Modalidad: A distancia"))
orga.agregar_hijo(Nodo("TP Integrador - Fecha: 19/06 "))

cuatrimestre1.agregar_hijo(Nodo("Reunión con grupo de Programación - Fecha: 11/06"))


# Materias Cuatrimestre 2
prog2 = Nodo("Programación II")
estad = Nodo("Probabilidad y Estadística")
bdd1 = Nodo("Base de Datos I")
ingles1 = Nodo("Inglés I")
cuatrimestre2.agregar_hijo(prog2)
cuatrimestre2.agregar_hijo(estad)
cuatrimestre2.agregar_hijo(bdd1)
cuatrimestre2.agregar_hijo(ingles1)

cuatrimestre2.agregar_hijo(Nodo("Mesa de examen - Fecha tentativa: 26 al 28/11"))

# Compromisos por materia Cuatrimestre 2

prog2.agregar_hijo(Nodo("Inicio tentativo cursado - Fecha: 01/08"))
estad.agregar_hijo(Nodo("Inicio tentativo cursado - Fecha: 01/08"))
bdd1.agregar_hijo(Nodo("Inicio tentativo cursado - Fecha: 01/08"))
ingles1.agregar_hijo(Nodo("Inicio tentativo cursado - Fecha: 01/08"))

# Imprimir árbol completo
anio1.imprimir()
