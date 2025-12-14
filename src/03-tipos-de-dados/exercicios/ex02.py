meses = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)

numero = int(input("Digite o número do mês (1 a 12): "))

if 1 <= numero <= 12:
    print(meses[numero - 1])
else:
    print("Mês inválido")
