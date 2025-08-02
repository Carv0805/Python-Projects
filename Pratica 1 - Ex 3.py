'''
Ex 3:
    Crie uma variavel de string que receba uma frase qualquer.
    Crie uma segunda variavel, agora contendo a metade da string digitada.
    Imprima na tela somente os dois últimos caracteres da segunda variavel do
    tipo string
'''
frase = input("Digite uma frase: ")
tam = len(frase)
metade = frase[:int(tam/2)]
print(metade[-2:])