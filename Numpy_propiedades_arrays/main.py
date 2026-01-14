# coding=utf-8

"""
============================
Programa:       numpy_propiedades_arrays
Contacto:       Juan Dario Rodas - jdrodas@hotmail.com

Propósito:
----------
- Demostrar las propiedades de los arreglos usando la librería numpy
- Shape, ndim, size, dtype, itemsize, nbytes
- Tipos de datos en arreglos: enteros, floats, booleanos
- Metodos disponibles para obtener información sobre el manejo de memoria
============================
"""

import numpy as np

print("=" * 60)
print("PROPIEDADES BÁSICAS DE ARRAYS")
print("=" * 60)

# Creamos un array de ejemplo
ejemplo = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

print("\nArray de ejemplo:")
print(ejemplo)

print("\n" + "-" * 60)
print("Propiedades básicas:")
print("-" * 60)

# shape: forma/dimensiones del array (filas, columnas, ...)
print(f"\nshape (forma): {ejemplo.shape}")
print(f"   → {ejemplo.shape[0]} filas, {ejemplo.shape[1]} columnas")

# ndim: número de dimensiones
print(f"\nndim (número de dimensiones): {ejemplo.ndim}")

# size: número total de elementos
print(f"\nsize (tamaño total): {ejemplo.size}")
print(f"   → {ejemplo.shape[0]} × {ejemplo.shape[1]} = {ejemplo.size} elementos")

# dtype: tipo de dato de los elementos
print(f"\ndtype (tipo de dato): {ejemplo.dtype}")

# itemsize: tamaño en bytes de cada elemento
print(f"\nitemsize (bytes por elemento): {ejemplo.itemsize}")

# nbytes: memoria ocupada en bytes
print(f"\nnbytes (memoria total en bytes): {ejemplo.nbytes}")
print(f"   → {ejemplo.size} elementos × {ejemplo.itemsize} bytes = {ejemplo.nbytes} bytes")

print("\n" + "=" * 60)
print("COMPARACIÓN: Arreglos de 1D vs 2D vs 3D")
print("=" * 60)

# Arreglo 1D (Vector)
arreglo_1d = np.array([1, 2, 3, 4, 5])
print("\nArreglo 1D (Vector):")
print(arreglo_1d)
print(f"   shape: {arreglo_1d.shape}")
print(f"   ndim: {arreglo_1d.ndim}")
print(f"   size: {arreglo_1d.size}")

# Arreglo 2D (Matriz)
arreglo_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\nArreglo 2D (Matriz):")
print(arreglo_2d)
print(f"   shape: {arreglo_2d.shape}")
print(f"   ndim: {arreglo_2d.ndim}")
print(f"   size: {arreglo_2d.size}")

# Arreglo 3D (Tensor)
arreglo_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print("\nArreglo 3D (Tensor):")
print(arreglo_3d)
print(f"   shape: {arreglo_3d.shape}")
print(f"   ndim: {arreglo_3d.ndim}")
print(f"   size: {arreglo_3d.size}")

print("\n" + "-" * 60)
print("Interpretación del shape:")
print("-" * 60)
print(f"   1D: ({arreglo_1d.shape[0]},) → {arreglo_1d.shape[0]} elementos")
print(f"   2D: {arreglo_2d.shape} → {arreglo_2d.shape[0]} filas × {arreglo_2d.shape[1]} columnas")
print(f"   3D: {arreglo_3d.shape} → {arreglo_3d.shape[0]} bloques × {arreglo_3d.shape[1]} filas × {arreglo_3d.shape[2]} columnas")

print("\n" + "=" * 60)
print("TIPOS DE DATOS (dtype)")
print("=" * 60)

# Enteros
print("\n1. Enteros (int):")
arreglo_enteros = np.array([1, 2, 3])
print(f"   Array: {arreglo_enteros}")
print(f"   dtype: {arreglo_enteros.dtype}")

# Flotantes
print("\n2. Flotantes (float):")
arreglo_float = np.array([1.5, 2.3, 3.7])
print(f"   Array: {arreglo_float}")
print(f"   dtype: {arreglo_float.dtype}")

# Booleanos
print("\n3. Booleanos (bool):")
arreglo_bool = np.array([True, False, True])
print(f"   Array: {arreglo_bool}")
print(f"   dtype: {arreglo_bool.dtype}")

# Especificar dtype explícitamente
print("\n4. Especificar dtype manualmente:")
arreglo_float32 = np.array([1, 2, 3], dtype=np.float32)
print(f"   Array: {arreglo_float32}")
print(f"   dtype: {arreglo_float32.dtype}")

# Conversión de tipos
print("\n5. Conversión de tipos (astype):")
arreglo_original = np.array([1.7, 2.3, 3.9])
arreglo_convertido = arreglo_original.astype(int)
print(f"   Original: {arreglo_original} → dtype: {arreglo_original.dtype}")
print(f"   Convertido: {arreglo_convertido} → dtype: {arreglo_convertido.dtype}")

print("\n" + "=" * 60)
print("ANÁLISIS DE MEMORIA")
print("=" * 60)

# Diferentes tamaños y tipos
arreglo_int8 = np.array([1, 2, 3, 4, 5], dtype=np.int8)
arreglo_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arreglo_float64 = np.array([1, 2, 3, 4, 5], dtype=np.float64)

print("\nMismos valores, diferentes tipos:")
print(f"\n   int8:    {arreglo_int8.nbytes} bytes ({arreglo_int8.itemsize} bytes/elemento)")
print(f"   int32:   {arreglo_int32.nbytes} bytes ({arreglo_int32.itemsize} bytes/elemento)")
print(f"   float64: {arreglo_float64.nbytes} bytes ({arreglo_float64.itemsize} bytes/elemento)")

# Array grande
arreglo_grande = np.zeros((1000, 1000))
print(f"\n   Array de 1000×1000 elementos:")
print(f"   → {arreglo_grande.nbytes:,} bytes")
print(f"   → {arreglo_grande.nbytes / 1024:.2f} KB")
print(f"   → {arreglo_grande.nbytes / (1024 ** 2):.2f} MB")

print("\n" + "=" * 60)
print("MÉTODOS INFORMATIVOS")
print("=" * 60)

arreglo_ejemplo = np.array([[1, 2, 3],
                [4, 5, 6]])

print("\nArray:")
print(arreglo_ejemplo)

print("\n📋 Información del array:")
print(f"   Array está en memoria C-contigua: {arreglo_ejemplo.flags['C_CONTIGUOUS']}")
print(f"   Array está en memoria Fortran-contigua: {arreglo_ejemplo.flags['F_CONTIGUOUS']}")
print(f"   Array es escribible: {arreglo_ejemplo.flags['WRITEABLE']}")