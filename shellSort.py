def shellSort(list):
  tamLista = len(list)
  gap = len(list) // 2
  while gap > 1:
    for i in range(gap):
      insertion(list, tamLista - 1)
    gap = gap // 2
  return list

def insertion(list, index):
  while index > 0:
    if list[index] < list[index - 1]:
      aux = list[index]
      list[index] = list[index - 1]
      list[index - 1] = aux
    index -= 1
  return list

listaD = [54,26,93,17,77,31,44,55,20]
print("lista desordenada")
print(listaD)
listaO = shellSort(listaD)
print("lista ordenada")
print(listaO)