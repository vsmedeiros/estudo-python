identificador = input("Digite o identificador: ")

valido = True

if len(identificador) != 7:
    valido = False
elif not identificador.startswith("BR"):
    valido = False
elif not identificador.endswith("X"):
    valido = False
else:
    parte_numerica = identificador[2:6]

    if not parte_numerica.isdigit():
        valido = False
    else:
        numero = int(parte_numerica)
        if numero < 1 or numero > 9999:
            valido = False

if valido:
    print("Identificador válido")
else:
    print("Identificador inválido")
