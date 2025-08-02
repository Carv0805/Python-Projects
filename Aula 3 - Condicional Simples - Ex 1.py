'''
Desenvolva um programa que leia dois valores núméricos inteiros e compare se o primeiro 
é maior do que o segundo. Caso seja verdadeiro o resultado, ele imprime na tela 
a mensagem informando que o primeiro valor digitado é maior que o segundo.
'''
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))

if(num_1>num_2):
    print(f"O primeiro número {num_1} é maior que o segundo valor {num_2}")
elif(num_1==num_2):
    print(f"O primeiro e o segundo número são iguais")
else:
    print(f"O segundo número {num_2} é maior que o primeiro valor {num_1}")