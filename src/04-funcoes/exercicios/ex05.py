def calcular_imc(individuo):
    """Retorna o IMC de um indivíduo com base na sua altura e peso."""
    return individuo["peso"] / (individuo["altura"] ** 2)


def obter_classificacao(imc):
    """Retorna a classificação com base no IMC."""
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    elif imc < 35:
        return "Obesidade Classe 1"
    elif imc < 40:
        return "Obesidade Classe 2"
    else:
        return "Obesidade Classe 3"


def situacao_individuo(imc):
    """Retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no
IMC."""

    if imc < 18.5:
        return "ganhar peso"
    elif imc <= 24.9:
        return "normal"
    else:
        return "perder peso"


peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

individuo = {
    "peso": peso,
    "altura": altura
}

imc = calcular_imc(individuo)

print(f"IMC: {imc:.2f}")
print(f"Classificação: {obter_classificacao(imc)}")
print(f"Situação: {situacao_individuo(imc)}")
