
livros = []

print("Cadastro de Livros\n(1) Cadastrar Livros\n(2) Listar Livros Cadastrados\n(3) Sair")
id = input("Opção: ")

while True:    
    if id == str(1):
        titulo = str(input("Digite os seguintes dados do livro\nTítulo: "))
        editora = str(input("Editora: "))
        autor = str(input("Autor: "))
        genero = str(input("Gênero: "))
        ano = int(input("Ano Publicação: "))
        isbn = int(input("ISBN: "))
        dicionario = {
        'titulo': titulo, 
        'editora': editora,
        'autor': autor,
        'genero': genero,
        'ano': ano,
        'isbn': isbn}
    
    livros.append(dicionario)


