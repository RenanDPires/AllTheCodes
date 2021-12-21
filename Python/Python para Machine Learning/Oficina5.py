import numpy as np
import numpy.ma as ma

# Etapa 1

# Entradas
visualizacao_stories = [
    [187, 120, 88, 70, 130, 168, 213],
    [0, 0, 42, 0, 0, 55, 77],
    [91, 0, 61, 0, 71, 121, 271],
    [0, 0, 0, 0, 187, 0, 0],
    [42, 23, 34, 0, 39, 29, 36]
]
pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

# Tranformar um array para np.array (só testanto mesmo)
visualizacao_stories= np.array(visualizacao_stories)

# Médias por dia (todos os usuários)
def mediaVisualizacoes (visualizacao_stories,dias_semana):
    vetorMedia= visualizacao_stories.mean(axis=0)
    for i in range(len(dias_semana)):
        print(f"Em {dias_semana[i]} a média de visualizações é {vetorMedia[i]}.")

# Soma de acessos por dia da semana
def diaComMaisVisualizacoes(visualizacao_stories,dias_semana):
    somaPorDia=[]
    somaPorDia.append(np.sum(visualizacao_stories, axis=0))
    somaPorDia=np.array(somaPorDia) # É desnecessário, se ajustar os metodos, mas fiz pra ficar mais facil depois
    print(f"\nO dia com mais visualizações foi {dias_semana[somaPorDia.argmax()]} com {somaPorDia.max()}.")

# Define quem gerou mais acessos (aqui não transformei o array para np.array, logo tive que usar: np."metodo"(array))
def usuarioComMaisVisualizacoes(visualizacao_stories,pessoas):
    somaPessoas=[]
    for i in range(len(pessoas)):
        somaPessoas.append(visualizacao_stories[i].sum()) 
    print(f"\nA pessoa com mais visualizações foi {pessoas[np.argmax(somaPessoas)]} com {np.max(somaPessoas)}.\n")

# Saídas para a semana 1

print("Dados da semana 1 >> \n")
# Retorna as médias diárias
mediaVisualizacoes(visualizacao_stories,dias_semana)

# Retorna o dia com mais visualizações e o valor
diaComMaisVisualizacoes(visualizacao_stories,dias_semana)

# Retorna quem mais teve visualizações na semana
usuarioComMaisVisualizacoes(visualizacao_stories,pessoas)

#===============================================================

# Etapa 2

# Array da nova semana
visualizacao_stories_invalidos = np.array([
    [52, 68, 97, 55, -1, 98, -1],
    [53, -1, 38, -1, -1, 72, 49],
    [88, -1, 64, -1, 77, 130, 43],
    [-1, 30, -1, -1, -1, 182, -1],
    [41, 20, 33, -1, 37, 23, 7]
])

# Criando array mascarado
array_mascarado = np.ma.masked_where(visualizacao_stories_invalidos == -1, visualizacao_stories_invalidos)


# Saídas para a semana 2
print("================================================================================")
print("================================================================================")
print("\nDados da semana 2 >> \n")
# Retorna as médias diárias
mediaVisualizacoes(array_mascarado,dias_semana)

# Retorna o dia com mais visualizações e o valor
diaComMaisVisualizacoes(array_mascarado,dias_semana)

# Retorna quem mais teve visualizações na semana
usuarioComMaisVisualizacoes(array_mascarado,pessoas)