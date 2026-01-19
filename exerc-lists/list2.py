import os

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
anos = [1990, 1985, 2000, 1995, 1980]


def exibir_main(texto):
    os.system('cls')
    print(texto)
    print()


def numeros_lista():
    exibir_main('Lista de Números')
    for numero in numeros:
        print(f'- {numero}')
    input('\nPressione Enter para voltar ao menu...')


def nomes_lista():
    exibir_main('Lista de Nomes')
    for nome in nomes:
        print(f'- {nome}')
    input('\nPressione Enter para voltar ao menu...')


def anos_lista():
    exibir_main('Lista de Anos')
    for ano in anos:
        print(f'- {ano}')
    input('\nPressione Enter para voltar ao menu...')


def exibir_opcoes():
    print('1. Números')
    print('2. Nomes')
    print('3. Anos')
    print('\n4. Finalizar Sistema\n')


def escolher_opcao():
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        return None


def main():
    while True:
        exibir_main('MENU PRINCIPAL')
        exibir_opcoes()
        opcao = escolher_opcao()

        if opcao == 1:
            numeros_lista()
        elif opcao == 2:
            nomes_lista()
        elif opcao == 3:
            anos_lista()
        elif opcao == 4:
            exibir_main('Finalizando o programa... Até mais!')
            break
        else:
            print('Opção inválida!')
            input('Pressione Enter para tentar novamente...')


if __name__ == '__main__':
    os.system('cls')
    main()