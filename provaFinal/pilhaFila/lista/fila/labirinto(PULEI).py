from collections import deque


def bfs(labirinto: deque, inicio: tuple, fim: tuple):
    fila = deque([])
    visitados = deque([])

    fila.append(inicio)
    visitados.append(inicio)


labirinto = [[0, 0, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0]]
for linha in labirinto:
    print(linha)
print(labirinto[0][2])
