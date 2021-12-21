# Aluno: Renan Duarte Pires
# Professor: Ivan Paulino Pereira
# Linguagem: Python 3.0


n = int(input("Por favor, insira um número (positivo e inteiro): "))

def primo(n):
    

    if n>0:
        for i in (2, n-1):
            if (n%i) == 0:
                x= 1
                break
            else:
                x= 0

        if x== 0:
            print("O número é primo.")
        else:
            print("O número não é primo.")

    else:
        n = int(input("Por favor, insira um número (positivo e inteiro): "))
        primo(n)
        

    

primo(n)