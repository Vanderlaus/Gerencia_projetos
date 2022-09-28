CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]
hospedes = []
funcoes = ['1','2','3','4','5']
poli = "="*50
espaco = " "*10
espaco1 = " "*12

print(f"{poli}\n{espaco1}MOTEL QUATRO ABACATINHOS :)\n{poli}")
print(f"{espaco}Cadastro de Hospedes{espaco}".center(50,"="))

while True:
    print(poli)
    print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
    print(poli)
    opcao = input("=> ")
    if not(opcao in funcoes):
        print("Digite uma opção válida.\n Uma das opções do Cadastro.")
    elif opcao == '1':
        varnome = input('Nome Completo: ').title()
        while True:
            vartelefone = input('Telefone com DDD: ')
            if not(vartelefone.isnumeric()):

                print('Somente números!')
            else:
                break
        while True:
            varcpf = input('CPF: ')

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
                print(f"{poli}CPF inválido!!{poli}")
            else: 
                print(f"{espaco}Hospede cadastrado com sucesso{espaco}".center(50,"="))
                dados = {
                    'nome': varnome, 
                    'cpf': varcpf,
                    'telefone': vartelefone
                }
                hospedes.append(dados) 
                break

    elif opcao == '2':
        if len(hospedes) == 0:
            print(f"{espaco}NÃO HÁ HÓSPEDES{espaco}".center(50,"="))
        else:
            for hospede in hospedes:
                print("Nome: " + hospede["nome"] + " CPF: " + hospede["cpf"] + f" Telefone: ({hospede['telefone'][0:2]}) {hospede['telefone'][2:]}") #transformar em função


    elif opcao == '3':
        if len(hospedes) == 0:
            print(f"{espaco}NÃO HÁ HÓSPEDES{espaco}".center(50,"="))
        else:
            hospedeEncontrado = False
            print(">>> BUSCAR HOSPEDE <<<")
            nomeHospedeDigitado = input("Digite o nome: ").title()
            for hospede in hospedes:
                if hospede["nome"] == nomeHospedeDigitado:
                    hospedeEncontrado = True
                    print("Nome: " + hospede["nome"] + " CPF: " + hospede["cpf"] + f" Telefone: ({hospede['telefone'][0:2]}) {hospede['telefone'][2:]}")
                    break

            if hospedeEncontrado == False:
                print("Não existe hospede registrado com esse nome")


    elif opcao == "4":
        if len(hospedes) == 0:
            print(f"{espaco}NÃO HÁ HÓSPEDES{espaco}".center(50,"="))
        else:
            for i, v in enumerate(hospedes):
                print(f"{i} - {v['nome']}")
            while True:
                indice = input("Qual hóspede deseja fazer o CHECKOUT: ")
                if not(indice.isnumeric()):
                    print("Letras não sao validas como opção!")
                elif int(indice) >= len(hospedes):
                    print("Hospede não existe!")
                else:
                    print(" Checkout realizado com sucesso ".center(50, '='))
                    hospedes.pop(int(indice))
                    break

    elif opcao == '5':
        print(' Beijo, tchau, tchau :D '.center(50, "*"))
        break