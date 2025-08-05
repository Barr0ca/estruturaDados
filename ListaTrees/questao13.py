from binarytree import bst

arvore = bst(height=2)

def conta_nos_internos(no):
    if not no:
        return 0
    if no.left or no.right:
        return 1 + conta_nos_internos(no.left) + conta_nos_internos(no.right)
    else:
        return 0

print(arvore)

print(conta_nos_internos(arvore))