from ex03 import Participacao
from ex01 import Aluno

class Projeto:
    def __init__(self, codigo: int, titulo: str, responsavel: str):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

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

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f"Projeto(codigo={self.codigo}, titulo='{self.titulo}', responsavel='{self.responsavel}')"
    
    def add_participacao(self, participacao):
        if not isinstance(participacao, Participacao):
            raise ValueError("A participação deve ser uma instância de Participacao")
        self.participacoes.append(participacao)

    def print_participacoes(self):
        for participacao in self.participacoes:
            print(participacao)


if __name__ == "__main__":
    projeto1 = Projeto.from_string(
        "1,Laboratório de Desenvolvimento de Software,Pedro Gomes"
    )
    projeto2 = Projeto(1, "Outro título", "Outro professor")
    aluno1 = Aluno("SP0101", "João da Silva", "joao@email.com")

    projeto1.add_participacao(Participacao(101, "2024-01-15", "2024-06-15", aluno1, projeto1))
    projeto1.add_participacao(Participacao(102, "2024-02-01", "2024-07-01", aluno1, projeto1))

    print(projeto1)
    projeto1.print_participacoes()
