# Verificando a propriedade de uma BST

from binarytree import bst

arvore = bst(height=2, is_perfect=True)


# Parâmetros para fazer a verificação de valores possíveis, no caso da raíz é +infinito e -infinito
def ver_bst(no, minimo=float('-inf'), maximo=float('inf')):
    if not no:
        return True
    if not (minimo < no.value < maximo):  # Verificação de valores
        return False
    # Para valores da direita a verificação o valor precisa ser maior que o valor do nó pai
    # Para valores da esquerda a verificação o valor precisa ser menor que o valor do nó pai
    return ver_bst(no.left, minimo, no.value) and ver_bst(no.right, no.value, maximo)


print(arvore)

print(ver_bst(arvore))
