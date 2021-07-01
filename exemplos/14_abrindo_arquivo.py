import random

#abrindo o arquivo e colocando dentro da variavel arquivo,
#o parametro r significa que será aberto para leitura
arquivo = open("palavras.txt", "r")
palavras = []

#percorremos todas as linhas do arquivo
#e colocamos na lista palavras
for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()

#sorteamos uma palavra
numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()
print(palavra_secreta)