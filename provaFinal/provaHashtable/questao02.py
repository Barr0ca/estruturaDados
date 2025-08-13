import string

frequencia = {}

# Ler linhas do usuário
while True:
    linha = input("Digite um texto (ou vazio para sair): ")
    if not linha:
        break
    # Remover pontuação e converter para minúsculas
    linha = linha.lower().translate(str.maketrans('', '', string.punctuation))
    palavras = linha.split()
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1

# Mostrar contagem de todas palavras
for palavra, qtd in frequencia.items():
    print(f"A palavra '{palavra}' apareceu {qtd} vez(es)")

# Mostrar as 10 palavras mais frequentes
top10 = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop 10 palavras mais frequentes:")
for palavra, qtd in top10:
    print(f"{palavra}: {qtd} vez(es)")
