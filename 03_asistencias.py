# P1: Solicitar el nombre del estudiante
nombre = input("Nombre del estudiante: ")

# P2: Solicitar la cantidad de días asistidos
dias_asistidos = int(input("Días asistidos: "))

# P3: Solicitar el total de días de clases
total_dias = int(input("Total de días de clases: "))

# P4: Calcular el porcentaje de asistencia
porcentaje = (dias_asistidos / total_dias) * 100

# P5: Verificar si la asistencia es alta
asistencia_alta = porcentaje >= 80

# P6: Mostrar el nombre del estudiante
print(f"Estudiante: {nombre}")

# P7: Mostrar el porcentaje de asistencia
print(f"Porcentaje de asistencia: {porcentaje}")

# P8: Mostrar si la asistencia es alta
print(f"¿Asistencia alta?: {asistencia_alta}")