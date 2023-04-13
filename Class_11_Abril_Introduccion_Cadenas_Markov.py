##Caminatas aleatorias 

import numpy as np

# define the matrix
matriz_transicion = np.array([[1/2, 1/2], [1/3, 2/3]])

print(matriz_transicion)

probabilidad_cero = np.array([1, 0])

# calculate p^3
matriz_transicion_3 = np.linalg.matrix_power(matriz_transicion, 3)
# print the result
print(matriz_transicion_3)


resultado = np.dot(probabilidad_cero, matriz_transicion_3)
print(resultado)


# calculate p^5
matriz_transicion_5 = np.linalg.matrix_power(matriz_transicion, 5)
# print the result
print(matriz_transicion_5)


# calculate p^10
matriz_transicion_10 = np.linalg.matrix_power(matriz_transicion, 10)
# print the result
print(matriz_transicion_10)


# La cadena se estabiliza despues de 23 pasos  
matriz_transicion_100 = np.linalg.matrix_power(matriz_transicion, 100)
# print the result
print(matriz_transicion_100)