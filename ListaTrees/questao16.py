from binarytree import bst

arvore = bst(height=2)


def soma_val_nos(no):
    if not no:
        return 0
    return no.value + soma_val_nos(no.left) + soma_val_nos(no.right)


print(arvore)

print(soma_val_nos(arvore))
