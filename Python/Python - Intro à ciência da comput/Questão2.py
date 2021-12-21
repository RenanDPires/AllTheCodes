# Auxiliador
continuar= 'Sim'

# Função de fatorial e saída
def fatorial(numero):
    fatorial= 1
    atual= numero
    for x in range(1,numero+1):
        fatorial= fatorial * atual
        atual= x
    print(f'Fatorial de {numero} = {fatorial}')
    
# Parâmetros de entrada
while continuar == 'Sim':
    numero= int(input('Digite um valor inteiro para o calculo do Fatorial ? -> '))
    if numero > 0:
        fatorial(numero)
    else: 
        print('Digite um valor inteiro para o calculo do Fatorial -> ')
        break
    continuar= input('Deseja continuar (Sim/Não)? ->')
    print('====================================')