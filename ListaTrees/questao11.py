from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def ver_bst(no, minimo=float('-inf'), maximo=float('inf')):
    if no is None:
        return True
    if not (minimo < no.value < maximo):
        return False
    return ver_bst(no.left, minimo, no.value) and ver_bst(no.right, no.value, maximo)


print(arvore)

print(ver_bst(arvore))
