"""
Sistema de venda de Veículos

Estrutura dos dicionários

cart = {
    id: "10",
    plate: {
        amount: "1",
        price: "29999"
    }
}

sales = {
    id_venda: {
        id: "10",
        plate: {
            amount: "1",
            price: "29999"
        }
    }
}
"""

import Utilidades as util
import Clientes as c
import Produtos as p

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


def main():
    """
    Ponto de entrada do módulo

    :return: None
    """
    clients = {"10": {
        c.CONST_FIELD_NAME: "Cézar",
        c.CONST_FIELD_CITY: "Curitiba",
        c.CONST_FIELD_AGE: "18"
    }
    }
    products = {"ABC-0001": {
        CONST_FIELD_BRAND: "Ford",
        CONST_FIELD_MODEL: "KA",
        CONST_FIELD_COLOR: "Rosa",
        CONST_FIELD_YEAR: 1999,
        CONST_FIELD_CATEG: "F",
        CONST_FIELD_SIZE: "Compacto",
        CONST_FIELD_DESC: "Motor DURATEC 2.0",
        CONST_FIELD_PRICE: 25000,
        CONST_FIELD_AMOUNT: 1
    },
        "ABC-1234": {
            CONST_FIELD_BRAND: "Ford",
            CONST_FIELD_MODEL: "Fiesta",
            CONST_FIELD_COLOR: "Vermelho",
            CONST_FIELD_YEAR: 1996,
            CONST_FIELD_CATEG: "F",
            CONST_FIELD_SIZE: "Compacto",
            CONST_FIELD_DESC: "Motor DURATEC 2.0",
            CONST_FIELD_PRICE: 29999,
            CONST_FIELD_AMOUNT: 1
        },
        "CWB-0001": {
            CONST_FIELD_BRAND: "Hyundai",
            CONST_FIELD_MODEL: "HB20",
            CONST_FIELD_COLOR: "Vermelho",
            CONST_FIELD_YEAR: 2013,
            CONST_FIELD_CATEG: "C",
            CONST_FIELD_SIZE: "Compacto",
            CONST_FIELD_DESC: "Nada",
            CONST_FIELD_PRICE: 34500,
            CONST_FIELD_AMOUNT: 1
        }
    }
    sales = {}  # Registro das vendas em formato de dicionário
    cart = {}  # Carrinho em formato de dicionário
    id_sell = 1
    while True:
        op = menu()
        if op == 1:  # Gerenciar Clientes
            c.main(clients)
        elif op == 2:  # Gerenciar Produtos
            p.main(products)
        elif op == 3:  # Adicionar Item no Carrinho
            resp, msg = reg_purchase(clients, products, cart)
            print(msg)
        elif op == 4:  # Ver Carrinho
            show_cart(cart)
        elif op == 5:  # Finalizar pedido atual
            resp, msg = end_purchase(products, cart, sales, id_sell)
            print(msg)
        elif op == 6:  # Cancelar pedido
            resp, msg = cancel_purchase(sales)
            print(msg)
        elif op == 7:  # Relatório de Pedidos
            purchase_historic(sales)
        elif op == 8:  # Relatório de Pedidos por Cliente
            purchase_historic_byc(sales)
        elif op == 9:  # Sair do Módulo
            break


def menu():
    """
    Exibe o menu de opções

    :return: Função de módulo auxiliar que pega um valor inteiro em um alcance
    """
    print("\n**** Concessionárias CZAR ****")
    print("1. Gerenciar Clientes")
    print("2. Gerenciar Produtos")
    print("3. Adicionar Item")
    print("4. Ver Carrinho")
    print("5. Finalizar Pedido")
    print("6. Cancelar Pedido")
    print("7. Relatório de Pedidos")
    print("8. Relatório de Pedidos por Cliente")
    print("9. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções", 1, 9)


def reg_purchase(clients, products, cart):
    """
    Adicionar Item no Carrinho

    :param clients: Database dos clientes em formato de dicionário
    :param products: Database dos produtos em formato de dicionário
    :param cart: Carrinho em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    id = input("\nDigite o CPF do cliente: ")
    if id not in clients:
        return False, "Cliente não cadastrado"
    else:
        p.list_products(products)
        plate = input("\nDigite a placa do veículo para adicioná-lo"
                      " no carrinho, digite 0 para sair: ").upper()
        if plate == '0':
            return False, "Operação Cancelada. Nada alterado"
        elif plate not in products:
            return False, "Veículo não cadastrado"
        elif plate in cart:
            return False, "Produto já adicionado ao carrinho"
        else:
            cart[id] = {plate: products[plate]}
            return True, "Produto adicionado no carrinho"


def show_cart(cart):
    """
    Mostrar Carrinho de compras atual

    :param cart: Carrinho em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    if len(cart) == 0:
        print("\nCarrinho vazio")
    else:
        print("\nPlaca", 3 * " ", "Quantidade", 3 * " ", "Valor")
        for id in cart:
            for plate in cart[id]:
                carrinho = cart[id][plate]
                total = carrinho[CONST_FIELD_PRICE]
                total *= len(cart)
                print(f'{plate}: {carrinho[CONST_FIELD_AMOUNT]:5}'
                      f'{carrinho[CONST_FIELD_PRICE]:15}')
                print(f"Quantidade de itens no carrinho: {len(cart)}")
                print(f"Valor total: {total}")


