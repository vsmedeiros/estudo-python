def carregar_dados_projetos(nome_arquivo):
    """
    Retorna uma tupla de dicionários com dados de projetos.
    """
    projetos = []

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(',')

                projeto = {
                    'codigo': int(partes[0]),
                    'titulo': partes[1],
                    'responsavel': partes[2]
                }

                projetos.append(projeto)

    return tuple(projetos)


projetos = carregar_dados_projetos('src/06-arquivos/exercicios/projetos.txt')
for projeto in projetos:
    print(projeto)
