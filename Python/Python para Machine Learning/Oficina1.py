
# Dados a serem usados:
notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

# Classificação de músicas
ruins= [0,1]
medianas= [2,3]
boas= [4,5]

# Auxiliadores

contadorRockRuim= []
contadorRockMediano= []
contadorRockBom= []

contadorRock=[[],[],[]] # Ruins, medianas e boas

contadorPopRuim= []
contadorPopMediano= []
contadorPopBom= []

contadorPop=[[],[],[]] # Ruins, medianas e boas


def classificadorRock():
    for i in range(len(notas_rock)):
        if notas_rock[i] in ruins:
            contadorRockRuim.append(notas_rock[i])
        elif notas_rock[i] in medianas:
            contadorRockMediano.append(notas_rock[i])
        elif notas_rock[i] in boas:
            contadorRockBom.append(notas_rock[i])
    contadorRock[0].append(len(contadorRockRuim))
    contadorRock[1].append(len(contadorRockMediano))
    contadorRock[2].append(len(contadorRockBom))

def classificadorPop():
    for i in range(len(notas_pop)):
        if notas_pop[i] in ruins:
            contadorPopRuim.append(notas_pop[i])
        elif notas_pop[i] in medianas:
            contadorPopMediano.append(notas_pop[i])
        elif notas_pop[i] in boas:
            contadorPopBom.append(notas_pop[i])
    contadorPop[0].append(len(contadorPopRuim))
    contadorPop[1].append(len(contadorPopMediano))
    contadorPop[2].append(len(contadorPopBom))

classificadorRock()
classificadorPop()

# Músicas medianas de rock
def verificaMedianasRock():
    if contadorRock[1][0] > 0:
        print("Há", contadorRock[1][0], "músicas medianas de Rock!", "Taxa de", (contadorRock[1][0]/len(notas_rock))*100, "%")
    else:
        print("Não há música mediana em Rock!")

# Músicas boas de Pop
def verificaBoasPop():
    if contadorPop[2][0] < len(notas_pop):
        print("Infelizmente nem todas as músicas Pop são boas!", "Taxa de", (contadorPop[1][0]/len(notas_pop))*100, "%")
    else:
        print("Sim, todas as músicas Pop são boas")

# Qual teve mais músicas boas?
def sinalizaMelhorEstilo():
    if contadorRock[2][0] > contadorPop[2][0]:
        print("O gênero Rock conta com", contadorRock[2][0] - contadorPop[2][0], "músicas boas a mais que o Pop." )
    elif contadorPop[2][0] > contadorRock[2][0]:
        print("O gênero Pop conta com", contadorPop[2][0] - contadorRock[2][0], "músicas boas a mais que o Rock." )
    else:
        print("Os gêneros têm as mesmas quantidades de músicas boas.")

def saidaTabela():
    print("=================================")
    print("|Classificação","\t|Rock","\t|Pop\t|")
    print("---------------------------------")
    print("|Boas", "\t\t|",contadorRock[2][0], "\t|",contadorPop[2][0], "\t|")
    print("|Medianas", "\t|",contadorRock[1][0], "\t|",contadorPop[1][0], "\t|")
    print("|Ruins", "\t\t|",contadorRock[0][0], "\t|",contadorPop[0][0], "\t|")
    print("---------------------------------")
    print("|Total", "\t\t|",len(notas_rock), "\t|",len(notas_pop), "\t|")
    print("=================================")

# Saída Geral
saidaTabela()
verificaMedianasRock()
verificaBoasPop()
sinalizaMelhorEstilo()

