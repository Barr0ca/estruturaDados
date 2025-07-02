def anagramas(lista: list):
    lista_ordenada1 = sorted(lista)
    lista_ordenada2 = sorted(lista)
    for palavra1 in lista_ordenada1:
        for palavra2 in lista_ordenada2:
            verifica_anagrama

def verifica_anagrama(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False