# Auxiliares
bonus= 0
maisProdutos= 's'
final= 0

# Calcular o preço final
while maisProdutos == 's':
    quantidade= int(input('Insira a quantidade de produtos -> '))
    preco= float(input('Agora insira o valor unitário -> '))
    final= final + (quantidade * preco)
    maisProdutos= input('Processar mais produtos? (s/n) -> ')


# Definir valor com desconto, bonus e vip
def processamento(final):
    mensagem= "Cliente ainda não pode ser VIP"
    if final < 100:
        desconto= 5
        comDesconto= final * (1 - (desconto/100))
    
    elif 100 <= final <= 1000:
        desconto= 8
        comDesconto= final * (1 - (desconto/100))
        bonus= 0.05 * comDesconto
    
    else:
        desconto= 10
        comDesconto= final * (1 - (desconto/100))
        bonus= 0.05 * comDesconto
        mensagem= 'O cliente será cadastrado como Cliente VIP.'
    
    print('\n=============================================')
    print(f'O valor final da compra é: R${comDesconto}.')
    print(f'Seu desconto é de: {desconto}%.')
    print(f'Cliente terá um bônus na próxima compra de: R${bonus}.')
    print(mensagem)



processamento(final)