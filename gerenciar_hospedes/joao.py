CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]
hospedes = []
poli = "="*50
espaco = " "*21
print(f"{poli}\n{espaco}MENU DO MOTEL\n{poli}")
print(f"{espaco}MENU{espaco}".center(50,"="))

while True:
    print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
    print(poli)
    opcao = input("=> ")
    if opcao == '1':
        varnome = input('Digite o seu nome: ').title()
        while True:
            vartelefone = input('Digite o seu telefone(ddxxxxxxxxx): ')
            if not(vartelefone.isnumeric()):
                print('Isso não é numero!')
            else:
                break
        while True:
            varcpf = input('Digite seu CPF (xxx.xxx.xxx-xx): ')

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
                print(f'{poli}Hospede cadastrado com sucesso!!{poli}')
                dados = {
                    'nome': varnome, 
                    'cpf': varcpf,
                    'telefone': vartelefone
                }
                hospedes.append(dados)
                break