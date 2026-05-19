sair = False
alunos = [
    ["Carlos", 17, 8.5],
    ["Maria", 18, 9.0],
    ["João", 16, 7.2]
]


while sair == False:

    print('''
Cadastrar aluno: 1
Listar alunos: 2
Buscar aluno: 3
Remover aluno: 4
Sair: 5''')
    try:
        menu_escolha = int(input('O que deseja fazer? '))

        if menu_escolha not in [1, 2, 3, 4, 5]:
            print('escolha inválida!')

        elif menu_escolha == 1:
            nome = input('Digite o nome do aluno: ')
            idade = int(input('Digite a idade: '))
            nota = float(input('Digite a nota final: '))
            alunos.append([nome, idade, nota])

        elif menu_escolha == 2:
            for aluno in alunos:
                print(f'Nome: {aluno[0]}')
                print(f'Idade: {aluno[1]}')
                print(f'Nota final: {aluno[2]}\n')

        elif menu_escolha == 3:
            nome_procurado = input('Digite o nome: ')

            for aluno in alunos:
                if aluno[0].lower() == nome_procurado.lower():
                    print(f'Nome: {aluno[0]}')
                    print(f'Idade: {aluno[1]}')
                    print(f'Nota final: {aluno[2]}')
                    break
            else:
                print('aluno invalido!')

        elif menu_escolha == 4:
            nome_remover = input('Digite o nome do aluno: ')

            for aluno in alunos:
                if aluno[0].lower() == nome_remover.lower():
                    alunos.remove(aluno)
                    print('Aluno removido!')
                    break
            else:
                print('aluno invalido!')

        elif menu_escolha == 5:
            print('Saindo do sistema')
            sair = True

    except ValueError:
        print('escolha invalida!')
