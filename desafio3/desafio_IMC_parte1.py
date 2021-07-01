nome = input("Qual o seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

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