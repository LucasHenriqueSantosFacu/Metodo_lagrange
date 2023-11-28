def interpolacao_lagrange(x_valores, y_valores):
    # Define um polinômio base para um índice i dado
    def termo_base(i):
        def termo(x):
            resultado = 1
            for j in range(len(x_valores)):
                if j != i:
                    resultado *= (x - x_valores[j]) / (x_valores[i] - x_valores[j])
            return resultado

        return termo

    # Define o polinômio interpolador de Lagrange
    polinomio_interpolador = lambda x: sum(y_valores[i] * termo_base(i)(x) for i in range(len(x_valores)))

    # Constrói a expressão simplificada do polinômio interpolador de Lagrange
    expressao_simplificada = ""
    for i in range(len(x_valores)):
        termo_str = f"{y_valores[i]} * "
        for j in range(len(x_valores)):
            if j != i:
                termo_str += f"(x - {x_valores[j]}) / ({x_valores[i]} - {x_valores[j]}) * "
        expressao_simplificada += termo_str[:-2] + " + "

    expressao_simplificada = expressao_simplificada[:-2]  # Remove o último "+"

    return expressao_simplificada

# Valores de exemplo para a interpolação
valores_x_exemplo = [-2, 0, 2, 3]
valores_y_exemplo = [5, -2, 3, 6]

# Obtém a expressão simplificada do polinômio interpolador de Lagrange
expressao_simplificada = interpolacao_lagrange(valores_x_exemplo, valores_y_exemplo)

# Imprime a expressão simplificada do polinômio interpolador de Lagrange em x
print("Expressão Simplificada do Polinômio Interpolador de Lagrange em x:")
print(expressao_simplificada)
