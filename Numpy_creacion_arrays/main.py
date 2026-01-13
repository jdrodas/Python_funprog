# coding=utf-8

"""
============================
Programa:       numpy_creacion_arrays
Contacto:       Juan Dario Rodas - jdrodas@hotmail.com

Propósito:
----------
- Demostrar la creación de arrays básicos desde listas usando la librería numpy
- Arreglos de valores especiales: ceros, unos, matriz identidad, matriz constante
============================
"""

import numpy as np

print("=" * 60)
print("CREACIÓN DE ARREGLOS BÁSICOS")
print("=" * 60)

# 1. Crear arreglo 1D desde una lista
print("\n1. Arreglo 1D (vector) desde lista:")
arreglo_1d = np.array([1, 2, 3, 4, 5])
print(f"   {arreglo_1d}")
print(f"   Tipo: {type(arreglo_1d)}")

# 2. arreglo 2D (matriz) desde lista de listas
print("\n2. Arreglo 2D (matriz) desde lista de listas:")
arreglo_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(arreglo_2d)
print(f"   Dimensiones: {arreglo_2d.shape}")

print("\n" + "=" * 60)
print("ARRAYS CON VALORES ESPECIALES")
print("=" * 60)

# 3. arreglo de ceros
print("\n3. arreglo de ceros (3x4):")
arreglo_zeros = np.zeros((3, 4))
print(arreglo_zeros)

# 4. arreglo de unos
print("\n4. arreglo de unos (2x3):")
arreglo_unos = np.ones((2, 3))
print(arreglo_unos)

# 5. Matriz identidad
print("\n5. Matriz identidad (4x4):")
matriz_identidad = np.eye(4)
print(matriz_identidad)

# 6. matriz con un valor constante
print("\n6. Array con valor constante 7 (2x3):")
matriz_constante = np.full((2, 3), 7)
print(matriz_constante)
