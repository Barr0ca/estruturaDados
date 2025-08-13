from collections import deque


def rem_fila(fila: deque):
    print(f"Cliente {fila.popleft()} atendido.")


def rem_pilha(pilha: list):
    print(f"Cliente {pilha.pop()} atendido.")


def caixa_fila(clientes: list):
    fila_clientes = deque(clientes)

    for i in range(len(fila_clientes)):
        rem_fila(fila_clientes)


def caixa_pilha(clientes: list):
    pilha_clientes = clientes.copy()

    for i in range(len(pilha_clientes)):
        rem_pilha(pilha_clientes)


pessoas = ['Ronaldo', 'Garrincha', 'Rivaldo',
           'Romário', 'Neymar', 'Roberto', 'Tafarell', 'Messi']

print('\nCOMPORTAMENTO FILA')
caixa_fila(pessoas)

print('\nCOMPORTAMENTO PILHA')
caixa_pilha(pessoas)
