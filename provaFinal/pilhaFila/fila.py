# Fila
from collections import deque
from random import randint

fila = deque([])

for i in range(3):
    fila.append(randint(0, 100))
    print(fila)

for c in range(len(fila)):
    print(fila.popleft())
