# P1: Solicitar las horas de estudio en la tarde
horas_tarde = int(input("Ingresa las horas de estudio en la tarde: "))

# P2: Solicitar las horas de estudio en la noche
horas_noche = int(input("Ingresa las horas de estudio en la noche: "))

# P3: Solicitar los minutos extra de repaso
minutos_extra = int(input("Ingresa los minutos extra de repaso: "))

# P4: Sumar las horas de estudio de la tarde y la noche
total_horas = horas_tarde + horas_noche

# P5: Convertir el total de horas a minutos y sumar los minutos extra
total_minutos = (total_horas * 60) + minutos_extra

# P6: Mostrar el total de horas y minutos estudiados
print(f"Estudiaste {total_horas} horas y {minutos_extra} minutos en total.")

# P7: Mostrar el equivalente total en minutos
print(f"Eso equivale a {total_minutos} minutos.")