def contador(numero: int):
    if numero == 0:
        return 0
    return 1 + contador(numero//10)


print(contador(100))
