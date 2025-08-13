import string


def frequencia(texto: str):
    contador_frequencia = {}
    texto = texto.split()

    for palavra in texto:
        palavra_limpa = palavra.strip(string.punctuation).lower()
        if contador_frequencia.get(palavra_limpa) is None:
            contador_frequencia[palavra_limpa] = 1
        else:
            contador_frequencia[palavra_limpa] += 1

    for palavra, frequencia in contador_frequencia.items():
        print(f"{palavra} apareceu {frequencia} vez(es).")


frequencia('arroz, feijão e pão arroz e arroz,')
