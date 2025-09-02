# Tupla de estudiantes
estudiantes = (
("Ana", 8.5),
("Luis", 7.0),
("María", 9.2),
("Pedro", 6.8),
("Sofía", 7.9)
)

ListaEstudiantes = list(estudiantes) #Convercion lista 
print(f"Lista de estudiantes: {ListaEstudiantes}")
print("----"*20)


# Modificación de la calificación de Pedro
ListaEstudiantes[3] = ("Pedro", 8.0)
print(f"Lista modificada: Nota de Pedro: 8.0")
print(ListaEstudiantes)
print("----"*20)

# Ordena con la nota en forma decendente
for puesto in range(len(ListaEstudiantes)):#FOR para leer la lista segun orden
    for nota in range(0, len(ListaEstudiantes)-puesto-1):#For para ordenarla por nota
        if ListaEstudiantes[nota][1] < ListaEstudiantes[nota+1][1]:#Modifica el orden
            # Cambia de lugar
            ListaEstudiantes[nota], ListaEstudiantes[nota+1] = ListaEstudiantes[nota+1], ListaEstudiantes[nota]

print(f"Lista ordenada por nota (descendente):")
print(ListaEstudiantes)