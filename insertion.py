def insertion(lista:list[int], indice: int) -> list[int]:
    i = indice # início
    while (i > 0): #condição de parada
        if lista[i-1] > lista[i]:
            aux = lista[i-1]
            lista[i-1] = lista[i]
            lista[i] = aux
        else:
            break
        i-= 1 #passo
    return lista

def insertion_sort(lista:list[int]) -> list[int]:
    i = 1 #início
    while (i < len(lista)): #condição de parada
        lista = insertion(lista,i)
        i+=1 # passo
        
    return lista

lista_desordenada = [3,1,5,10,15,90,2]
print("lista desordenada")
print(lista_desordenada)
lista_ordenada = insertion_sort(lista_desordenada)
print("lista ordenada")
print(lista_ordenada)