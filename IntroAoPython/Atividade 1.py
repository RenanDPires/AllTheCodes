# Respostas da primeira lista, favor tirar o "#" para poder executar cada comando.

# Q1
# print("Obrigado pelo curso!! Foi show.")

# Q2
# Permite a inserção de dados assim que executada a linha.


# Q3
# a) x=13 / inteiro 
#print(type(13))

# b) x='olá' / string (sequência de caracteres)
#print(type('olá'))

# c) x='True' / string (sequência de caracteres)
#print(type('True'))

# d) x='13.689' / string (sequência de caracteres)
#print(type('13.689'))

# e) x=14.9023 / float (número decimal)
#print(type(14.9023))

# f) x=False / bool (variável booleana, verdadeiro e falso - True e False)
#print(type(False))

# g) x=input() / função de inserção de dados
#print(type(input()))

# h) x=bool(input()) / função que converte o dado inserido para booleano
#print(type(bool(input())))

# i) x=int(14.80+30.50) / valor inteiro, já que int irá converter de float para int
#x=int(14.80+30.50)
#print(type(x))

# j) x=[1,2,'3334',4,True] / list, estrutura que armazena outros tipos de dados
#print(type([1,2,'3334',4,True]))


#Q4 Uso float por ser algo mais amplo para a realidade.
#X=float(input("Primeiro número: ")) # defino o tipo de valor inserido
#Y=float(input("Segundo número: ")) # defino o tipo de valor inserido
#soma=X+Y # executo a operação soma para os valores pós definição de tipo
#subtração=X-Y # executo a operação subtração para os valores pós definição de tipo
#multiplicação=X*Y # executo a operação multiplicação para os valores pós definição de tipo
#divisão=X/Y # executo a operação divisão para os valores pós definição de tipo
#print("A soma é",soma)
#print("A subtração é",subtração)
#print("A multiplicação é",multiplicação)
#print("A divisão é",divisão)

#Q5
# if é o comando "se". Ou seja, determina uma condição para que seus subordinados sejam executados
# elif é o comando "se" utilizado em série. Ou seja, caso a condição do if não seja atendida, os comandos elif's susequentes serão verificados em ordem.
# else é o comando "caso contrário". Ou seja, determina o que será feito se o comando if não for atendido.

#Q6
#a=int(input("Insira a nota do aluno(valor inteiro): "))
#if(a>9):
#    print('Excelente!! Você foi aprovado')
#elif(a>=7):
#    print('Aprovado')
#else:
#    print('Infelizmente você foi reprovado :/')

#Q7
#a=int(input("Insira seu número(valor inteiro):"))
#y=a*6.5
#print('Seu valor é:',y,'.')
#print('E ele está na faixa abaixo:')
#if(y>=100 and y<=150):
#    print('FAIXA 1')
#elif(y>=200 or y<=50) and (y<=-50 or y>=300):
#    print('FAIXA 2 e FAIXA 3')
#elif(y>=200 or y<=50):
#    print('FAIXA 2')
#elif(y<=-50 or y>=300): #"menor que 0" e "menor que -50" pode ser reduzido a "menor que -50, haja visto que todo número negativo é menor que 0"
#    print('FAIXA 3')

#Q8
#try e except são utilizados para. Caso observado um erro dentro do "try", o programa não seja encerrado e sim tentado de outra forma já definida no "except", não funcionado o programa é encerrado.

#Q9 Uso float por ser algo mais amplo para a realidade.
#try:
#    a=float(input("Insira a nota da primeira avaliação: "))
#    b=float(input("Insira a nota da segunda avaliação: "))
#    c=float(input("Insira a nota da terceira avaliação: "))
#except:
#    print("Insira as notas novamente")
#    a=float(input("Insira a nota da primeira avaliação: "))
#    b=float(input("Insira a nota da segunda avaliação: "))
#    c=float(input("Insira a nota da terceira avaliação: "))  
#
#média_ponderada=((a*2)+(b*3)+(c*5))//10.0
#if (média_ponderada>=6):
#    print('Parabéns, sua nota é',média_ponderada,'e voce foi aprovado!!!' )
#else:
#    print('Sua nota é', média_ponderada, 'e voce não foi aprovado.')

#Q10 Uso float por ser algo mais amplo para a realidade.
#try:
#    Operador=str(input("Escolha a operação a ser realizada informando o símbolo operador (+, -, *, /): "))
#    a=float(input("Insira seu primeiro número: "))
#    b=float(input("Insira seu segundo número: "))
#except:
#    print('Favor reinserir os dados...')
#    Operador=str(input("Escolha a operação a ser realizada informando o símbolo operador (+, -, *, /): "))
#    a=float(input("Insira seu primeiro número: "))
#    b=float(input("Insira seu segundo número: "))
#s=a+b
#u=a-b
#m=a*b
#d=a/b
#if(Operador=="+"):
#    print('Voce escolheu a soma')
#    print('Resultado:',s)
#elif(Operador=="-"):
#    print('Voce escolheu a subtração')
#    print('Resultado:',su)
#elif(Operador=="*"):
#    print('Voce escolheu o produto')
#    print('Resultado:',m)
#elif(Operador=="/"):
#    print('Voce escolheu a divisão')
#    print('Resultado:',d)
#else:
#    print('Reinicie o programa e insira a opreção corretamente.') #Não conseguir fazer um limitador de escolhas para as operações, então deixei esse aviso no fim.