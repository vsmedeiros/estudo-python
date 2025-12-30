def linha_para_dict(linha, chaves):
    """
    Recebe uma linha e uma lista de chaves e retorna um dicionário.
    """

    linha = linha.strip()
    valores = linha.split(',')

    dados = {}
    for i, chave in enumerate(chaves):
        dados[chave] = valores[i]

    return dados


def carregar_dados_projetos(nome_arquivo):
    """
    Retorna uma tupla de dicionários com dados de projetos.
    """
    projetos = []
    chaves = ['codigo', 'titulo', 'responsavel']

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.strip():
                projeto = linha_para_dict(linha, chaves)
                projeto['codigo'] = int(projeto['codigo'])
                projetos.append(projeto)

    return tuple(projetos)

projetos = carregar_dados_projetos('src/06-arquivos/exercicios/projetos.txt')
for projeto in projetos:
    print(projeto)
