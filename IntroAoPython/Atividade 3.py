# Respostas da segunda lista, favor tirar o "#" para poder executar cada comando.

# Q1
#x = [1,3,5,6,7,2,2,8,9,1,6,3,9,2,4,8,9,0,2,1,8,3,8,9,4,2,9,6]
#x.sort()
#print("Lista 'x', mas com elementos em ordem:",x)
#nova_lista=[] #lista onde ficarão os números repetidos em ordem
#nova_x=[] #lista onde ficarão os números sem repetição
#n=0
#while n<len(x):
#    if(n!=0) and (x[n]==x[(n-1)]):
#        nova_lista.append(x[n])
#    elif n==0 or x.count(x[n])!=1:
#        nova_x.append(x[n])
#    n=n+1

#print("Elementos repetidos da lista 'x':",nova_lista)
#print("Elementos repetidos da lista 'x':",nova_x)

#Q2
#z = [-500,7232,43405,-1,55,-55,805,765]
#n=0 #posição do meu item na lista
#s=0 #o valor da soma a ser usado no 'while', inicia zerado por 0 ser elemento neutro da adição/subtração

#while n<8:
#    if z[n]<0:
#        s=s+z[n]*-1
#    else:
#        s=s+z[n]
#    n=n+1

#print('A soma absoluta é:',s)

#Q3
#z = [-500,7232,43405,-1,55,-55,805,765]
#n=0 #posição do item na lista
#s=0 #o valor da soma a ser usado no 'while', inicia zerado por 0 ser elemento neutro da adição/subtração
#m=1 #o valor da multiplicação a ser usado no 'while', inicia com 1 por ele ser elemento neutro da multiplicação/divisão

#while n<8:
#    if z[n]<0:
#        s=s+z[n]*-1
#    else:
#        s=s+z[n]
#    m=m*z[n]
#    n=n+1
#d=m/s #resultado final com divisão real
#print('A soma absoluta é:',s)
#print('O resultado da divisão é:',d)

#Q4
#lista=[] #lista a ser preenchida com os valores inseridos pelo usuário
#b=input("Deseja inserir algum valor? (S/N)") #inseri aqui o primeiro input ja pra usar ele como condição do while

#while b=="S" or b=="s":
#    a=input("Insira seus valores, um a um.") #enquanto eu responder 's' ou 'S', irei adicionar valores à minha lista
#    b=input("Deseja inserir outro valor? (S/N)")
#    lista.append(a)
#lista.sort()
#print("Sua lista é:",lista)

#Q5
#n = int(input("O termo que deseja encontrar: "))
#ultimo=1
#penultimo=1
#fibonacci=[]

#if(n==1)or(n==2):
#    print("1")
#elif(n==0):
#    print("0")
#else:
#    count=3
#    while count <= n:
#        termo = ultimo + penultimo
#        penultimo = ultimo
#        ultimo = termo
#        count += 1
#        fibonacci.sort()
#        if fibonacci.count(termo)==1:
#            print("Valor já buscado")
#        else:
#            fibonacci.append(termo)
#        print("Sua lista é:",fibonacci)

#Q6
#b=0 #teste de um jeito diferente de começar com o while já definido na variável que periódicamente inserirmos
#lista=[]
#while b=="0" or b=="s" or b=="S":
#    a=input("Insira seu valor")
#    lista.append(a)
#    b=input("Valores todos inseridos?(S/N)")

#lista.sort()
#c=len(lista)
#d=lista[0]
#e=lista[c]
#print(c,d,e)
