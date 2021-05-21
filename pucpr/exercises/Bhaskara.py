# Programa que faz o cálculo da fórmula de Bhaskara

def delta(a, b, c):  # Calcula o valor do delta
    r = b ** 2 - 4 * a * c
    return r


def raiz_delta(raiz):  # Calcula o valor da raiz do delta
    r = raiz ** (1 / 2)
    return r


def cal_x(a, b, raiz):  # Calcula o valor do x1 e do x2 do delta
    x1 = (-b + raiz) / 2 * a
    x2 = (-b - raiz) / 2 * a
    return x1, x2


def main():  # Pede os valores de A, B, C e exibe o resultado
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    result = cal_x(a, b, raiz_delta(delta(a, b, c)))
    print(f"As raízes da parábula com valores A: {a}, B: {b} e C: {c} são: {result}")


if __name__ == "__main__":
    main()
