identificador = input("Digite o identificador: ")

erros = []

if len(identificador) != 7:
    erros.append("O identificador não contém 7 caracteres.")

if not identificador.startswith("BR"):
    erros.append("O identificador não inicia com a sequência BR.")

if not identificador.endswith("X"):
    erros.append("O identificador não finaliza com o caractere X.")

if len(identificador) >= 6:
    parte_numerica = identificador[2:6]
    if not parte_numerica.isdigit():
        erros.append(
            "O identificador não apresenta número inteiro entre 0001 e 9999.")
    else:
        numero = int(parte_numerica)
        if numero < 1 or numero > 9999:
            erros.append(
                "O identificador não apresenta número inteiro entre 0001 e 9999.")
else:
    erros.append(
        "O identificador não apresenta número inteiro entre 0001 e 9999.")

if not erros:
    print("Identificador válido")
else:
    print("Erros:")
    for erro in erros:
        print(f"- {erro}")
