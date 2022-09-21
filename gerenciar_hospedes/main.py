hospedes = []
#Dados = {"nome": '', "cpf": '', "telefone": ''}
poli = "="*50

while True:
    opcao = input()
    if opcao:
        pass
    
#4 -> Fazer Check-Out -- Vander
#Procurar o hospede pelo nome e remover ele da lista, e apresentar a tabela atualizada mostrando o ID nome CPF e 
#telefone indicando que essa pessoa foi removida e mostrando somente os hospedes cadastrados.

    elif opcao == "4":
        if len(hospedes) == 0:
            print(f"{poli}\n******************* NÃO HÁ HÓSPEDES ******************\n{poli}")
        else:
            for i, v in enumerate():
                print(f"{i} - {v['nome']}")
            while True:
                indice = input("Digite o indice do hóspede que deseja fazer o CHECKOUT: ")
                if not(indice.isnumeric()):
                    print("Letras não sao validas como opção!")
                elif int(indice) >= len(hospedes):
                    print("Indice nao existe!")
                else:
                    print("Checkout realizado com sucesso")
                    break
            hospedes.pop(int(indice))