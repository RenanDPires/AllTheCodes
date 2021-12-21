# Aluno: Renan Duarte Pires
# Matrícula: 20103003
# Linguagem: Python 3.0


# ATIVIDADE 1

"""
# Problema 1

# Entradas e variáveis
peso= float(input("Insira seu peso em kG -> "))
altura= float(input("Insira sua altura em m -> "))

# Cálculo
imc= peso/(altura*altura)

# Classiicação
if imc <= 18.5:
    classificacaoIMC= "\nAbaixo do peso"

elif 18.6 < imc <= 24.9:
    classificacaoIMC= "\nSaudável"

elif 25.0 < imc <= 29.9:
    classificacaoIMC= "\nPeso em excesso"


elif 30.0 < imc <= 34.9:
    classificacaoIMC= "\nObesidade grau I"

elif 35.0 < imc <= 39.9:
    classificacaoIMC= "\nObesidade grau II (Severa)"

elif 40.0 <= imc:
    classificacaoIMC= "\nObesidade grau II (Mórbida)"

# Saída
print(f"Seu IMC é {imc} e sua classificação é: {classificacaoIMC}!")
"""

"""
# Problema 2
# Entradas e variáveis
ponto1= []
ponto1.append(float(input("Insira o valor de x para o ponto 1 -> ")))
ponto1.append(float(input("Insira o valor de y para o ponto 1 -> ")))

ponto2= []
ponto2.append(float(input("Insira o valor de x para o ponto 2 -> ")))
ponto2.append(float(input("Insira o valor de y para o ponto 2 -> ")))

ponto3= []
ponto3.append(float(input("Insira o valor de x para o ponto 3 -> ")))
ponto3.append(float(input("Insira o valor de y para o ponto 3 -> ")))

# Cálculo das arestas
lados= []
def lado (ponto1, ponto2):
    lados.append((((ponto1[0]-ponto2[0])**2) + ((ponto1[1]-ponto2[1])**2))**0.5)

lado(ponto1, ponto2)
  
lado(ponto1, ponto3)

lado(ponto2, ponto3)

# Classificação do tipo de triângulo e saída
if lados[0] == lados[1] == lados[2]:
    print("Este triângulo é equilátero!")

if lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
    print("Este triângulo é isósceles!")

if lados[0] != lados[1] and lados[1] != lados[2] and lados[0] != lados[2]:
    print("Este triângulo é escaleno!")
"""

"""
# Problema 3
# Entrada
numero= input("Insira seu número de 5 dígitos-> ")

# Verificação de palíndromo e saída
if numero[0] == numero[-1] and numero[1] == numero[-2]:
    print("Este número é um palíndromo!")
else:
    print("Este número não é um palíndromo!")
"""
