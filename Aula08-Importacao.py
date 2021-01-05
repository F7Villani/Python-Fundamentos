# Aula 08 - Importação de Módulos

from Aula07_3_Metodos_Funcoes_Clases import Televisao
from Aula07_1_Metodos_Funcoes_Clases import Calculadora
from Aula08_2_Contador_de_Letras import contador_letras

if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5,10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista ))