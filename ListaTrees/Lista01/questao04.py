# Percurso em in-ordem

from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def in_order(no):  # Esquema de mostrar in-ordem visto em sala
    if no:
        in_order(no.left)
        print(no.value)
        in_order(no.right)


print(arvore)

in_order(arvore)
