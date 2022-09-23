CPFS = ["00000000000","11111111111", "22222222222", "33333333333", "44444444444", 
        "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"]
while True:
    opcao = 1
    if opcao == 1:
        hasError = False
        cpf = input("Digite o CPF ai pae: ")
        # Limpa o cpf, retira pontos traços e tudo que não seja um número
        cpf = [int(char) for char in cpf if char.isdigit()]        

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
            print("Deu merda")
        else: 
            print("Deu bom")