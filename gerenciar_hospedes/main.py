'''Cria um menu de forma infinita que apareça as opções:
1 -> Fazer Check-In -- Dieter
O programa deve perguntar as informações cadastrais, Nome/CPF/Telefone
e perguntar se deseja cadastrar outra pessoa, caso não, voltar ao menu.'''

hospedes = []
dados = {"nome": '', "cpf": '', "telefone": ''}
continuar = '1'
while True:

    if continuar == '1':
        varnome = input('Qual o seu nome? ')
        while True: 
            varcpf = input('Qual o seu CPF? ')
            if not(varcpf.isnumeric()):
                print('Isso não é numero.')
            else:
                break
        while True:
            vartelefone = input('Qual o seu telefone? ')
            if not(vartelefone.isnumeric()):
                print('Isso não é numero.')
            else:
                break
        print('Fim de cadastro')
        dados = {
            'Nome ': varnome, 
            'CPF ': varcpf,
            'Telefone: ': vartelefone
        }
        hospedes.append(dados)
    continuar = input('Você quer cadastrar mais?\n1) SIM\n2) NÃO\n::>')
    if continuar == '1':
        print('Sim, quero cadastrar mais.')

    elif continuar == '2':
        print('Saindo do programa')
        #Próxima linha é validação de cadastro. Pode retirar do programa Main.
        print('Cadastrados',(hospedes))
        break