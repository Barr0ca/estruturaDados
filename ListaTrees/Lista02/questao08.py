# Construindo uma BST a partir de uma pré-ordem

from binarytree import Node


def construir_bst_preordem(preordem, index, minimo=float('-inf'), maximo=float('inf')):
    if index[0] == len(preordem):
        return None

    valor = preordem[index[0]]
    if not (minimo < valor < maximo):
        return None

    # Cria o nó com o valor atual e incrementa índice
    no = Node(valor)
    index[0] += 1

    # Constrói recursivamente a subárvore esquerda e direita
    no.left = construir_bst_preordem(preordem, index, minimo, valor)
    no.right = construir_bst_preordem(preordem, index, valor, maximo)

    return no


preordem = [8, 5, 1, 7, 10, 12]
index = [0]
no = construir_bst_preordem(preordem, index)

print(no)
