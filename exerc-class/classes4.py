class Musica:
    # “Toda vez que eu criar uma música, quero guardá-la em um lugar comum.”
    musicas = []

    # __init__ é chamado automaticamente quando você faz:

    # musica1 = Musica()

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    # Musica.musicas.append(self):

    # Adiciona essa instância na lista da classe

    # É isso que permite listar todas depois

    # self representa o objeto que está sendo criado

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

Musica.listar_musicas()


# Isso é um padrão comum em POO (Programação Orientada a Objetos) para simular um “banco de dados em memória”.


# Pense assim:

# 1️⃣ A classe define o modelo
# 2️⃣ O __init__ cria objetos baseados nesse modelo
# 3️⃣ Cada objeto se registra automaticamente na lista da classe
# 4️⃣ Um método da classe percorre essa lista
# 5️⃣ Os dados são exibidos
