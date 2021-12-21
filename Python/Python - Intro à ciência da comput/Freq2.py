# Aluno: Renan Duarte Pires
# Matrícula: 20103003
# Linguagem: Python 3.0


import random

# ATIVIDADE 2

"""
# Problema 1

# Entrada
numero= int(input("Insira um valor inteiro positivo (maior ou igual a 2) -> "))
n= numero


# Função com lógica de resolução do problema
def calculo (n):
    n= numero
    m=3
    calculo= 0
    for x in range(2,(n+1),1):

        if x == 2:
            calculo= (x/m)
            
        else:
            calculo= calculo + (x/(m))
        
        m=m+2
        
    print("Sua resposta é ->", calculo) 

# Filtro para valores errados
while numero < 2:
    print("Favor inserir valor correto")
    numero= int(input("Insira um valor inteiro positivo (maior ou igual a 2) -> "))

# Após checagem, processamento da função
calculo(n)
"""

"""
# Problema 2

# Entrada
num= int(input("Insira um valor entre 1 e 10 -> "))

# Função com lógica para resolução do problema
def randomizado (num):
    soma= 0
    tentativas= 0
    lista= []

    # Fazer 10 tentativas, no máximo.
    while (soma != num) and (tentativas < 11):
        tentativas= tentativas + 1
        randomizado= random.randint(1,10)
        lista.append(randomizado)
        soma= randomizado + soma
    if soma == num:
        print(f"Foram necessárias {tentativas}, e os valores gerados foram: {lista}.")
    else:
        print(f"Foram realizadas {tentativas} tentativas e não foi possível chegarmos a número desejado!")
        print(f"Lista das tentativas: {lista}")
    
randomizado(num)
"""


"""
# Problema 3

# Entrada
investimento= float(input("Informe o valor a ser investido mensalmente -> R$"))
juros= float(input("Informe a taxa de juros a ser aplicado mensalmente (e.g.: 10 = 10%) ->"))
ano= 0
total= investimento

def calculo(juros,ano,total,investimento):
    repetir= "s"
    while repetir == "S" or repetir == "s":
        ano= ano +1
        for i in range(1,13):
            if i==1:
                total= (total)* (1+(juros/100))
                print(total)
            else:
                total= (total+investimento)* (1+(juros/100))
                print(total)
        print(f"O valor após {ano} ano(s) é: R${total} .")

        repetir= input("Deseja processar mais um ano ? (S/N) -> ") 
    


calculo(juros,ano,total,investimento)
"""   