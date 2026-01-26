# Importa o módulo 'os', que fornece funções para interagir com o sistema operacional.
# Neste código, será usado para limpar a tela do terminal.
import os

# Listas com dados de exemplo
numeros = [10, 20, 30, 40, 50]  # Lista de números
nomes = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']  # Lista de nomes
anos = [1995, 2000, 2005, 2010, 2015]  # Lista de anos

# Função para limpar a tela e exibir o texto de título
def exibir_main(texto): 
    os.system('cls')  # Limpa a tela (no Windows. Para Linux/Mac, seria 'clear')
    print(texto)  # Exibe o texto recebido como argumento
    print()  # Adiciona uma linha em branco para espaçamento

# Função para exibir a lista de números
def numeros_lista():
    exibir_main('Lista de Números')  # Exibe o título da seção
    for numero in numeros:  # Loop para percorrer e imprimir cada número da lista
        print(f'- {numero}')  # Imprime o número com um hífen para formatação
    input('\nPressione Enter para voltar ao menu...')  # Aguarda o usuário pressionar Enter para voltar ao menu

# Função para exibir a lista de nomes
def nomes_lista():
    exibir_main('Lista de Nomes')  # Exibe o título da seção
    for nome in nomes:  # Loop para percorrer e imprimir cada nome da lista
        print(f'- {nome}')  # Imprime o nome com um hífen para formatação
    input('\nPressione Enter para voltar ao menu...')  # Aguarda o usuário pressionar Enter para voltar ao menu

# Função para exibir a lista de anos
def anos_lista():
    exibir_main('Lista de Anos')  # Exibe o título da seção
    for ano in anos:  # Loop para percorrer e imprimir cada ano da lista
        print(f'- {ano}')  # Imprime o ano com um hífen para formatação
    input('\nPressione Enter para voltar ao menu...')  # Aguarda o usuário pressionar Enter para voltar ao menu

# Função para exibir as opções do menu principal
def exibir_opcoes():
    print('1. Números')  # Opção para ver a lista de números
    print('2. Nomes')  # Opção para ver a lista de nomes
    print('3. Anos')  # Opção para ver a lista de anos
    print('\n4. Finalizar Sistema\n')  # Opção para finalizar o programa

# Função para capturar a opção escolhida pelo usuário
def escolher_opcao():
    try:
        # Tenta converter a entrada do usuário para um número inteiro
        return int(input('Escolha uma opção: '))
    except ValueError:
        # Se a entrada não for válida (não for um número), retorna None
        return None

# Função principal que controla o fluxo do programa
def main():
    while True:  # Loop infinito para manter o menu ativo até que o usuário escolha finalizar
        exibir_main('MENU PRINCIPAL')  # Exibe o título do menu principal
        exibir_opcoes()  # Exibe as opções do menu
        opcao = escolher_opcao()  # Obtém a opção escolhida pelo usuário
        if opcao == 1:
            numeros_lista()  # Se a opção for 1, exibe a lista de números
        elif opcao == 2:
            nomes_lista()  # Se a opção for 2, exibe a lista de nomes
        elif opcao == 3:
            anos_lista()  # Se a opção for 3, exibe a lista de anos
        elif opcao == 4:
            # Se a opção for 4, exibe uma mensagem de finalização e encerra o programa
            exibir_main('Finalizando o programa... Até mais!')
            break  # Interrompe o loop e finaliza o programa
        else:
            # Caso o usuário digite uma opção inválida, exibe uma mensagem de erro
            print('Opção inválida! Tente novamente.\n')
            input('Pressione Enter para tentar novamente...')  # Aguarda o usuário pressionar Enter para tentar novamente

# Verifica se o script está sendo executado diretamente (não importado)
if __name__ == '__main__':
    os.system('cls')  # Limpa a tela antes de iniciar
    main()  # Chama a função principal para rodar o programa
