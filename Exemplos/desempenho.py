from time import time


def desempenho(funcao, lista: list):
    tempoInicial = time()
    print(funcao(lista))
    tempoFinal = time()
    tempoTotal = tempoFinal-tempoInicial

    print(
        f'Tempo de execução da função: {tempoTotal}')
