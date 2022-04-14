opcoes = {
        1:'Adicionar um novo ativo',
        2:'Visualizar a lista de ativos investidos',
        3:'Informar a venda de um ativo',
        4:'Visualizar resumo do valor total e unitario investido nos ativo',
        5:'Aperte 0 para sair',
}


def printMenu():
    for key in opcoes.keys():
        print(key, '--', opcoes[key])


while True:
    printMenu()
    bot = int(input('Informe a opção desejada: '))
    if bot == 1:
        print('Adicione um novo ativo:')
    if bot == 2:
        print('Visualize a lista de ativos')
    if bot == 3:
        print('Informe a venda de um ativo')
    if bot == 4:
        print('visualize o resumo total e unitário de cada ativo investido')
    if bot == 0:
        print('Saindo da operação')
        exit()