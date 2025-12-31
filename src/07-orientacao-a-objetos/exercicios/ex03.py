from ex01 import Aluno
from ex02 import Projeto


class Participacao:
    def __init__(
        self,
        codigo: int,
        data_inicio: str,
        data_fim: str,
        aluno,
        projeto
    ):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None:
            raise ValueError("Código não pode ser nulo")
        self._codigo = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if not valor:
            raise ValueError("Data de início não pode ser vazia ou nula")
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if not valor:
            raise ValueError("Data de fim não pode ser vazia ou nula")
        self._data_fim = valor

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        if valor is None:
            raise ValueError("Aluno não pode ser nulo")
        self._aluno = valor

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, valor):
        if valor is None:
            raise ValueError("Projeto não pode ser nulo")
        self._projeto = valor

    def __str__(self):
        return f"Participação(código={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno.nome}, projeto={self.projeto.titulo})"


if __name__ == "__main__":
    aluno = Aluno("SP0101", "João da Silva", "joao@email.com")
    projeto = Projeto(1, "LDS", "Pedro Gomes")

    participacao = Participacao(
        100,
        "2025-03-01",
        "2025-12-01",
        aluno,
        projeto
    )

    print(participacao)
