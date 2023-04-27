## Aplicación de cadenas Markov para analisis de mercado
#Nos interesa analizar la cuota de mercado y la lealtad de clientes para alguna marca 

import numpy as np

#EMPEZANDO CON EL COMPRADRO MF

# LA MATRIZ DE TRANSICIÓN DE ESTADOS
matriz_transicion = np.array([[0.9, 0.1], [0.2, 0.8]])

print(matriz_transicion)

#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_cero = np.array([1, 0])

# calculate p^2
matriz_transicion_2 = np.linalg.matrix_power(matriz_transicion, 2)
# print the result
print(matriz_transicion_2)


resultado2 = np.dot(probabilidad_cero, matriz_transicion_2)
print(resultado2)


# calculate p^3
matriz_transicion_3 = np.linalg.matrix_power(matriz_transicion, 3)
# print the result
print(matriz_transicion_3)


resultado3 = np.dot(probabilidad_cero, matriz_transicion_3)
print(resultado3)


# calculate p^10
matriz_transicion_10 = np.linalg.matrix_power(matriz_transicion, 10)
# print the result
print(matriz_transicion_10)


resultado10 = np.dot(probabilidad_cero, matriz_transicion_10)
print(resultado10)







#EMPEZANDO CON EL COMPRADRO AS

# LA MATRIZ DE TRANSICIÓN DE ESTADOS
matriz_transicion = np.array([[0.9, 0.1], [0.2, 0.8]])

print(matriz_transicion)

#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_cero_AS = np.array([0, 1])

# calculate p^2
matriz_transicion_2_AS = np.linalg.matrix_power(matriz_transicion, 2)
# print the result
print(matriz_transicion_2_AS)


resultado2_AS = np.dot(probabilidad_cero_AS, matriz_transicion_2_AS)
print(resultado2_AS)



# calculate p^3
matriz_transicion_3_AS = np.linalg.matrix_power(matriz_transicion, 3)
# print the result
print(matriz_transicion_3_AS)


resultado3_AS = np.dot(probabilidad_cero_AS, matriz_transicion_3_AS)
print(resultado3_AS)


# calculate p^10
matriz_transicion_10_AS = np.linalg.matrix_power(matriz_transicion, 10)
# print the result
print(matriz_transicion_10_AS)


resultado10_AS = np.dot(probabilidad_cero_AS, matriz_transicion_10_AS)
print(resultado10_AS)



