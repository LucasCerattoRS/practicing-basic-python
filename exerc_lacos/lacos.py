clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for i in range(len(clientes)):
# len(clientes)  retorna 5 #
# range(5)  # gera: 0, 1, 2, 3, 4 #
# i = Assume cada valor gerado pelo range. #
# fluxo do laço: i = 0 → i = 1 → i = 2 → i = 3 → i = 4 #
    print(f'O Cliente número {i+1} é: {clientes[i]}')

# For é adequado porque já sabemos a quantidade de repetições que precisaremos fazer


# Simplificado:

# clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"] #

# for cliente in clientes: #
#    print(cliente) #