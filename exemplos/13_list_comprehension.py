palavra_secreta = "banana"

#lista vazia
letras_acertadas = []

#utilizando o list comprehension
letras_acertadas = ["_" for letra in palavra_secreta]

#A linha a cima é a mesma coisa que as linhas abaixo
#
#letras_acertadas = []
#
#for letra in palavra_secreta :
#   letras_acertadas.append("_")

print(letras_acertadas)