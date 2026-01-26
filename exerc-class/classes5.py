# Uma classe chamada Pessoa com atributos: nome, idade e profissão. 
# Um método especial __str__ para imprimir uma representação em string da pessoa. 
# Tem também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adiciona uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    pessoas = []

    def __init__(self, nome: str, idade: int, profissao:str):
        self.nome = nome
        self.idade = int(idade)
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'
    
# @property serve para acessar um método como se fosse um atributo, preservando encapsulamento, legibilidade e controle sobre o acesso aos dados do objeto.
# Ele transforma um método em um atributo de leitura.
# Exemplo: ao invés de chamar pessoa.saudacao(), você pode simplesmente usar pessoa.saudacao.
    @classmethod
    def listar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(pessoa)

    def aniversario(self):
        self.idade += 1

# @property serve para acessar um método como se fosse um atributo, preservando encapsulamento, legibilidade e controle sobre o acesso aos dados do objeto.
# Ele transforma um método em um atributo de leitura.
# Exemplo: ao invés de chamar pessoa.saudacao(), você pode simplesmente usar pessoa.saudacao.
    @property
    def saudacao(self):
        return f'Olá, meu nome é {self.nome} e trabalho como {self.profissao}'   

# Essa estrutura verifica se o arquivo está sendo executado diretamente ou sendo importado como módulo.
# Se estiver sendo executado diretamente, o código dentro desse bloco será executado.
# Isso é útil para testar ou demonstrar funcionalidades específicas do módulo sem afetar outros módulos que possam importá-lo.
if __name__ == '__main__':
    pessoa1 = Pessoa('Rodrigo', 44, 'Gerente Financeiro')
    pessoa2= Pessoa('Ana', 30, 'Engenheira')


    pessoa1.aniversario()
    pessoa2.aniversario()
    Pessoa.listar_pessoas()
    