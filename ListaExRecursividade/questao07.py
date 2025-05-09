# Números de dígitos de um número

def digitos(n):
    if n == 0:
        return 0
    return 1 + digitos(n//10)

print(digitos(843))
