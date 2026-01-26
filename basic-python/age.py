def idade(): return int(input("Digite sua idade: "))
idade = idade()
print(f"Você tem {idade} anos.")
if idade < 13:
    print("Você é Crianca.")
elif idade < 18:
    print("Você é Adolescente.")
else:
    print("Você é Adulto.")

# A letra 'f' em Python é um prefixo para f-strings, que permite interpolar variáveis e expressões dentro de strings de forma simples e legível. #