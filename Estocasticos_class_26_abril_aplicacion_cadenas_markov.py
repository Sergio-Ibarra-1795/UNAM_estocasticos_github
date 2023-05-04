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





## Imaginar el caso en que la empresa AS genera una campaña publicitaria para quitar clientes a MF

# LA MATRIZ DE TRANSICIÓN DE ESTADOS CAMBIA 
matriz_transicion_inicial_estrategia_AS1 = np.array([[0.85, 0.15], [0.2, 0.8]])


#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_cero_AS = np.array([1, 0])

# calculate p^100
matriz_transicion_100_estrategia_AS1 = np.linalg.matrix_power(matriz_transicion_inicial_estrategia_AS1, 100)
# print the result
print(f"La matriz_transicion_periodo_100 DADA LA ESTRATEGIA AS_1 es: {matriz_transicion_100_estrategia_AS1}")

resultado100__estrategia_AS1= np.dot(probabilidad_cero_AS , matriz_transicion_100_estrategia_AS1)
print(f"La función de distribucion en periodo 100  DADA LA ESTRATEGIA AS_1 es: {resultado100__estrategia_AS1}")







## Imaginar el caso en que la empresa AS genera una campaña publicitaria AUN MAS AGRESIVA para quitar clientes a MF

# LA MATRIZ DE TRANSICIÓN DE ESTADOS CAMBIA 
matriz_transicion_inicial_estrategia_AS2 = np.array([[0.75, 0.25], [0.2, 0.8]])


#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_cero_AS_2 = np.array([1, 0])

# calculate p^100
matriz_transicion_100_estrategia_AS2 = np.linalg.matrix_power(matriz_transicion_inicial_estrategia_AS2, 100)
# print the result
print(f"La matriz_transicion_periodo_100 DADA LA ESTRATEGIA AS_2 es: {matriz_transicion_inicial_estrategia_AS2}")

resultado100__estrategia_AS2= np.dot(probabilidad_cero_AS_2 , matriz_transicion_100_estrategia_AS2)
print(f"La función de distribucion en periodo 100  DADA LA ESTRATEGIA AS_2 es: {resultado100__estrategia_AS2}")

