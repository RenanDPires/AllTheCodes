import math
from typing import Match

#Constantes utilizadas
print("----------------------------")
print("Constante\tUnidade")
print("k = 9,0 * 10^9\t(N.m^2)/C^2")
print("============================")
print("Grandeza\tUnidade")
print("Força elétrica\tN")
print("Carga elétrica\tC")
print("Unidade métrica\tm")
print("----------------------------")

#Valores das constantes
k= 9 * 10**9

#Valores para a questão
unidadeCarga= input("Insira a unidade da carga (C, mC, uC, nC, pC)>> ")

a= float(input("Insira o valor da carga 1 >> "))
b= float(input("Insira o valor da carga 2 >> "))
c= float(input("Insira o valor da carga 3 >> "))

r21= float(input("Insira a distância entre a partícula 2 e 1 >> "))
r31= float(input("Insira a distância entre a partícula 3 e 1 >> "))

an= float(input("Insira o ângulo entre r21 e r31 >>"))

#Ajuste de carga
arrayUnidadeCarga= ['C','mC','uC','nC','pC']
arrayMultiplicadorCarga= [1, 0.001, 0.000001, 0.000000001, 0.000000000001]

verificacaoIns= arrayUnidadeCarga.index(unidadeCarga)

a= a* arrayMultiplicadorCarga[verificacaoIns]
b= b* arrayMultiplicadorCarga[verificacaoIns]
c= c* arrayMultiplicadorCarga[verificacaoIns]

#Checar módulo/sentido
aSentido= 0
bSentido= 0
cSentido= 0

if a < 0:
    moduloa= -1*a
    aSentido= "negativo"
else:
    moduloa= a

if b < 0:
    modulob= -1*b
    bSentido= "negativo"
else:
    modulob= b

if c < 0:
    moduloc= -1*c
    cSentido= "negativo"
else:
    moduloc= c
    
#Lógica para sentidos das forças
if aSentido == bSentido:
    direcao21= "Se repelem"
else:
    direcao21= "Se atraem"

if aSentido == cSentido:
    direcao31= "Se repelem"
else:
    direcao31= "Se atraem"

#Cálculo das forças em r1  
#Trataremos individualmente cada Força, afim de trabalharmos com apenas uma dimensão por vez
moduloF21= (k * moduloa * modulob)/(r21)**2
forca21=[moduloF21,direcao21]

moduloF31= (k * moduloa * moduloc)/(r31)**2
forca31=[moduloF31,direcao31]

print("----------------------------")
print("Forca21:",forca21[0], "N.", forca21[1],"!!")
print("Forca31:",forca31[0], "N.", forca31[1],"!!")

#Lógica para o ângulo resultante
if forca21[1] == "Se atraem":
    if forca31[1] == "Se atraem":
        an= an
    else:
        an= 180 - an

else:
    if forca31[1] == "Se repelem":
        an= 180 - an
    else:
        an= an

cosseno= math.cos(math.radians(an))