# Aula 02 - Operações Aritiméticas e Interação com o usuário

# Requisitando números do tipo 'int'
a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

# Fazendo operações e guardando em variáveis
soma = a + b
multiplicacao = a*b
subtracao = a - b
divisao = a/b
resto = a%b

# Descobrir o tipo de uma variável
print(type(soma))

# Maneiras de exibir as variáveis 
## print('Soma: '+ str(soma))
## print('Soma: ', soma)
print('Soma: {}\nSubtracao: {} '
    '\nMultiplicacao: {} \nDivisao: {}'
 '\nResto: {}'.format(soma, subtracao, multiplicacao, divisao, resto))
