# Carro: classe com atributos básicos e instância
# O que é __init__: É chamado automaticamente quando você cria um objeto; Serve para inicializar o estado do objeto.
class Carro:
    def __init__(self, modelo='', cor='', ano=None):
# Didaticamente: “O carro pode nascer vazio e ser preenchido depois.”
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
# Para que serve __str__: Ele define como o objeto será exibido quando convertido em texto.
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

# criar uma instância e atribuir valores via construtor
carro1 = Carro('Gol', 'Prata', 2010)
print('Carro:', carro1)  # Saída formatada via __str__