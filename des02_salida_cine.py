# P1: Solicitar el nombre de la película
pelicula = input("Ingresa el nombre de la película: ")

# P2: Solicitar el precio de una entrada
precio_entrada = int(input("Ingresa el precio de la entrada: "))

# P3: Solicitar la cantidad de entradas
cantidad_entradas = int(input("Ingresa la cantidad de entradas: "))

# P4: Solicitar el dinero extra para comida
dinero_comida = int(input("Ingresa el dinero extra para comida: "))

# P5: Calcular el subtotal de entradas
subtotal_entradas = precio_entrada * cantidad_entradas

# P6: Calcular el total a pagar
total_pagar = subtotal_entradas + dinero_comida

# P7: Mostrar el nombre de la película
print(f"Película: {pelicula}")

# P8: Mostrar el subtotal de entradas
print(f"Subtotal entradas: ${subtotal_entradas}")

# P9: Mostrar el dinero extra para comida
print(f"Extra en comida: ${dinero_comida}")

# P10: Mostrar el total a pagar
print(f"Total a pagar: ${total_pagar}")