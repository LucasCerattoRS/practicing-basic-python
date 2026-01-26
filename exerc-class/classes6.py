# Restaurante: com dois atributos adicionais (endereco, capacidade)
class Restaurante:
    restaurantes = []  # lista de todas as instâncias

    # construtor: aceita nome e categoria; ativo inicia False por padrão
    def __init__(self, nome, categoria, endereco='', capacidade=0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.capacidade = capacidade
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    # método especial para representação em string
    def __str__(self):
        return f'{self.nome} — {self.categoria} (Ativo: {self.ativo})'

    @classmethod
    def listar_restaurantes(cls):
        for r in cls.restaurantes:
            print(r)

# instanciar usando o construtor
restaurante1 = Restaurante('Pizza Express', 'Italiana', endereco='Av. Central, 100', capacidade=60)
print('Restaurante:', restaurante1)  # __str__ será exibido

# mostrar todos os restaurantes cadastrados
print('\nLista de restaurantes cadastrados:')
Restaurante.listar_restaurantes()
