# list = [17,26,93,44,77,31,54,55,20]
list = [54,26,93,17,77,31,44,55,20]

gap = len(list) // 2
while gap > 0:
  for comeco in range(gap):
    for i in range(comeco+gap, len(list), gap):
      valorAtual = list[i]
      posicao = i
      if list[posicao-gap]>valorAtual:
        aux = list[posicao]
        list[posicao] = list[posicao-gap]
        list[posicao-gap] = aux
        
  gap = gap // 2