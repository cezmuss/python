"""
Avaliação Somativa 3

Questão 1:

Você foi contratado pelo restaurante Boca Feliz para participar do
desenvolvimento de um pequeno controle de estoque de ingredientes
iniciado em Python. O sistema já possui desenvolvido um dicionário
chamado estoque, no qual consta a lista de ingredientes com suas
respectivas quantidades. Também possui outro dicionário chamado cardapio,
no qual constam todos os ingredientes que compõe cada produto
servido no restaurante. Tais estruturas são mostradas a seguir:

estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

Sua primeira tarefa de programador consiste em desenvolver as seguintes
funcionalidades do sistema:

-Imprimir o cardápio do restaurante com as opções de produtos ofertados;
-Logo abaixo do cardápio, exibir a mensagem “O que deseja pedir (0 para sair)?”
-Digitando “0” deve sair do programa;
-Digitando o nome do produto pode ter uma das seguintes possibilidades:
-Se o item não consta no cardápio exibir a mensagem “Item não localizado no
cardápio”;
-Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma
mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”;
-Se for possível produzir o produto, reduzir as quantidades de estoque e
mostrar a mensagem “um {produto} saindo no capricho!!!”. O programa deve
continuar fazendo os pedidos até que o usuário decida sair do mesmo.

O restaurante Boca Feliz conta com você!!!
"""


def main():
    """
    Ponto de entrada do Módulo

    :return: Função de adquirimento do produto
    """
    estoque = {'pao': 1, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
    cardapio = {
        'x-burguer': ['pao', 'hamburguer'],
        'x-salada': ['pao', 'hamburguer', 'tomate'],
        'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
        'x-egg': ['pao', 'hamburguer', 'ovo'],
        'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
    }
    print("\n----- Bem Vindo ao Restaurante Boca Feliz -----")
    return menu(estoque, cardapio)


def menu(estoque: dict, cardapio: dict):
    """
    Cliente compra o lanche

    :param estoque: Estoque em formato de Dicionário
    :param cardapio: Cardápio em formato de Dicionário
    :return: None
    """
    show_menu(cardapio)
    while True:
        lanche = input("O que deseja pedir (0 para sair)? ")
        if lanche == "0":
            print("Obrigado, Volte Sempre!!")
            exit()
        elif lanche not in cardapio.keys():
            print("Item não localizado no cardápio")
            continue
        else:
            for ingrediente in cardapio[lanche]:
                if ingrediente in estoque:
                    if estoque[ingrediente] == 0:
                        print(f"Infelizmente acabou o {ingrediente}")
                        return menu(estoque, cardapio)
                    else:
                        estoque[ingrediente] -= 1
            print(f"Um {lanche} saindo no capricho!!!")
            continue


def show_menu(cardapio: dict):
    """
    Imprime o menu de lanches

    :param cardapio: Cardápio em formato de Dicionário
    :return: None
    """
    print("\nCardápio Restaurante Boca Feliz")
    for k, v in cardapio.items():
        print(f"Item: {k:9} / Ingredientes: {v}")


if __name__ == '__main__':  # Abre a função principal
    main()
