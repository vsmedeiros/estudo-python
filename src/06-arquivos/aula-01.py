""" Aula 01 - Curso de Python para iniciantes  # 12 – Manipulando Arquivos """

# arquivo = open("src/06-arquivos/test3.txt", "x")

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)
# print(lista[3])
# arquivo.write("Python\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# arquivo.close()

import os
# if os.path.exists("src/06-arquivos/test2.txt"):
#     os.remove("src/06-arquivos/test2.txt")
# else:
#     print("O arquivo não existe")

os.rmdir("src/06-arquivos/nova_pasta")
