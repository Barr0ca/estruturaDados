# Ordem decrescente de um número n até 1

def desc(n):
    if n == 1:
        return n
    
    print(n)
    
    return desc(n-1)


print(desc(5))
