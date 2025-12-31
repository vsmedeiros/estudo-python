class Projeto:
    def __init__(self, codigo: int, titulo: str, responsavel: str):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, dados: str):
        partes = dados.split(",")
        if len(partes) != 3:
            raise ValueError(
                "Formato inválido. Use: codigo,titulo,responsavel")
        codigo, titulo, responsavel = partes
        return cls(int(codigo), titulo, responsavel)

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise ValueError("Código deve ser um número inteiro")
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Título não pode ser vazio ou nulo")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor:
            raise ValueError("Responsável não pode ser vazio ou nulo")
        self._responsavel = valor

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False


p1 = Projeto.from_string(
    "1,Laboratório de Desenvolvimento de Software,Pedro Gomes"
)
p2 = Projeto(1, "Outro título", "Outro professor")

print(p1 == p2)
