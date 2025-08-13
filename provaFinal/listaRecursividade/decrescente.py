def decrescente(numero):
    if numero == 1:
        return print(1)
    print(numero)
    return decrescente(numero-1)


decrescente(10)
