lista_vazio = []    # Lista que conterá os livros.
id_global = 0


def orgList():
    global lista_vazio

    for livro in lista_vazio:
        id = livro['id']
        nome = livro['nome']
        autor = livro['autor']
        editora = livro['editora']
        print(f'Id: {id}\n Nome: {nome}\n Autor: {autor}\n Editora: {editora}\n', '-'* 20)

def valida_int(pergunta, min, max): #Função que valida a pergunta recebendo os números, caso não receba o valor esperado, mostra "Opção inválida" e os valores que podem ser digitados para obter alguma resposta.
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print(f'Opção inválida ({min} - {max})') #Antes de usar o (f''{min and max}) estava colocando uma numeração fixa(1- 4), fazendo assim torna mais agradavel para o usuário, pois nem sempre teremos esse valor como absoluto (de 1 a 4).
        x = int(input(pergunta))
    return x

def escolha():
    global id_global     # Variável declarada como global para poder ser usada nessa função(def). Assume o ID do livro
    print('*' * 78)
    print('-' * 30, ' MENU PRINCIPAL ', '-' * 30)
    print('Escolha a opção desejada: ')
    print('1- Cadastrar Livro')
    print('2- Consultar Livro(s)')
    print('3- Remover Livro')
    print('4- Encerrar programa')
    option = valida_int('>> ', 1, 4)
    print('*' * 60)


    if option == 1:
        print('-' * 15, ' MENU CADASTRAR LIVRO ', '-' * 15)
        id_global += 1 # Como a variável começa com 0(zero), toda vez que iremos adicionar um livro, essa variável recebe acréscimo de 1 ( soma-se um na variável)
        id = id_global
        print('Id do Livro: ', id)
        cadastrar_livro(id)
    elif option == 2:
        print('-' * 15, ' MENU CONSULTAR LIVRO ', '-' * 15)
        consultar_livro()
    elif option == 3:
        remover_livro()
    elif option == 4:
        print('Saindo do programa...')


def cadastrar_livro(id):
    global lista_vazio, id_global
    id = id_global

    nome = input('Por favor entre com o nome: ').casefold()
    autor = input('Por favor entre com o Autor(a): ').casefold()
    editora = input('Por favor entre com a editora: ').casefold()
    dadosLivro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora} #Por se tratar de um dicionário(object) temos que colocar os dados em volta de "{}" e referenciar as propriedades por 'propriedade'.
    lista_vazio.append(dadosLivro)

    escolha()

def consultar_livro():
    global lista_vazio
    print('Deseja escolher qual opção? ')
    print('1- Consultar Todos')
    print('2- Consultar por Id')
    print('3- Consultar por Autor(a)')
    print('4- Retornar ao Menu')
    consulta = valida_int('>>', 1, 4) # Consulta só irá receber números de 1 a 4.

    if consulta == 1:
        orgList()
        consultar_livro()

    elif consulta == 2:
        idEscolha = valida_int('Informe o ID do livro: ', 1, 9999)

        if (idEscolha - 1) > len(lista_vazio):
            print('Id inválido, não tem essa quantidade de livros!')
            consultar_livro()
        else:
            print(f'Id: {lista_vazio[idEscolha - 1]["id"]}\n Nome: {lista_vazio[idEscolha - 1]["nome"]}\n Autor(a): {lista_vazio[idEscolha - 1]["autor"]}\n Editora: {lista_vazio[idEscolha - 1]["editora"]}\n ', '-'*20)
            consultar_livro()

    elif consulta == 3:
        autorEscolha = input('Digite o nome do Autor(a) do livro: ').casefold()


        for livro in lista_vazio: # O "for" foi usado para passar por todos os livros da lista_vazio( lista que contém os livros).
            if (livro["autor"] == autorEscolha): #Compara o autor( autorEscolha) com cada propriedade do livro chamada autor, se for igual ela é adicionada na variável "livrosEncontrados".
                print(f'Id: {livro["id"]}\n Nome: {livro["nome"]}\n Autor: {livro["autor"]}\n Editora: {livro["editora"]}\n', '-'*20) #Irá mostrar livro por livro, até mostrar todos os livros do mesmo autor(a)

        consultar_livro()
    elif consulta == 4:
        escolha()


def remover_livro():
    optionRemove = valida_int('Digite o id do livro que deseja REMOVER: ', 1, 9999)
    positionRemove = (optionRemove - 1)
    lista_vazio.pop(positionRemove)
    print('Livro removido! ')
    escolha()



print(' Bem-vindo ao Controle de livros do Wendel dos Santos Ferreira RU: 4648393')
escolha()