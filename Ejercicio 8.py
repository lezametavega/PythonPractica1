#
hora_actual = input("Ingrese la hora en formato HH:MM (24 horas): ")
hora, minutos = hora_actual.split(":")
hora = int(hora)
minutos = int(minutos)

if (hora == 7 and 0 <= minutos <= 59) or (hora == 8 and minutos == 0):
    print("Es hora de desayunar.")
elif (hora == 12 and 0 <= minutos <= 59) or (hora == 13 and minutos == 0):
    print("Es hora de almorzar.")
elif (hora == 18 and 0 <= minutos <= 59) or (hora == 19 and minutos == 0):
    print("Es hora de cenar.")
else:
    print(" ")