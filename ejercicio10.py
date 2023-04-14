nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
           77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

# Punto A

lista_nombres = nombres.replace("'", "").replace("\n", "").replace(" ", "").split(',')

diccionario_alumnos = {i: [j, k] for i, j, k in zip(lista_nombres, notas_1, notas_2)}

print('Impresion de diccionario de alumnos'.center(100, '-'))
print(diccionario_alumnos)

# Punto B

print('Impresion de promedio de alumnos'.center(100, '-'))

promedio_alumnos = []

for i, j in diccionario_alumnos.values():
    prom = (i + j) / 2
    promedio_alumnos.append(prom)

# A partir de la lista de nombres + la lista de promedio que cree armo un diccionario donde guardo cada nombre con su nota prom

diccionario_promedio = {i: j for i, j in zip(lista_nombres, promedio_alumnos)}

print(diccionario_promedio)

# Punto C

print('Impresion de promedio general de los alumnos'.center(100, '-'))

promedio_general = (sum(promedio_alumnos)) / len(diccionario_alumnos)

print(f'{promedio_general:.2f}')

# Punto D

print('Impresion del estudiante con la nota promedio mas alta'.center(100, '-'))

promedio_max = max(diccionario_promedio.items(), key=lambda x: x[1])[0]

print(f'El alumno con la nota promedio mas alta es {promedio_max}')

# Punto E

print('Impresion del estudiante con la nota mas baja'.center(100, '-'))

nota_min = min(diccionario_alumnos.items(), key=lambda x: x[1])[0]

print(nota_min.lower())