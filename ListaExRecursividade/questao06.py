# Método de Euclides (MDC)

def mdc(n1, n2):
    if n1 % n2 == 0:
        return n2
    elif n2 % n1 == 0:
        return n1
    if n1 > n2:
        return mdc(n1%n2, n2)
    else:
        return mdc(n1, n2%n1)
    
print(mdc(108, 120))
