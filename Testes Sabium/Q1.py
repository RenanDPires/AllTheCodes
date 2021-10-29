#Testes para Sabium
#Q1
#Escreva um programa que seja capaz de identificar se uma palavra é palíndromo ou não. 
# Uma palavra palíndromo é a palavra que é possível se ler da esquerda para a direita e da direita para esquerda e tem o mesmo significado. 
# Exemplo: ovo, reviver
#Código em Python

palavra = input("Insira sua palavra para teste >>> ")
invPalavra= palavra[::-1]

if palavra == invPalavra:
    print("A palavra inserida É palíndromo!!!")
    print("=======================")
    print("| Palavra","|","Teste\t|")
    print("-----------------------")
    print("| ", palavra, "\t|", invPalavra, "\t\t|")
    print("=======================")
    
else:
    print("A palavra inserida NÃO É palíndromo!!!")
    print("=======================")
    print("| Palavra","|","Teste\t|")
    print("-----------------------")
    print("| ", palavra, "|", invPalavra, "\t|")
    print("=======================")
