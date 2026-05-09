# P1: Solicitar el porcentaje de batería actual
bateria = int(input("Ingresa el porcentaje de batería: "))

# P2: Evaluar si la batería es menor que 20
if bateria < 20:
    # P3: Mostrar mensaje de batería crítica
    print("Batería crítica")

# P4: Evaluar si la batería está entre 20 y 80
elif bateria <= 80:
    # P5: Mostrar mensaje de batería media
    print("Batería media")
# P6: Si no se cumple lo anterior, la batería es mayor que 80
else:
    # P7: Mostrar mensaje de batería alta
    print("Batería alta")