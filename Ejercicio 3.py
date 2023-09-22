# 
peso_gr_payaso = 112
peso_gr_muñeca = 75
num_payasos = int(input("Número de payasos vendidos: "))
num_muñecas = int(input("Número de muñecas vendidas: "))
peso_total = (num_payasos * peso_gr_payaso) + (num_muñecas * peso_gr_muñeca)
print(f"El peso total del paqueete enviado es {peso_total} gr.")