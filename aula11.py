lista = [0,10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
    
    
    
    
except ZeroDivisionError:
    print('Nao é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex) )

else:
    print('Executa quando nao ocorre exceção')

finally:
    print('Sempre executa')
    print('Fechando o arquivo...')
    arquivo.close()