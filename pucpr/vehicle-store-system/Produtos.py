"""
Sistema de gerenciamento de produtos (Véiculos)
"""

import Utilidades as util
import Sistema as s

# Definição de Constantes para evitar erros
CONST_FIELD_PLATE = "plate"
CONST_FIELD_BRAND = "brand"
CONST_FIELD_MODEL = "model"
CONST_FIELD_COLOR = "color"
CONST_FIELD_YEAR = "year"
CONST_FIELD_CATEG = "category"
CONST_FIELD_SIZE = "size"
CONST_FIELD_DESC = "desc"
CONST_FIELD_AMOUNT = "amount"
CONST_FIELD_PRICE = "price"


def main(products):
    """
    Ponto de entrada do módulo

    :param products: Database em formato de dicionário
    :return: None
    """
    while True:
        op = menu()
        if op == 1:  # Cadastrar produto
            resp, msg = register_product(products)
            print(msg)
        elif op == 2:  # Alterar dados dos produtos
            resp, msg = mod_product(products)
            print(msg)
        elif op == 3:  # Remover produtos
            resp, msg = del_product(products)
            print(msg)
        elif op == 4:  # Pesquisar produtos
            search_product(products)
        elif op == 5:  # Listar produtos
            list_products(products)
        elif op == 6:  # Sair do módulo
            break


def menu():
    """
    Exibe o menu de opções

    :return: Função de módulo auxiliar que pega um valor inteiro em um alcance
    """
    print("\n*** Sistema de Cadastro de Produtos ***")
    print("1. Cadastrar Produtos")
    print("2. Alterar Produtos")
    print("3. Remover Produto")
    print("4. Pesquisar Produtos")
    print("5. Listar Produtos")
    print("6. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções", 1, 6)


def register_product(products):
    """
    Cadastra novos veículos no sistema

    :param products: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    plate = util.min_max_characters("Digite a placa do veículo", 8, 8)
    if plate in products:
        op = util.get_yes_no_value("Veículo já cadastrado. "
                                   "Deseja alterar seus dados")
        if op == 'S':
            reg_mod_produts(plate, products)
            return True, "Veículo alterado com sucesso"
        else:
            return False, "Cadastro não foi realizado. Veículo já existente"
    else:
        reg_mod_produts(plate, products)
        return True, "Veículo cadastrado com sucesso"


def mod_product(products):
    """
    Altera dados dos veículos

    :param products: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    plate = util.min_max_characters("Digite a placa do veículo", 8, 8)
    if plate in products:
        reg_mod_produts(plate, products)
        return True, "Veículo alterado com sucesso"
    else:
        op = util.get_yes_no_value("Nenhum veículo com essa placa. "
                                   "Deseja cadastrá-lo")
        if op == 'S':
            reg_mod_produts(plate, products)
            return True, "Veículo cadastrado com sucesso"
        else:
            return False, "Nenhum veículo foi localizado"


def del_product(products):
    """
    Exclui veículos cadastrados

    :param products: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    plate = util.min_max_characters("Digite a placa do veículo", 8, 8)
    if plate in products:
        print(f"Os dados atuais do veículo com placa {plate} são:"
              f" {products[plate]}")
        op = util.get_yes_no_value("Deseja excluir esse veículo")
        if op == 'S':
            del products[plate]
            return True, "Veículo Excluido"
        else:
            return False, "Nada foi alterado"
    else:
        return False, "Nenhum veículo com essa placa"


def search_product(products):
    """
    Procura por veículos cadastrados

    :param products: Database em formato de dicionário
    :return: None
    """
    plate = util.min_max_characters("Digite a placa do veículo", 8, 8)
    if plate in products:
        # Imprime as informações do veículo
        print(f"Marca do veículo: {products[plate][CONST_FIELD_BRAND]}")
        print(f"Modelo do veículo: {products[plate][CONST_FIELD_MODEL]}")
        print(f"Cor do veículo: {products[plate][CONST_FIELD_COLOR]}")
        print(f"Ano do veículo: {products[plate][CONST_FIELD_YEAR]}")
        print(f"Categoria do veículo: {products[plate][CONST_FIELD_CATEG]}")
        print(f"Porte (tamanho) do veículo: "
              f"{products[plate][CONST_FIELD_SIZE]}")
        print(f"Descrição do produto: {products[plate][CONST_FIELD_DESC]}")
        print(f"Estoque do produto: {products[plate][CONST_FIELD_AMOUNT]}")
        print(f"Preço do veículo: {products[plate][CONST_FIELD_PRICE]}")
    else:
        op = util.get_yes_no_value("Veículo não encontrado. "
                                   "Deseja cadastrá-lo")
        if op == 'S':
            reg_mod_produts(plate, products)
        else:
            print("Veículo não encontrado")


def list_products(products):
    """
    Lista os veículos cadastrados

    :param products: Database em formato de dicionário
    :return: None
    """
    if len(products) < 0:
        print("Nenhum produto cadastrado no sistema")
    else:
        print("\n****** Produtos Cadastrados ******")
        print("Placa", 3*" ", "Marca", 3*" ", "Modelo", 2*" ",
              "Cor", 6*" ", "Ano", 1*" ", "Categ.", 1*" ",
              "Porte", 3*" ", "Descrição", 21*" ", "Estoque ",
              "Valor")
        for key in products:
            product = products[key]
            print(f"{key}: {product[CONST_FIELD_BRAND]:10}"
                  f"{product[CONST_FIELD_MODEL]:10}"
                  f"{product[CONST_FIELD_COLOR]:9}"
                  f"{product[CONST_FIELD_YEAR]:6}  "
                  f"{product[CONST_FIELD_CATEG]:3}", 4*" ",
                  f"{product[CONST_FIELD_SIZE]:10}"
                  f"{product[CONST_FIELD_DESC]:30}"
                  f"{product[CONST_FIELD_AMOUNT]:6}", 3*" ",
                  f"{product[CONST_FIELD_PRICE]}")


def reg_mod_produts(plate, products):
    """
    Função Auxiliar do cadastro / alteração de dados

    :param plate: Placa do veículo
    :param products: Database em formato de dicionário
    :return: None
    """
    brand = util.min_max_characters("Digite a marca do veículo", 2, 9)
    model = util.min_max_characters("Digite o modelo do veículo", 2, 9)
    color = util.min_max_characters("Digite a cor do veículo", 2, 9)
    year = util.get_int_value_with_range("Digite o ano do veículo", 1886, 2021)
    category = util.min_max_characters('Digite a categoria do veículo', 1, 1)
    size = util.min_max_characters("Digite o porte (tamanho) do veículo", 2, 9)
    desc = util.min_max_characters("Digite uma descrição "
                                   "curta do produto", 0, 28)
    amount = util.get_int_value_with_range("Estoque do produto", 0, 50)
    price = util.get_int_value_with_range("Digite o valor (em reais) "
                                          "do veículo", 0, 100000000)
    products[plate] = {
        CONST_FIELD_BRAND: brand,
        CONST_FIELD_MODEL: model,
        CONST_FIELD_COLOR: color,
        CONST_FIELD_YEAR: year,
        CONST_FIELD_CATEG: category,  # Atualiza / Cria o cadastro do veículo
        CONST_FIELD_SIZE: size,
        CONST_FIELD_DESC: desc,
        CONST_FIELD_AMOUNT: amount,
        CONST_FIELD_PRICE: price
    }


if __name__ == '__main__':  # Abre a função principal
    main()
