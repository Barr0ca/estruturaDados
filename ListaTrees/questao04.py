from binarytree import bst

arvore = bst(height=2, is_perfect=True)

def visita_no(no):
    if no.left:
        print(no.value)
        visita_no(no.left)
        visita_no(no.right)
    else:
        print(no.value)

print(arvore)

visita_no(arvore)