from time import sleep

poli = "="*50
espaco = " "*21
print(f"{poli}\n{espaco}LIVRARIA\n{poli}")
print(f"{espaco}MENU{espaco}".center(50,"="))
print(f"(1) Cadastro de Livros\n(2) Lista de Livros\n(3) Excluir Livros\n(4) Sair")
print(poli)
opcao = input("=> ")

if not(opcao.isnumeric()):
    print("Letras não sao validas como opção!")
    pass
if opcao == "1":
    print("Digite o nome do livro: ")
    pass
if opcao == "2":
    print("Lista de Livros")
    # criar um for com 2 indices, i para index e v para value e usar o enumerate
    # e com isso poder listas os livros com os indices ex: for i, v in <lista>:
    # print(f"{i} - {v}")
    # sleep(1)
if opcao == "3":
    print("Excluir Livros Cadastrados")
    pass

if opcao == "4":
    pass
    


