x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x == 0 and y == 0:
    print("O ponto está na origem.")
elif x == 0:
    print("O ponto está sobre o eixo Y.")
elif y == 0:
    print("O ponto está sobre o eixo X.")
elif x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
else:
    print("O ponto está no quarto quadrante.")

#        ↑ y
#        |
#   2    |    1
#        |
#--------+--------→ x
#        |
#   3    |    4
#        |
