# Lista de Exercícios
# Exercício 40

# Listas vazias que conterão dados importantes
cod_cidades = []
n_veiculos = []
n_acidentes = []
acidentes_2000 = []

# Entrada dos dados
for i in range(5):
    print(f"{i + 1}° Cidade")
    codigo_cidade = int(input("Digite o código da cidade: "))
    while codigo_cidade in cod_cidades:
        print("[Código já digitado]")
        codigo_cidade = int(input("Digite outro código: "))

    numero_acidentes = int(input("Digite o número de acidentes: "))
    numero_veiculos = int(input("Digite o número de veiculos: "))

    if numero_veiculos > 2000:
        acidentes_2000.append(numero_acidentes)
        n_acidentes.append(numero_acidentes)
    else:
        n_acidentes.append(numero_acidentes)

    n_veiculos.append(numero_veiculos)
    cod_cidades.append(codigo_cidade)

indice_acidentes_menor = n_acidentes.index(min(n_acidentes))
indice_acidentes_maior = n_acidentes.index(max(n_acidentes))

# Imprime a quantidade de acidentes e o código  das cidades com mais e com menos acidentes
print(f"\nMenos acidentes\nQuantidade de acidentes: {min(n_acidentes)}\nCódigo da cidade: "
      f"{cod_cidades[indice_acidentes_menor]}")
print(f"\nMais acidentes\nQuantidade de acidentes: {max(n_acidentes)}\nCódigo da cidade: "
      f"{cod_cidades[indice_acidentes_maior]}")

# Imprime a média de acidentes das 5 cidades
media_veiculos = sum(n_veiculos) / len(n_veiculos)
print(f"\nMédia de veiculos nas 5 cidades: {media_veiculos:2}")

# Imprime a média de acidentes nas cidades com menos de 2000 veículos
media_acidentes_2000 = sum(acidentes_2000) / len(acidentes_2000)
print(f"\nMédia de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_2000:2}")