def end_purchase(products, cart, sales, id_sell):
    """
    Finaliza a venda

    :param products: Database dos produtos em formato de dicionário
    :param cart: Carrinho em formato de dicionário
    :param sales: Registro das Vendas em formato de dicionário
    :param id_sell: ID de Registro de Venda en formato de dicionário
    :return: Mensagem de resultado da operação
    """
    show_cart(cart)
    purchase = util.get_yes_no_value("Certeza que deseja finalizar a compra")
    if purchase == 'S':
        sales[id_sell] = cart.copy()
        id_sell += 1
        cart.clear()
        for plate in products:
            products.pop(plate)
        return id_sell, "Compra finalizada"
    else:
        return False, "Operação Cancelada. Nada alterado"


def cancel_purchase(sales):
    """
    Cancela a venda

    :param sales: Registro das Vendas em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    id_venda = input(f"Digite o número da venda para a "
                     f"cancelar, digite 0 para sair: ")
    if id_venda == '0':
        return False, "Operação Cancelada. Nada alterado"
    else:
        if id_venda in sales:
            sales.pop(id_venda)
            return True, "Venda Cancelada"
        else:
            return False, "Nenhuma venda registrada com esse código"


def purchase_historic(sales):
    """
    Relatório de Pedidos / Vendas

    :param sales: Registro das Vendas em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    for id_sell in sales:
        for id in sales[id_sell]:
            for plate in sales[id_sell][id]:
                venda = sales[id_sell][id][plate]
                print("ID Venda:  CPF", 6 * " ", "Placa",
                      3 * " ", "Marca", 3 * " ", "Modelo", 2 * " ",
                      "Cor", 6 * " ", "Ano", 1 * " ", "Categ.", 1 * " ",
                      "Porte", 3 * " ", "Descrição", 21 * " ", "Estoque ",
                      "Valor")
                print(f"{id_sell}:         {id:11}"
                      f"{plate:10}{venda[CONST_FIELD_BRAND]:10}"
                      f"{venda[CONST_FIELD_MODEL]:10}"
                      f"{venda[CONST_FIELD_COLOR]:9}"
                      f"{venda[CONST_FIELD_YEAR]:6}  "
                      f"{venda[CONST_FIELD_CATEG]:3}", 4 * " ",
                      f"{venda[CONST_FIELD_SIZE]:10}"
                      f"{venda[CONST_FIELD_DESC]:30}"
                      f"{venda[CONST_FIELD_AMOUNT]:6}", 3 * " ",
                      f"{venda[CONST_FIELD_PRICE]}")


def purchase_historic_byc(sales):
    """
    Relatório de Pedidos / Vendas por Cliente

    :param sales: Registro das Vendas em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    for id_sell in sales:
        for id in sales[id_sell]:
            for plate in sales[id_sell][id]:
                venda = sales[id_sell][id][plate]
                print("CPF:", 6 * " ", "ID Venda", 2 * " ", "Placa",
                      3 * " ", "Marca", 3 * " ", "Modelo", 2 * " ",
                      "Cor", 6 * " ", "Ano", 1 * " ", "Categ.", 1 * " ",
                      "Porte", 3 * " ", "Descrição", 21 * " ", "Estoque ",
                      "Valor")
                print(f"{id:3}:{id_sell:12}        "
                      f"{plate:10}{venda[CONST_FIELD_BRAND]:10}"
                      f"{venda[CONST_FIELD_MODEL]:10}"
                      f"{venda[CONST_FIELD_COLOR]:9}"
                      f"{venda[CONST_FIELD_YEAR]:6}  "
                      f"{venda[CONST_FIELD_CATEG]:3}", 4 * " ",
                      f"{venda[CONST_FIELD_SIZE]:10}"
                      f"{venda[CONST_FIELD_DESC]:30}"
                      f"{venda[CONST_FIELD_AMOUNT]:6}", 3 * " ",
                      f"{venda[CONST_FIELD_PRICE]}")


if __name__ == '__main__':
    main()
