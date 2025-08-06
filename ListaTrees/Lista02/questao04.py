# Verificando se a BST está balanceada

from binarytree import bst

arvore = bst(height=3)


def ver_balan(no):
    if not no:  # Árvore vazia
        return True

    # Armazenando o valor da altura da árvore da esquerda
    altura_esquerda = -1
    if no.left:
        altura_esquerda = no.left.height

    # Armazenando o valor da altura da árvore da direita
    altura_direita = -1
    if no.right:
        altura_direita = no.right.height

    if abs(altura_esquerda - altura_direita) > 1:  # Verificação padrão de propriedade
        return False

    return ver_balan(no.left) and ver_balan(no.right)


print(arvore)

print(ver_balan(arvore))
