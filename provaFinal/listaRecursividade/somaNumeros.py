def soma(numero):
    if numero == 0:
        return 0
    return numero + soma(numero-1)


print(soma(10))
