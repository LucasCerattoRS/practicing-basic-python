peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

# o float permite numeros com virgula #

imc = peso / (altura ** 2)

# ** (Operador de potência) #

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
else:
    print("Acima do peso")

print("Seu IMC é:", round(imc, 2))

# round(imc, 2) vai mostrar dois numeros apos a virgula (arredondamento) #
