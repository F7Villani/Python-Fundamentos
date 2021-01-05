#Aula 10 - Datetime

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():

    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual))
    # Olhas as diretivas na documentacao do datetime

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario))
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018,6,20,15,30,20)
    print(data_criada)
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    nova_data = data_convertida + timedelta(days=365)
    print(nova_data)


if __name__ == '__main__':
    #trabalhando_com_time()
    trabalhando_com_datetime()
