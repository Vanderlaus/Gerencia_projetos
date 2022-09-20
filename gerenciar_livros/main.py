from time import sleep
import string

livros = []

poli = "="*50
espaco = " "*21
print(f"{poli}\n{espaco}LIVRARIA\n{poli}")

while True:
    print(f"{espaco}MENU{espaco}".center(50,"="))
    print("(1) Cadastro de Livros\n(2) Lista de Livros\n(3) Excluir Livros\n(4) Sair")
    print(poli)
    opcao = input("=> ")

    if not(opcao.isnumeric()):
        print("Letras não sao validas como opção!")
        
    elif opcao == "1":
        titulo = str(input("Digite os seguintes dados do livro\nTítulo: "))
        editora = str(input("Editora: "))
        autor = str(input("Autor: "))
        genero = str(input("Gênero: "))
        ano = int(input("Ano Publicação: "))
        
        while True:
            isbn = input("ISBN: ")
                    
            res = []
            for i in isbn:
                if i in string.digits:
                    res.append(int(i))

            if 1 and (isbn[-1] in 'Xx'):
                res.append(10)

            if len(res) != 10:
                hasError = True

            sum = 0
            for pos, dig in enumerate(res[:-1]):
                sum += ((pos + 1) * dig)

            hasError = sum % 11 == res[-1]

            if hasError:
                dicionario = {
                    'titulo': titulo, 
                    'editora': editora,
                    'autor': autor,
                    'genero': genero,
                    'ano': ano,
                    'isbn': isbn
                }
                livros.append(dicionario)
                print("Deu certo!")
                break
            
            else:
                print("Deu erro!")

    elif opcao == "2":
        if len(livros) == 0:
            print(f"{poli}\n******************* LISTA VAZIA ******************\n{poli}")
        else:
            for i in livros:
                print(f"Titulo: {i['titulo']} Editora: {i['editora']} Autor: {i['autor']} Genero: {i['genero']} Ano: {i['ano']} ISBN: {i['isbn']}")
                sleep(1)

    elif opcao == "3":
        if len(livros) == 0:
            print(f"{poli}\n******************* LISTA VAZIA ******************\n{poli}")
        else:
            for i, v in enumerate(livros):
                print(f"{i} - {v['titulo']}")
            while True:
                indice = input("Digite o indice que voce quer EXCLUIR: ")
                if not(indice.isnumeric()):
                    print("Letras não sao validas como opção!")
                elif int(indice) >= len(livros):
                    print("Indice nao existe!")
                else:
                    break
            livros.pop(int(indice))

    elif opcao == "4":
        break
    