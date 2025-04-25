from math import ceil

def shellSort(list):
  gap = ceil(len(list)/2)
  while gap > 0:
    for i in range(0, len(list)-gap):
      valorAtual = list[i]
      if list[i+gap]<valorAtual:
        aux = list[i]
        list[i] = list[i+gap]
        list[i+gap] = aux
    gap -= 1
  return list

listaD = [3,1,5,10,15,90,2]
print("lista desordenada")
print(listaD)
listaO = shellSort(listaD)
print("lista ordenada")
print(listaO)