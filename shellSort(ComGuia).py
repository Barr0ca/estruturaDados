def shellSort(list):
  gap = len(list) // 2
  while gap > 0:
    for comeco in range(gap):
      for i in range(comeco+gap, len(list), gap):
        valorAtual = list[i]
        posicao = i
        while posicao >= gap and list[posicao-gap] > valorAtual:
          list[posicao] = list[posicao-gap]
          posicao = posicao - gap
        list[posicao] = valorAtual
    gap = gap // 2
  return list

listaD = [54,26,93,17,77,31,44,55,20,88]
print("lista desordenada")
print(listaD)
listaO = shellSort(listaD)
print("lista ordenada")
print(listaO)