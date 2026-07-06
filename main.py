# ==========================
# IMPORTAÇÕES
# ==========================
import json

# ==========================
# BANCO DE DADOS (JSON)
# ==========================
def carregar_alunos():
    try:
        with open('alunos.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_alunos():
    with open('alunos.json', 'w', encoding='utf-8') as json_file:
        json.dump(alunos, json_file, indent=4)

alunos = carregar_alunos()
# ==========================
# MENU
# ==========================
def mostrar_menu():
    print('''
Cadastrar aluno: 1
Listar alunos: 2
editar aluno:3
Buscar aluno: 4
Remover aluno: 5
media do aluno:6
media da turma: 7
Sair: 8''')

def menu_escolha():
    while True:
        try:
            escolher = int(input('O que deseja fazer? '))

            if escolher in [1, 2, 3, 4, 5, 6, 7, 8]:
                return escolher

            print('Escolha inválida!')

        except ValueError:
            print('Digite apenas os números das opções!')

# ==========================
# CADASTRO
# ==========================
def cadastrar_aluno():
    nome = cadastrar_nome()
    idade = cadastrar_idade()
    notas = cadastrar_notas()

    alunos.append({
        "nome": nome,
        "idade": idade,
        "notas": notas
    })
    salvar_alunos()

def cadastrar_nome():
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
    return nome

def cadastrar_idade():
    while True:
        try:
            idade = int(input('Digite a idade: '))

            if 0 <= idade <= 100:
                break

            print('Idade inválida! Tente novamente!')

        except ValueError:
            print('Digite um valor numérico!')
    return idade

def cadastrar_notas():
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
    return notas
# ==========================
# CONSULTAS
# ==========================
def encontrar_aluno(nome):
    nome = nome.strip().lower()

    for aluno in alunos:
        if aluno['nome'].lower() == nome:
            return aluno
    return None

def busca_aluno():
    nome = input('Digite o nome do aluno: ')
    aluno = encontrar_aluno(nome)
    if aluno:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: {aluno['notas']}")

    else:
        print('aluno invalido!')

def lista_alunos():
    for indice, aluno in enumerate(alunos, start=1):
        print(f"{indice}_ Nome: {aluno['nome']} | Idade: {aluno['idade']} | Notas: {aluno['notas']}")

# ==========================
# EDIÇÃO
# ==========================
def editar_aluno():
    a = 1

# ==========================
# REMOÇÃO
# ==========================
def remover_aluno():
    nome = input('Digite o nome do aluno: ')
    aluno = encontrar_aluno(nome)

    if aluno:
        alunos.remove(aluno)
        salvar_alunos()
        print('Aluno removido!')
    else:
        print('Aluno inválido!')

# ==========================
# MÉDIAS
# ==========================
def calcular_media_aluno(aluno):
    if len(aluno['notas']) == 0:
        return None

    return sum(aluno['notas']) / len(aluno['notas'])


def media_aluno():
    nome = input('Digite o nome do aluno: ')
    aluno = encontrar_aluno(nome)

    if aluno:
        media = calcular_media_aluno(aluno)

        if media is None:
            print(f"O aluno {aluno['nome']} não possui notas cadastradas.")
        else:
            print(f"Média do aluno {aluno['nome']} é: {media:.2f}")

    else:
        print('aluno invalido!')


def media_turma():
    if len(alunos) == 0:
        print('lista de alunos vazia, adicione alunos para que a media seja calculada')
    else:
        calculo_media_turma = sum(calcular_media_aluno(aluno) for aluno in alunos) / len(alunos)
        print(f"Média da turma: {calculo_media_turma:.2f}")

# ==========================
# PROGRAMA PRINCIPAL
# ==========================
def main():
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
            media_aluno()

        elif escolha == 7:
            media_turma()

        elif escolha == 8:
            print('saindo do sistema')
            break

if __name__ == "__main__":
    main()
