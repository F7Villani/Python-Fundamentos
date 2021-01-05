#Aula 07.2 - Métodos, Funções e Clases

# Criando e usando uma clase sem o '__init__'
class Calculadora:
    
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora() # Não é necessário passar os parâmetros aqui
print(calculadora.soma(10,2))
print(calculadora.subtracao(10,2))
print(calculadora.multiplicacao(10,2))
print(calculadora.divisao(10,2))