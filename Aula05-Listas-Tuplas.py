# Aula 05 - Listas e Tuplas

# Listas são mutáveis e por convenção e facilidade, colocamos 
# dentro delas variáveis de mesmo tipo

# Criando Listas
lista = [10,2,8,5,3,4]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# Ordenação das Listas
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

# Inversão dos valores da Lista 
lista_animal.reverse()
print(lista_animal)

# Tuplas são como listas, mas são imutáveis
tupla = (1,10,2,5,6)
tupla_lista = tuple(lista)
# Transformando uma lista numa tupla
print(tupla_lista)
print(tupla)

print(lista_animal[1]) # Acessando um elemento da lista pelo seu index

# Somando todos os elementos da lista
soma = 0
for i in lista:
    print(i)
    soma +=i 
print(soma)

print(sum(lista)) # Função que retorna a soma todos os elementos da lista
print(max(lista)) # Função que retorna o maior valor da lista

# Verificando se um elemento específico está contido na lista
if 'gato' in lista_animal:
    print("Existe um 'gato' na lista")
else:
    print("Não existe um gato na lista")

