# Contando os nós internos de uma BST

from binarytree import bst

arvore = bst(height=2)


# Lógica inversa ao nós folhas, caso haja nós ou na esquerda ou na direita é um nó interno
def conta_nos_internos(no):
    if not no:
        return 0
    if no.left or no.right:
        return 1 + conta_nos_internos(no.left) + conta_nos_internos(no.right)
    else:  # Caso seja um nó folha
        return 0


print(arvore)

print(conta_nos_internos(arvore))
