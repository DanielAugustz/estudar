class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Matrícula: {self.matricula}")
        print("Disciplinas:")
        if self.disciplinas:
            for disciplina in self.disciplinas:
                print(f" - {disciplina.nome}")
        else:
            print("Nenhuma disciplina matriculada")

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Salário: {self.salario}")

class Disciplina:
    def __init__(self, nome, codigo, professor):
        self.nome = nome
        self.codigo = codigo
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome}, Código: {self.codigo}")
        print(f"Professor: {self.professor.nome}")
        print("Alunos matriculados:")
        if self.alunos:
            for aluno in self.alunos:
                print(f" - {aluno.nome}")
        else:
            print("Nenhum aluno matriculado")

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.professores = []
        self.disciplinas = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_alunos(self):
        print("Alunos matriculados:")
        if self.alunos:
            for aluno in self.alunos:
                aluno.exibir_informacoes()
        else:
            print("Nenhum aluno matriculado")

    def exibir_professores(self):
        print("Professores cadastrados:")
        if self.professores:
            for professor in self.professores:
                professor.exibir_informacoes()
        else:
            print("Nenhum professor cadastrado")

    def exibir_disciplinas(self):
        print("Disciplinas oferecidas:")
        if self.disciplinas:
            for disciplina in self.disciplinas:
                disciplina.exibir_informacoes()
        else:
            print("Nenhuma disciplina cadastrada")
