peso = float(input("Por favor, digite seu peso em KG: "))
altura = float(input("Por favor, digite sua altura em metros: "))

imc = peso/pow(altura,2)

if imc < 20:
    print("Você está abaixo do peso.")
elif imc <= 25:
    print("Você está com o peso ideal.")
elif imc <= 30:
    print("Você está com excesso de peso.")
elif imc <= 35:
    print("Você está com obesidade")
else:
    print("Você está com obesidade mórbida")

