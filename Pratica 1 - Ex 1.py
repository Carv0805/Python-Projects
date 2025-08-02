'''
Ex 1:
    Desenvolva um algoritmo que solicite ao usuario o preço de um produto e 
    um percentual de desconto a ser aplicado a ele.
    Calcule e exiba o valor do desconto e o preço final do produto.
'''
preco = float(input("Digite o preço do produto: "))
percentual = float(input("Digite a percentual de desconto (0-100%): "))

desconto = preco*(percentual*0.01)
preco_final= preco - desconto
print(f'O preço do produto é {preco}. O desconto é de {percentual}%')
print(f'Valor calculado de desconto: {desconto}. Valor final do produto: {preco_final}')
