from binarytree import bst

arvore = bst(height=2, is_perfect=False)


def soma_val_nos(no):
    if not no:  # Caso não exista nó atual retorna 0
        return 0
    # Soma o valor do nó atual a cada return
    return no.value + soma_val_nos(no.left) + soma_val_nos(no.right)

def conta_nos(root):
    if not root:
        return 0
    return 1 + conta_nos(root.left) + conta_nos(root.right)
     

def average_value(root):
    if not root:
        return 0
    nos = conta_nos(root)
    soma = soma_val_nos(root)
    return soma/nos

print(arvore)

print(f'{average_value(arvore):.2}')

# print(conta_nos(arvore))