# Percurso em pré-ordem

from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def pre_order(no):  # Esquema de mostrar pré-ordem visto em sala
    if no:
        print(no.value)
        pre_order(no.left)
        pre_order(no.right)


print(arvore)

pre_order(arvore)
