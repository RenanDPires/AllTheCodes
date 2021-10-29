#Testes para Sabium
#Q2
#Escreva um programa que leia todos os caracteres de um arquivo texto e imprima em ordem crescente as percentagens das ocorrências das letras encontradas. Os caracteres que não são letras devem ser ignorados.
#Exemplo de texto contido em arquivo txt
#"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
#Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing."
#Resultado
#Total de letras: 283
#Percentuais:
#"a" = 9,54%
#"b" = 1,06%
#"c" = 4,24%
#...
#"z" = 0,00%

#Código em Python

f= open('arquivo.txt')

print(f.read())