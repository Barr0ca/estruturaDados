from binarytree import bst

arvore = bst(height=2, is_perfect=True)

def encontrar_index(no, valor):
    contador = 0
    for i in no:
        if i.value == valor:
            return contador
        contador += 1
    return None 

index = encontrar_index(arvore, 0)

def remove(no, index):
    if index is None:
        return 'Valor não encontrado.'
    del no[index]
    return no

print(arvore)

print(remove(arvore, index))
