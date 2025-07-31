from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def busca_no(no, valor):
    if no.value > valor:
        busca_no(no.left, valor)
    elif no.value < valor:
        busca_no(no.right, valor)
    else:
        print(no.value)


busca_no(arvore, 6)
