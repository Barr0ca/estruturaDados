# Calcula média de alunos em uma hashtable

def ht_calc_media(ht: dict):
    for aluno, notas in ht.items():
        print(aluno, (sum(notas)/len(notas)))

ht = {'Ian': [10,80,30,100], 'Paulo': [30,70,30,80]}

ht_calc_media(ht)
