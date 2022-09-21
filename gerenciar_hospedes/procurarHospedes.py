hospedes = [{"nome": 'daniel', "cpf": '23232', "telefone": '123123'},
            {"nome": 'seila', "cpf": '234242', "telefone": '6661623'}]

hospedeEncontrado = False
nomeHospedeDigitado = input("Digite o nome do hóspede: ")
for hospede in hospedes:
    if hospede["nome"] == nomeHospedeDigitado:
        hospedeEncontrado = True
        print("Nome: " + hospede["nome"] + " CPF: " + hospede["cpf"] + " Telefone: " + hospede["telefone"])
        break

if hospedeEncontrado == False:
    print("Não há hóspede registrado com esse nome.")

    