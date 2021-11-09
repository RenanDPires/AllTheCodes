import random
import collections

# NÃO CONSEGUI USAR O ALGORÍTMO ZEROR, LOGO, BOLEI DOIS MÉTODOS DE AUXILIAR A MÁQUINA A GANHAR DO USUÁRIO MAIS VEZES.
# SE O USUÁRIO SOUBER O SCRIPT DO JOGO, ELE PODE "ENGANAR" A MÁQUINA


# Etapa 1 (criar a lógica do jogo)

# Entrada inicial e auxiliadores
entrada= []
entrada.append(int(input("Escolha sua opção (1,2,3,4):\n1- Pedra\n2- Papel\n3-Tesoura\n4- Sair\n")))
textoJogadas= ["Pedra", "Papel", "Tesoura"]
possiveisJogadas= [1,2,3]
listaDeRespostasGanhadoras= []


# Lógica para etapa 1 (com menos de 4 preenchimentos do jogador)
while (entrada[-1] != 4) and (int(len(entrada)) <= 5):
    jogadasMaquinaAleatorio= int(random.choice(possiveisJogadas))
    if entrada[-1] == jogadasMaquinaAleatorio:
        print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
        print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
        print(f"EMPATE!!")
    else:
        if entrada[-1] == 1:
            if jogadasMaquinaAleatorio == 2:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!") 
        elif entrada[-1] == 2:
            if jogadasMaquinaAleatorio == 3:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!")
        elif entrada[-1] == 3:
            if jogadasMaquinaAleatorio == 1:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!")
    entrada.append(int(input("\nEscolha sua opção (1,2,3,4):\n1- Pedra\n2- Papel\n3-Tesoura\n4- Sair\n")))
    print((collections.Counter(entrada)).most_common())

print((collections.Counter(entrada)).most_common(1))



# Etapa 2 Auxiliar a máquina a ter jogadas asertivas

while (entrada[-1] != 4):
# Não consegui utilizar o algoritmo ZeroR, então proponho a solução 1: a máquina joga para ganhar da jogada que o usuário mais fez
    if (collections.Counter(entrada)).most_common(1)[0][0] == 1:
        jogadasMaquinaAleatorio= 2
    elif (collections.Counter(entrada)).most_common(1)[0][0] == 2:
        jogadasMaquinaAleatorio= 3
    else:
        jogadasMaquinaAleatorio= 1

    print(jogadasMaquinaAleatorio)
    if entrada[-1] == jogadasMaquinaAleatorio:
        print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
        print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
        print(f"EMPATE!!")
    else:
        if entrada[-1] == 1:
            if jogadasMaquinaAleatorio == 2:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!") 
        elif entrada[-1] == 2:
            if jogadasMaquinaAleatorio == 3:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!")
        elif entrada[-1] == 3:
            if jogadasMaquinaAleatorio == 1:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!")
    entrada.append(int(input("\nEscolha sua opção (1,2,3,4):\n1- Pedra\n2- Papel\n3-Tesoura\n4- Sair\n")))


while (entrada[-1] != 4):
# Não consegui utilizar o algoritmo ZeroR, então proponho a solução 2: a máquina tem mais chances de escolher um valor que ganhe do usuário 
# (Ela trabalha criando uma lista das respostas que ganhem do usuário e dará uma resposta aleatória com base nesta lista)
    if entrada[-1] == 1:
        listaDeRespostasGanhadoras.append(2)
    elif entrada[-1] == 2:
        listaDeRespostasGanhadoras.append(3)
    elif entrada[-1] == 3:
        listaDeRespostasGanhadoras.append(1)

    jogadasMaquinaAleatorio= random.choice(listaDeRespostasGanhadoras)

    if entrada[-1] == jogadasMaquinaAleatorio:
        print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
        print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
        print(f"EMPATE!!")
    else:
        if entrada[-1] == 1:
            if jogadasMaquinaAleatorio == 2:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!") 
        elif entrada[-1] == 2:
            if jogadasMaquinaAleatorio == 3:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!")
        elif entrada[-1] == 3:
            if jogadasMaquinaAleatorio == 1:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ PERDEU!!")
            else:
                print(f"Sua jogada => {textoJogadas[(entrada[-1]-1)]}")
                print(f"A Jogada da máquina foi => {textoJogadas[(jogadasMaquinaAleatorio-1)]}")
                print(f"VOCÊ GANHOU!!")
    entrada.append(int(input("\nEscolha sua opção (1,2,3,4):\n1- Pedra\n2- Papel\n3-Tesoura\n4- Sair\n")))


print("Obrigado por jogar! ")
