from binarytree import bst

arvore = bst(height=2)

def conta_nos_folhas(no):
    if not no:
        return 0
    if not no.left and not no.right:
        return 1
    return conta_nos_folhas(no.left) + conta_nos_folhas(no.right)

print(arvore)

print(conta_nos_folhas(arvore))