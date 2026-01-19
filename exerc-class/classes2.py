# Cliente: classe com 4 atributos; instanciar 3 objetos via construtor
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome}, {self.idade} anos — {self.email} / {self.telefone}'

# criar 3 instâncias de Cliente
cliente1 = Cliente('Ana Silva', 28, 'ana.silva@example.com', '(11) 99999-0001')
cliente2 = Cliente('Bruno Costa', 35, 'bruno.costa@example.com', '(11) 99999-0002')
cliente3 = Cliente('Carla Pereira', 22, 'carla.pereira@example.com', '(11) 99999-0003')

print('\nClientes:')
print(cliente1)
print(cliente2)
print(cliente3)