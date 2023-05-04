## Aplicación de cadenas Markov para analisis de mercado


import numpy as np

#EMPEZANDO CON EL COMPRADOR Z

# LA MATRIZ DE TRANSICIÓN DE ESTADOS
matriz_transicion_periodo_inicial = np.array([[0.7, 0.2, 0.1], [0.2, 0.75, 0.05], [0.1, 0.1, 0.8]])

print(f"La matriz_transicion_periodo_inicial es: {matriz_transicion_periodo_inicial}")

#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_iniciando_z = np.array([1, 0, 0])

# calculate p^2
matriz_transicion_2 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 2)
# print the result
print(f"La matriz_transicion_periodo_2 es: {matriz_transicion_2}")

resultado2_iniciandoz = np.dot(probabilidad_iniciando_z, matriz_transicion_2)
print(f"La función de distribucion en periodo 2 iniciando z es: {resultado2_iniciandoz}")


# calculate p^10
matriz_transicion_10 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 10)
# print the result
print(f"La matriz_transicion_periodo_10 es: {matriz_transicion_10}")

resultado10_iniciandoz = np.dot(probabilidad_iniciando_z , matriz_transicion_10)
print(f"La función de distribucion en periodo 10 iniciando z es: {resultado10_iniciandoz}")


# calculate p^25
matriz_transicion_25 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 25)
# print the result
print(f"La matriz_transicion_periodo_25 es: {matriz_transicion_25}")
resultado25_iniciandoz = np.dot(probabilidad_iniciando_z , matriz_transicion_25)
print(f"La función de distribucion en periodo 25 iniciando z es: {resultado25_iniciandoz}")


# calculate p^100
matriz_transicion_100 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 100)
# print the result
print(f"La matriz_transicion_periodo_100 es: {matriz_transicion_100}")

resultado100_iniciandoz = np.dot(probabilidad_iniciando_z , matriz_transicion_100)
print(resultado100_iniciandoz)
print(f"La función de distribucion en periodo 100 iniciando z es: {resultado100_iniciandoz}")



#EMPEZANDO CON EL COMPRADOR Y

# LA MATRIZ DE TRANSICIÓN DE ESTADOS
matriz_transicion_periodo_inicial = np.array([[0.7, 0.2, 0.1], [0.2, 0.75, 0.05], [0.1, 0.1, 0.8]])

print(f"La matriz_transicion_periodo_inicial es: {matriz_transicion_periodo_inicial}")

#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_iniciando_y = np.array([0, 1, 0])

# calculate p^2
matriz_transicion_2 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 2)
# print the result
print(f"La matriz_transicion_periodo_2 es: {matriz_transicion_2}")

resultado2_iniciandoy = np.dot(probabilidad_iniciando_y, matriz_transicion_2)
print(f"La función de distribucion en periodo 2 iniciando y es: {resultado2_iniciandoy}")


# calculate p^10
matriz_transicion_10 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 10)
# print the result
print(f"La matriz_transicion_periodo_10 es: {matriz_transicion_10}")

resultado10_iniciandoy = np.dot(probabilidad_iniciando_y , matriz_transicion_10)
print(f"La función de distribucion en periodo 10 iniciando y es: {resultado10_iniciandoy}")


# calculate p^25
matriz_transicion_25 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 25)
# print the result
print(f"La matriz_transicion_periodo_25 es: {matriz_transicion_25}")
resultado25_iniciandoy = np.dot(probabilidad_iniciando_y , matriz_transicion_25)
print(f"La función de distribucion en periodo 25 iniciando y es: {resultado25_iniciandoy}")


# calculate p^100
matriz_transicion_100 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 100)
# print the result
print(f"La matriz_transicion_periodo_100 es: {matriz_transicion_100}")

resultado100_iniciandoy = np.dot(probabilidad_iniciando_y , matriz_transicion_100)
print(f"La función de distribucion en periodo 100 iniciando y es: {resultado100_iniciandoy}")







#Cual sería la probabilidad de que un cliente de la empresa Z cambie en 3 meses a la empresa V?

# calculate p^3
matriz_transicion_3 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 3)
# print the result
print(f"La matriz_transicion_periodo_3 es: {matriz_transicion_3}")

#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_iniciando_z = np.array([1, 0, 0])


resultado3_iniciandoz = np.dot(probabilidad_iniciando_z, matriz_transicion_3)
print(f"La función de distribucion en periodo 3 iniciando z es: {resultado3_iniciandoz}")







#EMPEZANDO CON EL COMPRADOR Z, Y y V 

# LA MATRIZ DE TRANSICIÓN DE ESTADOS
matriz_transicion_periodo_inicial = np.array([[0.7, 0.2, 0.1], [0.2, 0.75, 0.05], [0.1, 0.1, 0.8]])

print(f"La matriz_transicion_periodo_inicial es: {matriz_transicion_periodo_inicial}")

#LA PROBABILIDAD EN EL TIEMPO INICIAL O DISTRIBUCIÓN DE PORBABILIDAD INICAL
probabilidad_iniciando_z_y_v = np.array([0.3333, 0.3333, 0.3333])

# calculate p^2
matriz_transicion_2 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 2)
# print the result
print(f"La matriz_transicion_periodo_2 es: {matriz_transicion_2}")

resultado2_iniciando_z_y_v = np.dot(probabilidad_iniciando_z_y_v, matriz_transicion_2)
print(f"La función de distribucion en periodo 2 iniciando z,y,v es: {resultado2_iniciando_z_y_v}")


# calculate p^10
matriz_transicion_10 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 10)
# print the result
print(f"La matriz_transicion_periodo_10 es: {matriz_transicion_10}")

resultado10_iniciando_z_y_v = np.dot(probabilidad_iniciando_z_y_v , matriz_transicion_10)
print(f"La función de distribucion en periodo 10 iniciando z,y,v es: {resultado10_iniciandoy}")


# calculate p^25
matriz_transicion_25 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 25)
# print the result
print(f"La matriz_transicion_periodo_25 es: {matriz_transicion_25}")
resultado25_iniciando_z_y_v = np.dot(probabilidad_iniciando_z_y_v, matriz_transicion_25)
print(f"La función de distribucion en periodo 25 iniciando z,y,v es: {resultado25_iniciando_z_y_v}")


# calculate p^100
matriz_transicion_100 = np.linalg.matrix_power(matriz_transicion_periodo_inicial, 100)
# print the result
print(f"La matriz_transicion_periodo_100 es: {matriz_transicion_100}")

resultado100_iniciando_z_y_v = np.dot(probabilidad_iniciando_z_y_v, matriz_transicion_100)
print(f"La función de distribucion en periodo 100 iniciando z,y,v es: {resultado100_iniciando_z_y_v}")



