"""
Exemplo de uso de funções para cadastro
Uso de Dicionários como banco de dados
Estrutura:

clients {
    id : {
        name: ,
        city: ,
        age:
    }
}
"""

import Utilidades as util

# Definição de Constantes para evitar erros
CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


def main(clients):
    """
    Ponto de entrada do módulo

    :param clients: Database em formato de dicionário
    :return: None
    """
    while True:
        op = menu()
        if op == 1:  # Cadastrar cliente
            resp, msg = client_add(clients)
            print(msg)
        elif op == 2:  # Alterar dados do cliente
            resp, msg = client_edit(clients)
            print(msg)
        elif op == 3:  # Excluir cliente
            resp, msg = client_del(clients)
            print(msg)
        elif op == 4:  # Pesquisar clientes
            client_query(clients)
        elif op == 5:  # Zerar banco de dados
            resp, msg = database_clear(clients)
            print(msg)
            if resp:
                r = util.get_yes_no_value("Deseja cadastrar um cliente")
                if r == 'S':
                    client_add(clients)
        elif op == 6:  # Sair do módulo
            break


def menu():
    """
    Exibe o menu de opções

    :return: Função de módulo auxiliar que pega um valor inteiro em um alcance
    """
    print("\n*** Sistema de Cadastro de Clientes ***")
    print("1. Cadastrar cliente")
    print("2. Alterar dados de cliente")
    print("3. Excluir cliente")
    print("4. Pesquisar cliente")
    print("5. Zerar banco de dados")
    print("6. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções", 1, 6)


def client_add(clients):
    """
    Cadastra clientes

    :param clients: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print(f"Cliente já cadastrado. Os dados atuais do cliente "
              f"com CPF '{id}' são: {clients[id]}")
        op = util.get_yes_no_value("Deseja alterar seus dados")
        if op == 'S':
            add_edit_client(id, clients)
            return True, "Cliente alterado com sucesso"
        else:
            return False, "Cadastro não realizado. Cliente já existente"
    else:
        add_edit_client(id, clients)
        return True, "Cliente cadastrado com sucesso"


def client_edit(clients):
    """
    Edita clientes

    :param clients: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print(f"Os dados atuais do cliente com CPF '{id}' são: {clients[id]}")
        add_edit_client(id, clients)
        return True, "Cliente alterado com sucesso"
    else:
        op = util.get_yes_no_value("Cliente não localizado. "
                                   "Deseja fazer seu cadastro")
        if op == 'S':
            add_edit_client(id, clients)
            return True, "Cliente cadastrado com sucesso"
        else:
            return False, "Cliente não localizado."


def client_del(clients):
    """
    Exclui clientes

    :param clients: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print(f"Os dados atuais do cliente com CPF '{id}' são: {clients[id]}")
        op = util.get_yes_no_value("Tem certeza que deseja excluir "
                                   "este cliente")
        if op == 'S':
            del clients[id]
            return True, "Cliente excluído com sucesso"
        else:
            return False, "Operação cancelada pelo usuário"
    else:
        return False, "Nenhum cliente cadastrado com esse CPF"


def client_query(clients):
    """
    Pesquisa clientes

    :param clients: Database em formato de dicionário
    :return: None
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print("Nome do cliente:", clients[id][CONST_FIELD_NAME])
        print("Cidade do cliente:", clients[id][CONST_FIELD_CITY])
        print("Idade do cliente:", clients[id][CONST_FIELD_AGE])
    else:
        op = util.get_yes_no_value("Cliente não encontrado, "
                                   "Deseja cadastrá-lo")
        if op == 'S':
            add_edit_client(id, clients)
        else:
            print("Cliente não localizado")


def database_clear(clients):
    """
    Apaga o banco de dados de clientes

    :param clients: Database em formato de dicionário
    :return: Mensagem de resultado da operação
    """
    print(f"O banco de dados possui {len(clients)} clientes cadastrados")
    op = util.get_yes_no_value("Tem certeza que deseja zerar o banco de dados")
    if op == 'S':
        clients.clear()
        return True, "Dados zerados com sucesso"
    else:
        return False, "Operação cancelada pelo usuário"


def add_edit_client(id, clients):
    """
    Função auxiliar do cadastro / alteração dados

    :param id: CPF do cliente
    :param clients: Database em formato de dicionário
    :return: None
    """
    name = input("Digite o nome do cliente: ")
    city = input("Digite a cidade do cliente: ")
    age = util.get_int_value_with_range("Digite a idade do cliente", 18, 120)
    clients[id] = {
        CONST_FIELD_NAME: name,
        CONST_FIELD_CITY: city,  # Atualiza / Cria o cadastro do cliente
        CONST_FIELD_AGE: age
    }


if __name__ == '__main__':  # Abre a função principal
    main()
