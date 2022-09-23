CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]
hospedes = []
funcoes = ['1','2','3','4','5']
poli = "="*50
espaco = " "*21
print(f"{poli}\n{espaco}MENU DO MOTEL\n{poli}")
print(f"{espaco}MENU{espaco}".center(50,"="))

while True:
    print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
    print(poli)

    opcao = input("=> ")
    if not(opcao in funcoes):
        print("Digite uma opção válida.\n Uma das opções do MENU.")

    elif opcao == '1':
        varnome = input('Digite o seu nome: ').title()
        while True:
            vartelefone = input('Digite o seu telefone: ')
            if not(vartelefone.isnumeric()):
                print('Isso não é numero!')
            else:
                break
        varcpf = input('Digite seu CPF: ')

        hasError = False
        # Limpa o cpf, retira pontos traços e tudo que não seja um número
        cpf = [int(char) for char in varcpf if char.isdigit()]        

        # Verifica se o cpf são números repetidos
        if ''.join(map(str, cpf)) in CPFS:
            hasError = True

        # verifica se o tamanho está correto
        if len(cpf) != 11:
            hasError = True

        if not(hasError):
            for i in range(9, 11):
                value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
                digit = ((value * 10) % 11) % 10
                if digit != cpf[i]:
                    hasError = True
            
        if hasError:
            print(f"{poli}Deu merda{poli}")
        else: 
            print(f'{poli}Fim de cadastro{poli}')
            dados = {
                'nome': varnome, 
                'cpf': varcpf,
                'telefone': vartelefone
            }
            hospedes.append(dados)

    elif opcao == '2':
        if len(hospedes) == 0:
            print(f"{poli}\n******************* NÃO HÁ HÓSPEDES ******************\n{poli}")
        else:
            for hospede in hospedes:
                print("Nome: " + hospede["nome"] + " CPF: " + hospede["cpf"] + " Telefone: " + hospede["telefone"])

    elif opcao == '3':
        if len(hospedes) == 0:
            print(f"{poli}\n******************* NÃO HÁ HÓSPEDES ******************\n{poli}")
        else:
            hospedeEncontrado = False
            print(">>> BUSCAR HOSPEDE <<<")
            nomeHospedeDigitado = input("Digite o nome: ").title()
            for hospede in hospedes:
                if hospede["nome"] == nomeHospedeDigitado:
                    hospedeEncontrado = True
                    print("Nome: " + hospede["nome"] + " CPF: " + hospede["cpf"] + " Telefone: " + hospede["telefone"])
                    break

            if hospedeEncontrado == False:
                print("Não existe hospede registrado com esse nome.")


    elif opcao == "4":
        if len(hospedes) == 0:
            print(f"{poli}\n******************* NÃO HÁ HÓSPEDES ******************\n{poli}")
        else:
            for i, v in enumerate(hospedes):
                print(f"{i} - {v['nome']}")
            while True:
                indice = input("Digite o indice do hóspede que deseja fazer o CHECKOUT: ")
                if not(indice.isnumeric()):
                    print("Letras não sao validas como opção!")
                elif int(indice) >= len(hospedes):
                    print("Indice nao existe!")
                else:
                    print("Checkout realizado com sucesso".center(50, '='))
                    hospedes.pop(int(indice))
                    break

    elif opcao == '5':
        print('Saindo do programa'.center(50, "*"))
        break