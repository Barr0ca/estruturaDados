# Soma nota de alunos em uma hashtable

def soma_notas_ht(ht1: dict, ht2: dict):
    ht_notas_somadas = {}

    for aluno, nota in ht1.items():
        if aluno not in ht_notas_somadas:
            ht_notas_somadas[aluno] = nota
        else:
            ht_notas_somadas[aluno] += nota 

    for aluno, nota in ht2.items():
        if aluno not in ht_notas_somadas:
            ht_notas_somadas[aluno] = nota
        else:
            ht_notas_somadas[aluno] += nota 
                
    return ht_notas_somadas


ht_notas_alunos_1 = {'Paulo': 7.0, 'Ian': 7.3, 'Maria': 8.8, 'José': 8}
ht_notas_alunos_2 = {'Ian': 8.9, 'Paulo': 6.3, 'Maria': 8.0, 'José': 10, 'Tomas': 8}

print(soma_notas_ht(ht_notas_alunos_1, ht_notas_alunos_2))