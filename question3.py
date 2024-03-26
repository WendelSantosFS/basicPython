def escolha_servico(): #Esta função, quando chamada RETORNA um valor com base no serviço escolhido.
    while True:        #Como está em Loop Infinito, só irá sair da função caso algum serviço seja escolhido.
        print('\nEntre com o tipo de serviço desejado: ')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        x = input('>>').casefold() # Fiz o tratamento da variável para que receba letras maúsculas e minúsculas sem alterar o resultado.

        if x == 'dig':
            x = 1.1
            return x
        elif x == 'ico':
            x = 1
            return x
        elif x == 'ipb':
            x = 0.4
            return x
        elif x == 'fot':
            x = 0.2
            return x
        else:
            print('Opção inválida...')

def validation(): # Função que valida um números, só aceita entrada de números, se receber uma 'string' pede para o usuário digitar só números.
    try:
        number = int(input('\nDigite um número de páginas: '))
        return number
    except ValueError:
        number = int(input('Por favor, digite apenas números! '))
        return number

def num_pagina():  # retornar valor das páginas já com desconto.
    paginas = validation() #A função que valida números foi chamada.

    if paginas > 0 and paginas < 20:
        desconto = paginas * 1  # 1 = 100%, logo esta operação não terá desconto.
    elif paginas < 200:
        desconto = paginas * 0.85  # subitraí "0.15" de 1, logo esta operação irá gerar um desconto de 15% no valor total.
    elif paginas < 2000:
        desconto = paginas * 0.80  # Tal operação irá gerar um valor com 20% de desconto.
    elif paginas  < 10000:
        desconto = paginas * 0.75  # Esta operação irá gerar um desconto de 25% de desconto.
    elif paginas > 10000:
        print('Não aceitamos tantas páginas de um vez.')
        return num_pagina() # caso o valor ultrapassar o limite por cliente, aparece uma mensagem e chama a função de novo, LOOP INFINITO.

    return desconto

def valida02():
    try:
        number = int(input('>> '))
        return number
    except ValueError:
        number = int(input('>> '))
        return number

def servico_extra(): # Função para perguntar se o cliente deseja algum serviço extra. Caso escolha que SIM, será cobrado do mesmo.
    print('\nDeseja adicionar mais algum serviço?')
    print('1 - Encadernação Simples - R$10,00')
    print('2 - Encadernação Capa Dura - R$25,00')
    print('0 - Não desejo mais nada.')
    y = valida02()

    if y == 1:
        return 10
    elif y == 2:
        return 25
    elif y == 0:
        return 0
    else:
        return servico_extra() # Se for digitado valor diferente das opções existentes(0, 1, 2), a função chama ela mesma, também gerando um LOOP INFINITO.

print(' Bem-vindo ao Copiadora do Wendel dos Santos Ferreira RU: 4648393')
servico = escolha_servico() # SERVICO = Recebe o valor do serviço.

paginas = num_pagina()      # PAGINAS = Rebece o número de páginas.
extra = servico_extra()     # EXTRA = Caso o cliente deseje adicionar mais serviços ao que foi escolhido, será guardado na variável EXTRA.

total = float(servico * paginas) + extra
print(f'\nTotal (R$): {total:.2f} ', '(servico: ', servico , ' * paginas: ' , paginas , ' + extra(s): ', extra, ')')