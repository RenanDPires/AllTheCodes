# Respostas da segunda lista, favor tirar o "#" para poder executar cada comando.

# Q1
#x=0
#while(x==0): #fiz só pra gerar um mini loop e testar o laço "while"
#    try:
#        a=input("Insira seu primeiro valor: ")
#        b=input("Insira seu segundo valor: ")
#        A=float(a)
#        B=float(b)
#        soma=A+B
#        print("Seu resultado é: ",soma)
#    except:
#        print('Insira apenas numerais')
#        a=input("Insira seu primeiro valor: ")
#        b=input("Insira seu segundo valor: ")
#        A=float(a)
#        B=float(b)
#        soma=A+B
#        print("Seu resultado é: ",soma)

#Q2 Não entendi muito bem a questão, mas fiz meu melhor
#x=1
#m=x*15
#print(x,'*', '15','=', m)
#while(x<15):
#    x=x+1
#    m=x*15
#    print(x,'*', '15','=', m)

#Q3 fiz um programa um pouco diferente do pedido, mas que funciona com mais opções. Basicamente ele te diz o valor do "enésimo" termo que você quiser
#n = int(input("O termo que deseja encontrar: "))
#m=7
#valor=((n-1)*2)+7
#if(n==1):
#    print('O valor do',n,'° termo','é:', m)
#elif (n<=1):
#    print('Favor inserir valores maiores ou iguais a um')
#else:
#    print('O valor do',n,'° termo','é:', valor)

#Q4 Defini a função "nome" que define dois parametros de entrada. A primeira entrada será definida como menssagem personalizada, baseada no "input()"
#def nome (a,b):
#	c = a + b
#	return c
#n=input("Favor, insira seu nome de usuário: ")
#if(n=="Ana"):
#    p = nome ("Bem vinda, ",n)
#    print(p)
#elif(n=="Beto"):
#    p = nome ("Bem vindo, ",n)
#    print(p)
#elif(n=="Carlos"):
#    p = nome ("Bem vindo, ",n)
#    print(p)
#else:
#    print('Favor solicite seu cadastro.')

#Q5 Que questão difícil...nossaaaaa
#def arranjo_simples (h,i):
#    b=1
#    a=1
#    while(a<=h):
#        b=b*a
#        a=a+1
#    j=h-i
#    c=1
#    d=1
#    while(d<=j):
#        c=c*d
#        d=d+1
#    f=b//c
#    return f

#x=int(input("Inserir primeiro número: "))
#y=int(input("Inserir segundo número: "))


#p= arranjo_simples(x,y)
#print('O valor do arranjo de',x,'em',y,'é',p)

#Q6 Acho que é assim
#while True:
#    b = int ( input ("Digite o primeiro número: ") )
#    c = int ( input ("Digite o segundo número: ") )
#    a=b+c
#    print('O resultado da soma é:',a)

#Q7
#n = int(input("Que termo deseja encontrar: "))
#ultimo=1
#penultimo=1

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
#    print(termo)

#Q8
#n = int(input("Que termo deseja encontrar: "))
#ultimo=1
#penultimo=1

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
#    print(termo)

#Q10
#while True:
#    operacao = str(input("Digite a operacao desejada (soma, sub, mult, div): "))
#    try:
#        numero1 = input("Digite o primeiro número: ")
#        numero2 = input("Digite o segundo número: ")
#        if operacao == "soma":
#	        resultado = int(numero1) + int(numero2)
#        elif operacao == "sub":
#	        resultado = int(numero1) - int(numero2)
#        elif operacao == "mult":
#	        resultado = int(numero1) * int(numero2)
#        elif operacao == "div":
#	        resultado = int(numero1) / int(numero2)
#        else:
#	        resultado = "Operação não suportada"
#        print("O resultado da operação é: " + str(resultado))
#    except:
#        print('Insira os valores corretamente!!')
#        numero1 = input("Digite o primeiro número: ")
#        numero2 = input("Digite o segundo número: ")
#        if operacao == "soma":
#	        resultado = int(numero1) + int(numero2)
#        elif operacao == "sub":
#	        resultado = int(numero1) - int(numero2)
#        elif operacao == "mult":
#	        resultado = int(numero1) * int(numero2)
#        elif operacao == "div":
#	        resultado = int(numero1) / int(numero2)
#        else:
#	        resultado = "Operação não suportada"
#        print("O resultado da operação é: " + str(resultado))