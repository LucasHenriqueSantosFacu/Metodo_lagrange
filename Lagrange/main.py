def formula_de_lagrange(x_valores, y_valores):
    # Lista para armazenar os termos do polinômio interpolador
    resultado = []

    # Itera sobre cada ponto conhecido
    for i in range(len(x_valores)):
        # Numerador do termo de Lagrange
        termo_numerador = [str(y_valores[i])]
        # Denominador do termo de Lagrange
        termo_denominador = ["1.0"]

        # Itera sobre todos os pontos conhecidos novamente para construir os termos
        for j in range(len(x_valores)):
            if j != i:
                # Adiciona parte do termo numerador
                termo_numerador.append(f" * (x - {x_valores[j]})")
                # Adiciona parte do termo denominador
                termo_denominador.append(f" * ({x_valores[i]} - {x_valores[j]})")

        # Combina as partes para formar o termo completo de Lagrange
        resultado.append(" * ".join(termo_numerador) + " / " + " * ".join(termo_denominador))

    # Combina todos os termos para formar o polinômio interpolador final
    return " + ".join(resultado)


def main():
    # Informações para o usuário
    numero_de_pontos = int(input("Digite o número de pontos conhecidos (por exemplo: se tiver 3 combinações de x e y, digite 3): "))
    x_valores = []
    y_valores = []

    print("Digite os pontos conhecidos (x, f(x), ou seja, y):")
    for i in range(numero_de_pontos):
        ponto = input(f"Ponto {i + 1}: ").split()
        x_valores.append(float(ponto[0]))
        y_valores.append(float(ponto[1]))

    # Calcular o polinômio interpolador usando a fórmula de Lagrange
    polinomio_interpolador = formula_de_lagrange(x_valores, y_valores)

    # Exibe o resultado final
    print("\nGrau do Polinômio:", numero_de_pontos - 1)
    print("Polinômio Interpolador:", polinomio_interpolador)


if __name__ == "__main__":
    main()
