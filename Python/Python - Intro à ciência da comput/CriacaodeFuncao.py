# Aluno: Renan Duarte Pires
# Professor: Ivan Paulino Pereira
# Linguagem: Python 3.0

# Entrada
media= float(input("Insira a média do aluno: "))

def conceitoAluno (media):
    # Limites máximos dos conceitos
    d= 49 
    c= 69
    b= 89
    a= 100
   
   # Lógica para dar o conceito
    if media <= d:
        conceito= 'D'
        mensagem= "Você precisa melhorar muito, se dedique mais!"
    elif d < media <= c :
        conceito= 'C'
        mensagem= "Você precisa melhorar, se dedique mais!"
    elif c < media <= b :
        conceito= 'B'
        mensagem= "Você está muito bem. Parabéns!"
    elif b < media <= a :
        conceito= 'A'
        mensagem= "Você está no caminho da excelência. Parabéns!"

    # Saída
    print(f'O conceito do aluno é *{conceito}*.\n{mensagem}')

conceitoAluno (media)