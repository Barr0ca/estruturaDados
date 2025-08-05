from binarytree import bst, Node

arvore = bst(height=2, is_perfect=True)


def insercao(no, valor):
    if no.value != valor:
        if valor > no.value:
            if no.right:
                insercao(no.right, valor)
            else:
                no.right = Node(valor)
        else:
            if no.left:
                insercao(no.left, valor)
            else:
                no.left = Node(valor)

insercao(arvore, 5)
insercao(arvore, 2)

print(arvore)
