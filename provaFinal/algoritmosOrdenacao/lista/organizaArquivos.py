import os


def shell_sort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap][1] > temp[1]:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


# Caminho da pasta que você quer acessar (mude para a sua pasta)
pasta = '/home/ian/Imagens/Capturas de tela'

# Lista para armazenar (nome_arquivo, tamanho)
arquivos = []

for nome in os.listdir(pasta):
    caminho_completo = os.path.join(pasta, nome)
    if os.path.isfile(caminho_completo):
        tamanho = os.path.getsize(caminho_completo)
        arquivos.append((nome, tamanho))

arquivos_ordenados = shell_sort(arquivos)

for nome, tamanho in arquivos_ordenados:
    print(f'{nome}: {tamanho / (1024*1024):.2f} MB')
