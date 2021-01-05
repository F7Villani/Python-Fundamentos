# Aula 08 Lambda

contador_letras = lambda lista: [len(x) for x in lista]

lista = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista))

soma = lambda a,b: a+b
print(soma(5,10))

calculadora = {
    'soma': lambda a,b: a+b, 
    'subtracao': lambda a,b: a-b, 
    'multiplicacao': lambda a,b: a*b, 
    'divisao': lambda a,b: a/b
}

soma = calculadora['soma']
print(soma(10,5))