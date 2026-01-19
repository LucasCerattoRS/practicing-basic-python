class Contador:
#Classe que representa um contador.
#A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    contador_global = 0

# Função do __init__: Executado automaticamente ao criar uma instância; Inicializa o estado individual do objeto.

    def __init__(self):
        self.valor = 0

# O método __init__ é conhecido como o construtor da classe em Python. 
# Ele é automaticamente chamado quando uma nova instância da classe é criada e serve para realizar as inicializações necessárias nos atributos da instância. 
# O nome __init__ é uma abreviação de initialize (inicializar), e sua principal função é garantir que os atributos da instância tenham valores iniciais apropriados.

# self.valor: É um atributo de instância; Cada objeto possui seu próprio valor; Alterar um não afeta os outros.

    def __str__(self):
        return f'Contador: {self.valor}'
    
# O método str retorna uma string que contém uma representação legível da instância, incluindo o valor atual do contador. #
# Define como o objeto será representado em texto.

    def incrementar(self):
        self.valor += 1

# Atua somente no objeto
# Modifica o estado interno (self.valor)
# Não interfere em outros contadores

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        return 'Contador global foi zerado.'
    
# O método não opera sobre um objeto específico: Ele atua sobre a classe como um todo
# O parâmetro cls representa a própria classe


# A ideia central (guarde isso)

# Classe é o molde.
# Instância é o objeto criado a partir do molde.
# Objeto e instância, na prática, são a mesma coisa.


# O que muda é o ponto de vista:

# instância → termo técnico (algo foi instanciado)
# objeto → o que você usa no código



# Trazendo isso para o código Contador
# A classe (o molde)
# class Contador:

# Aqui não tem um contador real ainda.
# só descreveu: quais dados existirão;
# quais comportamentos existirão;
