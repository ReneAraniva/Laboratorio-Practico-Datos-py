#lista de calificaciones de un estudiante:
calificaciones = [8, 9, 7, 6, 10, 5, 4, 9]

# Calcular estadísticas
promedio = sum(calificaciones) / len(calificaciones)
maxima = max(calificaciones)#Nota maxima
minima = min(calificaciones)#Nota Minima
por_encima_promedio = sum(1 for nota in calificaciones if nota > promedio)
calificaciones.sort(reverse=True)

# Mostrar resultados
print("---"*15)
print("Estadísticas de calificaciones:")
print(f"Promedio: {promedio}")
print(f"Calificación máxima: {maxima}")
print(f"Calificación mínima: {minima}")
print(f"Calificaciones por encima del promedio: {por_encima_promedio}")
print("Calificaciones ordenadas de mayor a menor:")
print(calificaciones)
print("---"*15)