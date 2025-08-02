'''
Ex 2:
    Escreva um programa que pergunte a quantidade de km percorridos por um carro
    alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
    foi alugado. 
    Calcule o preço a pagar, saberndo que o carro custa R$60 por dia e R$0,15
    por km rodado
'''
km=int(input("Digite a quantidade de km percorrido pelo carro: "))
dias=int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco = (km*0.15)+(dias*60)
print(f"Km = {km}.") 
print(f"Dias: {dias}.")
print(f"Valor a ser pago: {preco}R$")