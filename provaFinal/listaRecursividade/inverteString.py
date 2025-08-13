def inverte(palavra):
    if len(palavra) == 0:
        return ''
    return palavra[len(palavra)-1] + inverte(palavra[:-1])


print(inverte('Batata'))
