from sub.avaliacao import Avaliacao

class Restaurante:
    # “Toda vez que eu criar um restaurante, quero guardá-lo em um lugar comum.”
    restaurantes = []
#  O método __init__ é chamado automaticamente quando uma nova instância de uma classe é criada. Serve como o construtor da classe, sendo executado imediatamente após a instância ter sido criada. #
# ! O self em Python é uma convenção que representa a instância da própria classe, utilizado como o primeiro parâmetro em métodos de instância, ou seja, métodos pertencentes a objetos específicos da classe #
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
# A lista restaurantes é um atributo da classe Restaurante. A linha de código Restaurante.restaurantes.append(self), adiciona automaticamente a instância atual da classe Restaurante à lista restaurantes, que é um atributo de classe, porque é definida diretamente dentro do escopo da classe e fora de qualquer método específico. #
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(
            f"{'Nome do Restaurante'.ljust(25)} | "
            f"{'Categoria'.ljust(25)} | "
            f"{'Avaliação'.ljust(25)} | "
            f"{'Status'.ljust(25)}"
        )

        for restaurante in cls.restaurantes:
            media = str(restaurante.media_avaliacoes).ljust(25)
            status = restaurante.ativo.ljust(25)

            print(
                f'{restaurante._nome.ljust(25)} | '
                f'{restaurante._categoria.ljust(25)} | '
                f'{media} | '
                f'{status}'
            )

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐' 
    
    def alernar_estados(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

# com o property somos capazes de ler as informações
    @property
    def media_avaliacoes(self):
        # se não tiver avaliação retorna 0
        if not self._avaliacao:
            return '-'
        # soma utilizando o sum, cada avaliacao da lista a gente só pega a nota
        soma_das_notas= sum(avaliacao._nota for avaliacao in self._avaliacao)
        # depois contamos a quantidade de notas que temos
        quantidade_de_notas = len(self._avaliacao)
        # e pra finalizar, pegamos a media e exibimos o valor com uma casa decimal, descrito abaixo com o comando round e o numero de casas decimais 
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

