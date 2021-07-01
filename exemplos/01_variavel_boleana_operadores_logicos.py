#variável booleana só pode receber True (verdadeiro) ou False (falso)
#a primeira letra é maiuscula para True e False
continuar = True
tentativa = 1

#enquanto(continuar == true)
while (continuar):
    print(type(continuar), "contendo", continuar)
    resposta = input("Tentativa "+str(tentativa)+" - Você quer continuar o loop digite True, se não digite False")

    #vamos verificar se foi False
    #if de uma linha só podemos fazer assim
    if (resposta == "False"): continuar = False
    tentativa = tentativa+1

print("Você digitou False e o loop foi encerrado")