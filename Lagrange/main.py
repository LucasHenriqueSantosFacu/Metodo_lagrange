def formula_de_lagrange(x, y):
    resultado = []

    for i in range(len(x)):
        term_num = [str(y[i])]
        term_denom = ["1.0"]

        for j in range(len(x)):
            if j != i:
                term_num.append(f" * (x - {x[j]})")
                term_denom.append(f" * ({x[i]} - {x[j]})")

        resultado.append(" * ".join(term_num) + " / " + " * ".join(term_denom))

    return " + ".join(resultado)


def main():
    # Infos para o user
    n = int(input("Digite o número de pontos conhecidos (por exemplo: se tiver 3 combinações de x e y, digite 3): "))
    x = []
    y = []

    print("Digite os pontos conhecidos (x, f(x), ou seja, y):")
    for i in range(n):
        ponto = input(f"Ponto {i + 1}: ").split()
        x.append(float(ponto[0]))
        y.append(float(ponto[1]))

    # Calcular o polinômio interpolador
    polinomio_interpolador = formula_de_lagrange(x, y)

    # Finalizar mostrando resultado
    print("\nGrau do Polinômio:", n - 1)
    print("Polinômio Interpolador:", polinomio_interpolador)


if __name__ == "__main__":
    main()