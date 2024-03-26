"""
palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

"""

"""
import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor (jogador1, jogador2):
    global empate, v1, v2   # Traz as variáveis para serem usadas na função.
    if jogador1 == 1: # Pedra
        if jogador2 == 1: # Pedra
            empate += 1
        elif jogador2 == 2: # Papel
            v2 += 1
        elif jogador2 == 3: # Tesoura
            v1 += 1
    elif jogador1 == 2: # Papel
        if jogador2 == 1:  # Pedra
            v1 += 1
        elif jogador2 == 2:  # Papel
            empate += 1
        elif jogador2 == 3:  # Tesoura
            v2 += 1
    elif jogador1 == 3: # Tesoura
        if jogador2 == 1:  # Pedra
            v2 += 1
        elif jogador2 == 2:  # Papel
            v1 += 1
        elif jogador2 == 3:  # Tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

#Programa principal
print('JOKENPO')
print('1- Pedra')
print('2- Papel')
print('3- Tesoura')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)
    #print(vencedor(j1, j2))

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Número de vitórias do Jogador 1: ', resultados[0])
print('Número de vitórias do Jogador 2: ', resultados[1])
print('Número de empates: ', resultados[2])
"""

'''
cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input("Você deseja cadastrar uma pessoa? [S/N]: ")
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual o seu nome? ')
    sexo = input('Qual o seu sexo [M/F]? ')
    ano = int(input('Qual o seu ano de nascimento? '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)
'''

def orgList():
    global lista_vazio
    listaAtt = []

    for livro in lista_vazio:
        id = array['id']
        nome = array['nome']
        autor = array['autor']
        editora = array['editora']

        listaAtt.append(f'Id: {id}\n Nome: {nome}\n Autor: {autor}\n Editora: {editora}')

    return listaAtt



