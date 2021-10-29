#Testes para Sabium
#Q2
#Uma matriz quadrada inteira é um “quadrado mágico” se a soma dos elementos de cada linha, 
# a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.
#Por exemplo, a matriz abaixo é um quadrado mágico:
#Código em Python

n= int(input("Insira o tamanho da sua matriz quadrada >> "))

matriz= []

for i in range(n):
    linha = []
    for x in range(n):
        linha.append(int(input()))
    matriz.append(linha)


# Teste das linhas
valoresLinhas= [] #vetor para guardar os valores das somas de linhas
for i in range(n):
    valoresLinhas.append(sum(matriz[i]))

for i in range(len(valoresLinhas)):
    l= i-1
    if (valoresLinhas[l] == valoresLinhas[i]):
        testeLinhas = "ok"
        somaLinha= valoresLinhas[i]
    else:
        testeLinhas = "nOk"
        somaLinha= 0
        break


# Teste das colunas
valoresColunas= []
for j in range(n):
    colunas=[]
    for i in range(n):
       colunas.append(matriz[i][j])

    valoresColunas.append(sum(colunas))

for i in range(len(valoresColunas)):
    l= i-1
    if (valoresColunas[l] == valoresColunas[i]):
        testeColunas = "ok"
        somaColuna= valoresColunas[i]
    else:
        testeColunas = "nOk"
        somaColuna= 0
        break


# Teste da diagonal
valoresDiagonal= []
for i in range(n):
    for j in range(n):
        if i == j:
            valoresDiagonal.append(matriz[i][j])

somaDiagonal= sum(valoresDiagonal)



# Acima fiz testes nas linhas e nas colunas
# Agora faremos os testes finais (com o valor da soma da diagonal)

if (testeLinhas == "ok") & (testeColunas == "ok"):
    if somaLinha == somaColuna == somaDiagonal:
        print("quadrado mágico")
    else:
        print("quadrado não mágico")
else:
    print("quadrado não mágico")
