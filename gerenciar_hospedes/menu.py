""""1 -> Fazer Check-In
2 -> Relatório Hospedes
3 -> Procurar Hospedes
4 -> Fazer Check-Out 
5 -> Finalizar Atendimento"""

        
from time import sleep

poli = "="*50
espaco = " "*21
print(f"{poli}\n{espaco}MENU DO MOTEL\n{poli}")
print(f"{espaco}MENU{espaco}".center(50,"="))

while True:
    print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
    print(poli)
    opcao = input("=> ")

    
    if opcao == "1":
        print("Opção 1 Deu certo!")

    if opcao == "2":
        print("Opção 2 Deu certo!")

    if opcao == "3":
        print("Opção 3 Deu certo!")

    if opcao == "4":
        print("Opção 4 Deu certo!")

    if opcao == "5":
        break
