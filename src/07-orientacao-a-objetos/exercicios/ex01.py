class Aluno:
    def __init__(self, prontuario: str, nome: str, email: str):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, dados: str):
        partes = dados.split(",")
        if len(partes) != 3:
            raise ValueError("Formato inválido. Use: prontuario,nome,email")
        return cls(*partes)

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if not valor:
            raise ValueError("Prontuário não pode ser vazio ou nulo")
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio ou nulo")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor:
            raise ValueError("Email não pode ser vazio ou nulo")
        self._email = valor

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)
    
    def __str__(self):
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}', email='{self.email}')"


if __name__ == "__main__":
    aluno1 = Aluno.from_string("SP0101,João da Silva,joao@email.com")
    aluno2 = Aluno("SP0101", "João Silva", "joao2@email.com")

    print(aluno1 == aluno2)
