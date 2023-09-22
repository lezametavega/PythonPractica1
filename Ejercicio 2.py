# 
costo_comida = float(input("Ingrese el costo de la comida: $  "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina a dejar: "))
propina = costo_comida * (porcentaje_propina / 100)
print(f"Debe dejar $ {propina:} de propina.")