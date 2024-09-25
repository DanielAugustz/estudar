from classes import *

def criar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade do aluno: ")
    cpf = input("CPF do aluno: ")
    matricula = input("Matricula do aluno: ")
    aluno = Aluno(nome, idade, cpf, matricula)
    return aluno

def criar_professor():
    nome = input("Nome do professor: ")
    idade = input("Idade do professor: ")
    cpf = input("CPF do professor: ")
    salario = float(input("Salario do professor: "))
    professor = Professor(nome, idade, cpf, salario)
    return professor

def criar_disciplina(professores):
    nome = input("Nome da disciplina: ")
    codigo = input("Codigo da disciplina: ")
    for i, professor in enumerate(professores):
        print(f"{i + 1}. {professor.nome}")
    opcao = int(input("Escolha o professor pelo indice: ")) - 1
    if opcao < 0 or opcao >= len(professores):
        print("Professor inválido!")
        return None
    disciplina = Disciplina(nome, codigo, professores[opcao])
    return disciplina

escola = Escola("Escola")


while True:
    print("\n--- Sistema de Gerenciamento Escolar ---")
    print("1. Adicionar aluno")
    print("2. Adicionar professor")
    print("3. Adicionar disciplina")
    print("4. Exibir alunos")
    print("5. Exibir professores")
    print("6. Exibir disciplinas")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        aluno = criar_aluno()
        escola.adicionar_aluno(aluno)
    elif opcao == 2:
        professor = criar_professor()
        escola.adicionar_professor(professor)
    elif opcao == 3:
        if len(escola.professores) == 0:
            print("Não ha professores cadastrados")
        else:
            disciplina = criar_disciplina(escola.professores)
            if disciplina:
                escola.adicionar_disciplina(disciplina)
    elif opcao == 4:
        escola.exibir_alunos()
    elif opcao == 5:
        escola.exibir_professores()
    elif opcao == 6:
        escola.exibir_disciplinas()
    elif opcao == 0:
        print("Saindo do sistema")
        break
    else:
        print("Opção invalida!")
