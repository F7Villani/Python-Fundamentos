# Aula 06 - Conjuntos

# Conjuntos são containers, assim como listas e tuplas, porém não possuem ordem, nem permitem duplacidade

conjunto = {1, 2, 3, 4} # Criando um conjunto
print(type(conjunto)) # Tipo 'set'
conjunto.add(5) # Adiciona um valor ao conjunto
conjunto.discard(2) # Deleta um valor do conjunto
print(conjunto)

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8,9}

# União de conjuntos - Valores iguais são colapsados
conjunto_uniao = conjunto.union(conjunto2)
print("União: {}".format(conjunto_uniao))

# Intersecção de conjuntos - Retorna valores contidos nos dois conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print("Interseçãao: {}".format(conjunto_interseccao))

# Diferença dos conjuntos - Retirar do primeiro tudo que é semelhante ao segundo
conjunto_diferenca = (conjunto.difference(conjunto2))
print("Diferenca entre 1 e 2: {}".format(conjunto_diferenca))

# Diferenca Simetrica - Retorna a união dos dois conjuntos retirando valores semelhantes
conjunto_diff_simetrica = conjunto2.symmetric_difference(conjunto)
print('Diferenca Simetrica: {}'.format(conjunto_diff_simetrica))

# Conjunto Subset (Subconjunto) - Retorna True/False
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,6}
conjunto_subset1 = conjunto_a.issubset(conjunto_b)
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('Conjunto 1 é subconjunto de 2: {}'.format(conjunto_subset1))
print('Conjunto 2 é subconjunto de 1: {}'.format(conjunto_subset2))

# Conjunto Superset (superconjunto) - Retorna True/false
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('Conjunto 2 é superconjunto de 1: {}'.format(conjunto_superset))

# Conversão - Valores semelhantes são colapsados
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print("Conjunto animais: {}".format(conjunto_animais))