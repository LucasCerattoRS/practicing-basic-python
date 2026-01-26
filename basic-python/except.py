#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

valores = [10, 20, 30, 40, 50]
try:
    media = sum(valores) / len(valores)
    print(f"A média dos valores é: {media}")
except ZeroDivisionError:
    print("Erro: A lista está vazia.")

# Len retorna o número de itens em um objeto. No caso de listas, ele retorna a quantidade de elementos presentes na lista. #
# Sum calcula a soma de todos os elementos em um iterável, como uma lista ou tupla. #

# Divisão por zero
except ZeroDivisionError:
    print("Não pode dividir por zero!")

# Conversão de tipo inválida
except ValueError:
    print("Valor inválido para conversão!")

# Índice fora do intervalo
except IndexError:
    print("Índice não existe na lista!")

# Chave não encontrada em dicionário
except KeyError:
    print("Chave não encontrada!")

# Arquivo não encontrado
except FileNotFoundError:
    print("Arquivo não existe!")

# Tipo de dado incorreto
except TypeError:
    print("Tipo de dado inválido!")

# Atributo não existe
except AttributeError:
    print("Atributo não existe!")

# Nome de variável não definida
except NameError:
    print("Variável não foi definida!")