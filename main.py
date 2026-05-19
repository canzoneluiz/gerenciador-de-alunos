sair = False
alunos = []


while sair == False:

    print('''
Cadastrar aluno: 1
Listar alunos: 2
Buscar aluno: 3
Remover aluno: 4
media da turma: 5
Sair: 6''')
    try:
        menu_escolha = int(input('O que deseja fazer? '))

        if menu_escolha not in [1, 2, 3, 4, 5, 6]:
            print('escolha inválida!')

        elif menu_escolha == 1:
            while True:
                nome = input('Digite o nome do aluno: ').strip()
                if nome != "":
                    break
                print('Nome vazio!Tente novamente!')
            while True:
                idade = int(input('Digite a idade: '))
                if 0 < idade <= 100:
                    break
                print('idade invalida!Tente novamente!')
            while True:
                nota = float(input('Digite a nota final: '))
                if 0 <= nota <= 10:
                    break
                print('nota invalida!Tente novamente!')
            alunos.append([nome, idade, nota])

        elif menu_escolha == 2:
            for indice, aluno in enumerate(alunos, start=1):
                print(f"{indice}_ Nome: {aluno[0]} | Idade: {aluno[1]} | Nota: {aluno[2]}")

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
            soma = 0
            if len(alunos) == 0:
                print('lista de alunos vazia, adicione alunos para que a media seja calculada')
            else:
                media = sum(aluno[2] for aluno in alunos) / len(alunos)
                print(media)

        elif menu_escolha == 6:
            print('Saindo do sistema')
            sair = True

    except ValueError:
        print('escolha invalida!')
