alunos = []

def mostrar_menu():
    print('''
Cadastrar aluno: 1
Listar alunos: 2
editar aluno:3
Buscar aluno: 4
Remover aluno: 5
media da turma: 6
Sair: 7''')

def menu_escolha():
    while True:
        try:
            escolher = int(input('O que deseja fazer? '))

            if escolher in [1, 2, 3, 4, 5, 6]:
                return escolher

            print('Escolha inválida!')

        except ValueError:
            print('Digite apenas os números das opções!')

def cadastrar_aluno():
    while True:
        nome = input('Digite o nome do aluno: ').strip()

        if nome == "":
            print('Nome vazio! Tente novamente!')
            continue

        nome_valido = True

        for caractere in nome:
            if not caractere.isalpha() and caractere not in " -'":
                print("Nome inválido! Use apenas letras, espaços, hífens e apóstrofos.")
                nome_valido = False
                break
        if nome_valido:
            break


    while True:
        try:
            idade = int(input('Digite a idade: '))

            if 0 <= idade <= 100:
                break

            print('Idade inválida! Tente novamente!')

        except ValueError:
            print('Digite um valor numérico!')

    while True:
        try:
            quantidade = int(input("Quantas notas deseja cadastrar? "))

            if quantidade > 0:
                break

            print("Digite um número maior que zero!")

        except ValueError:
            print("Digite um número inteiro!")

    notas = []

    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a {i + 1}ª nota: "))

                if 0 <= nota <= 10:
                    notas.append(nota)
                    break

                print("Nota inválida!")

            except ValueError:
                print("Digite um número!")


    alunos.append([nome, idade, notas])

def lista_alunos():
    for indice, aluno in enumerate(alunos, start=1):
        print(f"{indice}_ Nome: {aluno[0]} | Idade: {aluno[1]} | Nota: {aluno[2]}")

def editar_aluno():
    a=1

def encontrar_aluno():
    nome_procurado = input('Digite o nome: ')
    for aluno in alunos:
        if aluno[0].lower() == nome_procurado.lower():
            return aluno
    return None

def busca_aluno():
    aluno = encontrar_aluno()

    if aluno:
            print(f'Nome: {aluno[0]}')
            print(f'Idade: {aluno[1]}')
            print(f'Nota final: {aluno[2]}')

    else:
        print('aluno invalido!')

def remover_aluno():
    nome_remover = input('Digite o nome do aluno: ')

    for aluno in alunos:
        if aluno[0].lower() == nome_remover.lower():
            alunos.remove(aluno)
            print('Aluno removido!')
            break
    else:
        print('aluno invalido!')

def media_alunos():
    if len(alunos) == 0:
        print('lista de alunos vazia, adicione alunos para que a media seja calculada')
    else:
        media = sum(aluno[2] for aluno in alunos) / len(alunos)
        print(f"Média da turma: {media:.2f}")



while True:

    mostrar_menu()

    escolha = menu_escolha()

    if escolha == 1:
        cadastrar_aluno()

    elif escolha == 2:
        lista_alunos()

    elif escolha == 3:
        editar_aluno()

    elif escolha == 4:
        busca_aluno()

    elif escolha == 5:
        remover_aluno()

    elif escolha == 6:
        media_alunos()

    elif escolha == 7:
        print('saindo do sistema')
        break
