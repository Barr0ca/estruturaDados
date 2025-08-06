# Busca em uma BST

from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def busca_no(no, valor):
    if not no:  # Caso o valor procurado não exista
        print('Valor não encontrado')
        return
    elif no.value < valor:  # Se o valor for maior que o nó atual busca na direita
        busca_no(no.right, valor)
        return
    if no.value > valor:  # Se o valor for menor que o nó atual busca na esquerda
        busca_no(no.left, valor)
        return
    else:
        print(f'Valor {no.value} encontrado.')


busca_no(arvore, 6)
