hospedes = [{"nome": 'Daniel', "cpf": '23232', "telefone": '123123'},
            {"nome": 'Thiago', "cpf": '234242', "telefone": '6661623'}]

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



