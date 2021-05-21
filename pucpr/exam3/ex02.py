"""
Avaliação Somativa 3

Questão 2:

Como navegador de uma nave interestelar da frota Alfa, uma de suas principais
funções é calcular as distâncias no espaço. Para isto, realizar rapidamente
conversão de unidades de tempo é uma habilidade fundamental em seu trabalho.
Assim sendo, a fim de facilitar seu próprio trabalho, você, programador em
linguagem Python, decide desenvolver seu próprio conversor unidades de tempo
em deslocamento no espaço. Para tanto, consegue as seguintes informações de
base para seu programa: um dicionário chamado ano_luz, que tem os valores das
demais unidades de tempo convertidos para valor em anos luz, e uma lista
chamada unidades com o nome e abreviações das unidades de tempo, como segue:

ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}

unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)",
"Minuto-Luz (ml)", "Segundo-Luz (sl)"]

Desta forma, sua tarefa é desenvolver um programa com as seguintes
funcionalidades:

-Imprimir a lista de unidades de conversão
-Solicitar o valor que se deseja converter usando a frase “Valor a ser
convertido:”
-Solicitar a unidade origem do valor usando a frase “Converter de: ”
-Solicitar a unidade destino de conversão usando a frase “Converter para: ”
-Exibir o valor convertido com a frase
“Conversão: {valor} {unidade origem} = {valor} {unidade destino}”

A frota Alfa conta com você, oficial navegador!!!
"""


def main():
    """
    Ponto de Entrada do Módulo

    :return: None
    """
    ano_luz = {
        "pc": 0.31,
        "al": 1,
        "ae": 63241.09,
        "ml": 525960.23,
        "sl": 31557609.92
    }
    unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)",
                "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
    while True:
        op = menu()
        if op == 1:
            show_unidades(unidades)
        elif op == 2:
            convert(ano_luz)
        else:
            break


def menu():
    """
    Menu do Programa

    :return: Função que pega valor inteiro para seleção de opção
    """
    print("\n----- Sistema de Conversão de Unidades -----")
    print("1. Listar Unidades")
    print("2. Converter Valores")
    print("3. Sair")
    return get_int_value_with_range("Digite uma das opções", 1, 3)


def show_unidades(unidades):
    """
    Mostra as Unidades

    :param unidades: Lista contendo o Nome e as Siglas das Unidades
    :return: None
    """
    print("\n----- Lista das Unidades -----")
    for u in unidades:
        print(u)


def convert(ano_luz):
    """
    Faz a conversão dos valores

    :param ano_luz: Dicionário contendo as Unidades
    :return: None
    """
    while True:
        valor = float(input("\nValor a ser convertido: "))
        origem = input("Converter de: ")
        if origem in ano_luz.keys():
            destino = input("Converter para: ")
            if destino in ano_luz.keys():
                if ano_luz[origem] == ano_luz[destino]:
                    print(f"Conversão {valor} {origem} = {valor} {destino}")
                elif ano_luz[origem] > ano_luz[destino]:
                    converter = valor / (ano_luz[origem] / ano_luz[destino])
                    print(f"Conversão "
                          f"{valor} {origem} = {converter:2} {destino}")
                else:
                    converter = valor * (ano_luz[destino] / ano_luz[origem])
                    print(f"Conversão "
                          f"{valor} {origem} = {converter:2} {destino}")
            else:
                print("Nenhuma Unidade com essa Sigla")
        else:
            print("Nenhuma Unidadade com essa Sigla")



def get_int_value_with_range(message: str, min_value: int, max_value: int) \
        -> int:
    """
    Valida dados inteiros em um determinado range

    :param message: A mensagem a ser exibida
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna a opção escolhida dentro do range
    """
    while True:
        try:
            op = int(input(message + ": "))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print(f"Opção inválida: escolha um número de "
                  f"{min_value} a {max_value}")
        else:
            return op


if __name__ == '__main__':  # Abre a função principal
    main()
