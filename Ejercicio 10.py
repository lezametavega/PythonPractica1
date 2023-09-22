#
Lista = ["domingos", "los", "todos", "son", "clases", "Las"]
Elementos_delete = [0, 4, 5]
Lista2 = [Lista[i] for i in range(len(Lista)) if i not in Elementos_delete]
print(Lista2)