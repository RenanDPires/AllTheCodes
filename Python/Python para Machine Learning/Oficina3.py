
# Bibliotecas a serem usadas (TIve que setar o local, pois meu uso o python "original" em inglês) 
import locale
from datetime import datetime, date
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Dados a serem usados
# Entrada de aniversários
aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989', '16 de Junho de 1987', '04/07/1990']

# Formatos nos quais esse código funciona
formatos= ['%d/%m/%Y','%d de %B de %Y', '%Y-%B-%d', '%d/%b/%Y', '%d %B %Y' ]

# Lista auxiliadora para guardar as datas já convertidas 
aniversariosConvertidos= []

# Função de conversão de string para datetime
def conversao (aniversarios,formatos,aniversariosConvertidos):
    for i in range(len(aniversarios)):
        for l in range(len(formatos)):
            try:
                aniversariosConvertidos.append(datetime.strptime(aniversarios[i], formatos[l] ))
            except ValueError:
                pass
    return aniversariosConvertidos

# Chamado da função de conversão
conversao(aniversarios,formatos,aniversariosConvertidos)

# Ordenação dos aniversarios por mês e dia, respectivamente
aniversariosConvertidos=sorted(aniversariosConvertidos, key=lambda d: (d.month, d.day))

# Aniversarios sem o ano (apenas para a checagem de hoje)
aniversariosApenasMesEDia= []

# Função de conversão de datetime para string sem ano
def mesEDia (aniversariosConvertidos,aniversariosApenasMesEDia):
    for i in range(len(aniversariosConvertidos)):
        aniversariosApenasMesEDia.append(aniversariosConvertidos[i].strftime('%m, %d'))

# Chamado da função de conversão para string do mês e dia
mesEDia(aniversariosConvertidos,aniversariosApenasMesEDia)

# Salvamento do dia de hoje em uma variável
hoje= date.today()

# Saída do que foi pedido da questão
if (hoje.strftime('%m, %d')) in aniversariosApenasMesEDia:
    print(hoje.strftime("Hoje, %A, %d de %B de %Y tem aniversário!"))
else:
    print("Infelizmente não tem bolinho hoje")
