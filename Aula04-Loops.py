# Aula 04 - Loops

# Exemplo 01 - Loop com 'for'

resultado = 0
for x in range(1, 10):
    # Loop que percorre o Range, começando em 1 indo até quase 10
    print(x)
    if x < 9:
        resultado += 1
        # resultado = resultado + 1
print(resultado)

# Exemplo 02 - Loop com 'while'

import os
a = 0
while a != 10:
    a = int(input("Digite o numero 10: "))
    os.system("CLS")
    # O programa apenas sairá do loop quando o usuário digitar o número 10
print("Obrigado!")

# Exemplo 03 - Verificando se o número informado é PRIMO

a = int(input("Digite um número: "))
c = 0
for x in range(1,a+1):
    # Loop que roda de 1 até 'a'
    if a%x == 0:
        c+=1
if c == 2:
    print("{} é PRIMO".format(a))
else:
    print("{} não é PRIMO".format(a))

# Exemplo 04 - Todos os números PRIMOS anteriores ao número informado

num = int(input("Digite um número: "))
for i in range(num+1):
    # For rodando de 0 até o número informado
    # Se o primeiro parâmetro do Range não for informado ele inicia no 0
    div = 0
    for x in range(1, i+1):
        # For rodando de 1 até o número do primeiro For
        if i%x == 0:
            div+=1

    if div == 2:
        # Exibi o número caso ele seja PRIMO
        print("{}".format(i))
   