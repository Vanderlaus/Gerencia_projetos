        
from time import sleep
import string

livros = []

poli = "="*50
espaco = " "*21
print(f"{poli}\n{espaco}LIVRARIA\n{poli}")
print(f"{espaco}MENU{espaco}".center(50,"="))

while True:
    print(f"(1) Cadastro de Livros\n(2) Lista de Livros\n(3) Excluir Livros\n(4) Sair")
    print(poli)
    opcao = input("=> ")

    if not(opcao.isnumeric()):
        print("Letras não sao validas como opção!")
        pass
    if opcao == "1":
        titulo = str(input("Digite os seguintes dados do livro\nTítulo: "))
        editora = str(input("Editora: "))
        autor = str(input("Autor: "))
        genero = str(input("Gênero: "))
        ano = int(input("Ano Publicação: "))
        isbn = input("ISBN: ")

        dicionario = {
            'titulo': titulo, 
            'editora': editora,
            'autor': autor,
            'genero': genero,
            'ano': ano,
            'isbn': isbn
        }

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
            livros.append(dicionario)
            print("Deu certo!")
        
        else:
            print("Deu erro!")


    if opcao == "2":
        print("Lista de Livros")
        for i in livros:
            print(f"Titulo: {i['titulo']} Editora: {i['editora']} Autor: {i['autor']} Genero: {i['genero']} Ano: {i['ano']} ISBN: {i['isbn']}")

    if opcao == "3":
        print("Excluir Livros Cadastrados")
        pass

    if opcao == "4":
        break
