from binarytree import bst

arvore = bst(height=3)


def ver_balan(no):
    if not no:
        return True

    altura_esquerda = -1
    if no.left:
        altura_esquerda = no.left.height

    altura_direita = -1
    if no.right:
        altura_direita = no.right.height

    if abs(altura_esquerda - altura_direita) > 1:
        return False

    return ver_balan(no.left) and ver_balan(no.right)


print(arvore)

print(ver_balan(arvore))
