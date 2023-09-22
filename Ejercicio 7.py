# 
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("\nMenú:")
print("1. Sumar los dos números")
print("2. Restar los dos números en el orden puesto")
print("3. Multiplicar los dos números")
opcion = input("Seleccione una opción: ")

if opcion == "1":
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es igual a {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es igual a {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es igual a {resultado}")
else:
    print("Opción no válida.")