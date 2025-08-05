from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def pos_order(no):
    if no:
        pos_order(no.left)
        pos_order(no.right)
        print(no.value)


print(arvore)

pos_order(arvore)
