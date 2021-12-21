# Auxiliador
serie= 0

#Entrada
n= int(input('Insira o n da série -> '))

# Lógica do somatório
for x in range(n+1):
    r= 1/3
    
    serie= (serie + (1/3)**x)
    print(serie)

print(f'O somatório do valor da série é {round(serie-1,2)}')