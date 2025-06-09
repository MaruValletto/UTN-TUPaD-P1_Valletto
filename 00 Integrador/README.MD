 Organización Académica con Árbol Jerárquico en Python 3

Este repositorio contiene el Trabajo Práctico Integrador de la materia Programación I de la Tecnicatura Universitaria en Programación (UTN FRRo), donde se aplica la estructura de árbol n-ario para modelar la planificación académica del Año 1 de cursado.

Descripción

El proyecto simula el recorrido de un estudiante durante su primer año, organizando materias y compromisos (como parciales, trabajos prácticos y reuniones) en una estructura jerárquica. El árbol fue desarrollado en Python 3 sin el uso de librerías externas, utilizando una clase `Nodo` personalizada.

Estructura del Árbol

La jerarquía se define en distintos niveles:

- Nivel 0: Año académico (raíz)
- Nivel 1: Cuatrimestres (1° y 2°)
- Nivel 2: Materias (por ejemplo, Programación I, Matemática)
- Nivel 3: Compromisos académicos (parciales, TPs, reuniones)
- Nivel 4: Detalles incluidos en el nombre del nodo (fecha, modalidad, grupo)

Implementación

- Clase `Nodo` con atributos `nombre` e `hijos`
- Método `agregar_hijo()` para añadir descendientes
- Método `imprimir()` para recorrer el árbol con formato visual
- Recorrido preorden primero se imprime el nodo actual, luego sus hijos
- Visualización estructurada en consola con caracteres tipo árbol (`├──`, `└──`)

Ejecución

Para ejecutar el programa y ver la jerarquía académica se necesita Python 3