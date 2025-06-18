def bubbleSort(list):
    for j in range(len(list)):
        for i in range(len(list)-j-1):
            if list[i] > list[i+1]:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
    return list

lista = [8,10,5,4,1]
print(bubbleSort(lista))