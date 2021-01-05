# Aula 03 - Condicionais

## Exemplo 01

# Requisitando as notas ao usuário
a = int (input("Primeiro Bimestre: "))
b = int (input("Segundo Bimestre: "))
c = int (input("Terceiro Bimestre: "))
d = int (input("Quarto Bimestre: "))

# Calculando a média das notas
media = (a+b+c+d)/4

# Condicional de validação das notas
if a<=10 and b<=10 and c<=10 and d<=10:
    print("Média: {}".format(media))
else:
    print("Foi informada alguma nota errada!")

## Exemplo 02

# Requisitando dois valores ao usuário
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

# Condição que determina se há pelo menos um par entre os valores informados
if (a%2)==0 or (b%2)==0:
    print("Há pelo menos um número PAR entre {} e {}".format(a,b))
else:
    print("Não há nenhum número PAR informado.")

# Condição que verifica se o valor 'a'é par ou ímpar
if (a%2) == 0:
    print("O número {} é PAR.".format(a))
else:
    print("O número {} é ÍMPAR.".format(a))

## Exemplo 03

# Requisitando valores ao usuário
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

# Condição para encontrar o maior número entre os informados
if (a>b) and (a>c):
    print("O maior número é {}".format(a))
elif (b>a) and (b>c):
    print("O maior número é {}".format(b))
else:
    print("O maior número é {}".format(c))

