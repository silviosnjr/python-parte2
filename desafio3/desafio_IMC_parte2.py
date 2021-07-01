nome = input("Qual o seu nome: ")
altura = 0.0
peso = 0.0

while (altura < 0.1 or altura > 2.4) :
    altura = float(input("Digite sua altura em metros: ").replace(",", "."))
    if (altura > 2.4) :
        print("Altura inválida. Não existe uma pessoal tão alta assim!")
    elif(altura < 0.1) :
        print("Altura inválida. Não existe uma pessoa tão baixa assim!")
    else :
        break

while (peso < 2.1 or peso > 500) :
    peso = float(input("Digite seu peso em Kg: ").replace(",", "."))
    if (peso < 2.1) :
        print("Peso inválido. Não existe uma pessoal tão leve assim!")
    elif(peso > 500) :
        print("Peso inválido. Não existe uma pessoa tão pesada assim!")
    else :
        break

imc = peso / altura ** 2

print(nome, "seu IMC é: %.4f" % imc)

if imc < 18.5:
    print("Você está abaixo do peso, se alimente melhor!")
elif imc < 24.6:
    print("Peso ideal, parabéns!")
elif imc < 29.9:
    print("Levemente acima do peso.")
elif imc < 34.9:
    print("Obesidade grau I, cuidado!")
elif imc < 39.9 :
    print("Obesedidade grau II, isso é severo!")
else :
    print("Obesidade Grau III, isso já é morbito!")