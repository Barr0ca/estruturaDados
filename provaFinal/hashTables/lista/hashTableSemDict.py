class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, chave):
        return sum(ord(c) for c in str(chave)) % self.tamanho

    def inserir(self, chave, valor):
        index = self.hash(chave)
        self.tabela[index] = (chave, valor)

    def buscar(self, chave):
        index = self.hash(chave)
        if self.tabela[index] is None:
            return None
        elif self.tabela[index][0] == chave:
            return self.tabela[index][1]
        return None


ht = HashTable(10)
ht.inserir("Ronaldo", 9)
ht.inserir("Messi", 10)

print(ht.buscar("Ronaldo"))
print(ht.buscar("Messi"))
print(ht.buscar("Pelé"))
