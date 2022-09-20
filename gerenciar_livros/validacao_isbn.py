#Validação de ISBN dos livros


"""Funções para validar números de ISBN.
ORIGINAL: http://maracujah.net/files/software/nif.py
https://gist.github.com/dreispt/024dd11c160af58268e2b44019080bbf
"""


import string

# tamanhos dos nums do BI, contribuinte, NISS, NIB e ISBN
(LEN_ISBN) = (10)


def _toIntList(numstr, acceptX=0):
    res = []
    # converter todos os dígitos
    for i in numstr:
        if i in string.digits:
            res.append(int(i))
    # converter dígito de controle no ISBN
    if acceptX and (numstr[-1] in 'Xx'):
        res.append(10)
    return res

def controlISBN(isbn):
    "Verifica a validade de ISBN."
    # converter para lista de inteiros
    isbn = _toIntList(isbn, 1)

    # verificar tamanho do número
    if len(isbn) != LEN_ISBN:
        return False

    # computar soma de controlo
    sum = 0
    for pos, dig in enumerate(isbn[:-1]):
        sum += ((pos + 1) * dig)

    # verificar soma de controlo
    return sum % 11 == isbn[-1]

isbn1 = (input('Digite um ISBN-10 válido: '))

if __name__ == "__main__":

    print("O resultado do teu ISBN-10 é:", controlISBN(isbn1))


    