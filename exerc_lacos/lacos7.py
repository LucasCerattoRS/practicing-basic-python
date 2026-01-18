# O livro começa com 5 exemplares em estoque

# Cada venda:

# diminui 1 do estoque

# mostra uma mensagem com a quantidade restante

# Quando o estoque chegar a 0, o sistema:

# para de vender

# mostra "Estoque esgotado"

# Para isso, o melhor é usar um laço while, que repete enquanto ainda houver estoque.

# Porque não sabemos “quantas vezes” a venda vai acontecer, apenas sabemos que deve continuar enquanto o estoque for maior que 0.

estoque = 5

while estoque > 0:
    estoque -= 1
    print(f'Venda realizada! Estoque Restante: {estoque}')

print('Estoque esgotado')