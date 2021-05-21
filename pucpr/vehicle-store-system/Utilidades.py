"""
Módulo de funções úteis
"""


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


def get_yes_no_value(message: str) -> ():
    """
    Valida opções de sim e não

    :param message: A mensagem a ser exibida
    :return: Retorna a opção escolhida S/N
    """
    while True:
        op = input(message + " [S/N]? ").upper()
        if op == 'S' or op == 'N':
            return op
        else:
            print("Opção inválida: escolha Sim [S] ou Não [N]")


def min_max_characters(message: str, min_value: int, max_value: int) -> ():
    """
    Valida um mínimo e um máximo de caracteres que podem ser inseridos

    :param message: A mensagem a ser exibida
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna o texto inserido
    """
    while True:
        op = input(message + ": ")
        if min_value == max_value:
            if not min_value <= len(op) <= max_value:
                print(f"Obrigatório inserir {max_value} caracteres")
            else:
                return op.upper()
        else:
            if not min_value <= len(op) <= max_value:
                print(f"Digite no mínimo {min_value} e "
                      f"no máximo {max_value} caracteres")
            else:
                return op.title()
