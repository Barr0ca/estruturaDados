from binarytree import bst, Node, get_index

def add_valor(no, valor):
    if get_index(no, no) != valor:
        if get_index(valor, valor) > get_index(no, no):
            if get_index(no, no.rigth):
                add_valor(get_index(no, no.rigth), valor)
            else:
                get_index(no, no.rigth) == Node(valor)
        else:
            if get_index(no, no.left):
                add_valor(get_index(no, no.left), valor)
            else:
                get_index(no, no.left) == Node(valor)
    else:
        return print('Já existe esse valor.')
    return valor

arvore = bst(height=2, is_perfect=True)

print(arvore)

add_valor(7, arvore)
