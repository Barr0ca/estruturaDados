from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def busca_no(no, valor):
    if not no:
        print('Valor não encontrado')
        return
    elif no.value < valor:
        busca_no(no.right, valor)
        return
    if no.value > valor:
        busca_no(no.left, valor)
        return
    else:
        print(f'Valor {no.value} encontrado.')


busca_no(arvore, 6)
