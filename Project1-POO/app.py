# “Executa este bloco apenas se este arquivo for o programa principal.”

from sub.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

restaurante_mexicano = Restaurante('exican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alernar_estados()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()