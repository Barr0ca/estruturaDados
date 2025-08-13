from binarytree import bst, Node

arvore = bst(height=2, is_perfect=True)


def encontrar_index(no, valor):  # Função que encontra o index equivalente ao valor fornecido
    contador = 0
    for i in no:  # Loop para incrementar o contador até chegar ao valor
        if i.value == valor:
            return contador  # Index do valor
        contador += 1
    return None


def remove(no, valor):
    if no is None:
        return None

    if valor < no.value:
        no.left = remove(no.left, valor)
    elif valor > no.value:
        no.right = remove(no.right, valor)
    else:
        # Caso 1: nó folha
        if no.left is None and no.right is None:
            return None
        # Caso 2: só tem filho direito
        elif no.left is None:
            return no.right
        # Caso 3: só tem filho esquerdo
        elif no.right is None:
            return no.left
        # Caso 4: dois filhos — pega o menor da subárvore direita
        else:
            sucessor = no.right
            while sucessor.left:
                sucessor = sucessor.left
            no.value = sucessor.value
            no.right = remove(no.right, sucessor.value)
    return no

def insercao(no, valor):  # Função recebe o nó raíz e o valor a ser adicionado
    if not no:
        return Node(valor) 
    if valor < no.value:
        no.left = insercao(no.left, valor)
    elif valor > no.value:
        no.right = insercao(no.right, valor)
    return no

def is_height_balanced(root):
    if not root:  # Árvore vazia
        return True

    # Armazenando o valor da altura da árvore da esquerda
    altura_esquerda = -1
    if root.left:
        altura_esquerda = root.left.height

    # Armazenando o valor da altura da árvore da direita
    altura_direita = -1
    if root.right:
        altura_direita = root.right.height

    if abs(altura_esquerda - altura_direita) > 1:  # Verificação padrão de propriedade
        return False

    return is_height_balanced(root.left) and is_height_balanced(root.right)


valores = [8, 4, 12, 2, 6, 10, 14]
raiz = None
for v in valores:
    raiz = insercao(raiz, v)

print("Árvore antes da remoção:")
print(raiz)

raiz = remove(raiz, 4)
raiz = remove(raiz, 2)
raiz = remove(raiz, 6)

print("\nÁrvore depois da remoção:")
print(raiz)

print("\nBalanceada?", is_height_balanced(raiz))