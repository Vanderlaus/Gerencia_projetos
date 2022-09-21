'''Cria um menu de forma infinita que apareça as opções:
1 -> Fazer Check-In -- Dieter
O programa deve perguntar as informações cadastrais, Nome/CPF/Telefone
e perguntar se deseja cadastrar outra pessoa, caso não, voltar ao menu.'''

hospedes = []
dados = {"nome": '', "cpf": '', "telefone": ''}

while True:
    varnome = input('Qual o seu nome?')

    while True: 
        varcpf = input('Qual o seu CPF?')
        if not(cpf.isnumeric()):
            print('Isso não é numero.')
        else:
            break
    while True:
        vartelefone = input('Qual o seu telefone?')
        if not(telefone.isnumeric()):
            print('Isso não é numero.')
        else:
            break
    print('Fim de cadastro')
    dados = {
    'titulo': varnome, 
    'editora': varcpf,
    'autor': vartelefone
    }
    dados.append(hospedes)
    print(hospedes)
    break