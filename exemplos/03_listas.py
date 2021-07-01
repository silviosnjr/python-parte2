#CRIANDO variável LISTA de frutas
frutas = ["Banana", "Maça", "Pera", "Uva"]
print(frutas)

#ADICIONANDO no final
frutas.append("Melancia")
print("Frutas após append:", frutas)

#INSERINDO
frutas.insert(1, "Abacaxi")
print("Frutas após insert:", frutas)

#REMOVENDO
frutas.pop(3)
print("Frutas após pop:", frutas)

#OBTER O TAMANHO DA LISTA
print("Existem", len(frutas), "nomes de frutas inseridos na lista")