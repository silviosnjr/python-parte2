dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

print("Tipo da variável dias:", type(dias))
print(dias)

#converter uma tupla em lista
dias = list(dias)
print("Tipo da variável dias:", type(dias))
dias.append("sábado extra")
print(dias)

#converter uma tupla em lista
dias = tuple(dias)
print("Tipo da variável dias:", type(dias))
print(dias)