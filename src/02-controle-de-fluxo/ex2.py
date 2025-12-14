entrada = input("Digite as notas separadas por vírgulas\nExemplo (7.5, 8.0, 6.0):\n")

notas = [float(nota.strip()) for nota in entrada.split(",")]

media = sum(notas) / len(notas)

if media > 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média aritmética: {media:.2f}")
print(f"Situação: {situacao}")
