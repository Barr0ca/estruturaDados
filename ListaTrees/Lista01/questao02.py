# Inserção em uma BST

from binarytree import bst, Node

arvore = bst(height=2, is_perfect=True)


def insercao(no, valor):  # Função recebe o nó raíz e o valor a ser adicionado
    if no.value != valor:  # Só adiciona o valor se ele for diferente de algum nó
        if valor > no.value:  # Se valor for maior que nó atual ele adiciona à direita
            if no.right:
                # Nesse bloco de IF ELSE só adiciona o valor se não tiver mais valor à direita
                insercao(no.right, valor)
            else:
                no.right = Node(valor)
        # Nesse bloco segue mesma lógica, so que para esquerda (valor menor que o nó atual)
        else:
            if no.left:
                insercao(no.left, valor)
            else:
                no.left = Node(valor)


insercao(arvore, 5)
insercao(arvore, 2)

print(arvore)
