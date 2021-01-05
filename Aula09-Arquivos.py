# Aula 09 Arquivos

import shutil

def escrever_arquivo(texto):
    # SE NAO informarmos um diretorio, o arquivo sera criado junto ao .py 
    arquivo = open('teste.txt', 'w',)
    # 'w' sobrepoe qualquer informacao ja no arquivo
    # 'a' atualiza a informacao ja no arquivo
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    lista_media = []
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/ro_sk/OneDrive - Instituto Maua de Tecnologia/Documentos/Python/Ola-Mundo/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'C:/Users/ro_sk/OneDrive - Instituto Maua de Tecnologia/Documentos/Python/Ola-Mundo/notas_alunos.txt' )
        
        
     

if __name__ == "__main__":
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Segunda linha.\n')
    #ler_arquivo('teste.txt')
    # aluno = '\nCesa,8,5,6,9\n'
    # atualizar_arquivo('notas.txt', aluno)
    #lista_media = media_notas('notas.txt')
    #print(lista_media) 
    move_arquivo('notas.txt')


