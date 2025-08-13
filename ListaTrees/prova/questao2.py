from binarytree import bst

arvore = bst(height=2)


def list_leaf_values(root, lista: list):
    if root:
        if not root.left and not root.right: 
            lista.append(root.value)
        list_leaf_values(root.left, lista)
        list_leaf_values(root.right, lista) 
    return lista

lista = []

print(arvore)

print(list_leaf_values(arvore, lista))
