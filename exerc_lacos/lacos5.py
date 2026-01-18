projetos = ["Website", "Jogo", "Análise de dados", None, "Aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)