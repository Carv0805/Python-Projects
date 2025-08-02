'''
Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. 
Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:

Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

Se número de páginas for menor que 20 retornar o número de página sem desconto;
Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira:

total = (servico * num_pagina) + extra
'''

def escolha_servico():#Função para relacionar a escolha de um serviço pelo usuario
    acumulador_servico = 0 #acumulador para receber os valores de cada tipo de serviço selecionado pelo usuario
    while True:
        print("\nEntre com o tipo de serviço desejado:")
        print("DIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia")
        try:
            servico = input(">>")
            if (servico != "DIG" and servico != "dig" and servico != "ICO" and servico != "ico" and servico != "IPB" and servico != "ipb" and servico != "FOT" and servico != "fot"):
                print("Escolha inválida, entre com o tipo de serviço novamente.\n")
            elif(servico == "DIG" or servico == "dig"): #Condicional para validar as duas maneiras diferentes que o usuario pode querer chamar o serviço
                acumulador_servico = 1.10
                return acumulador_servico # retornar falor a função 
                break 
            elif(servico == "ICO" or servico == "ico"):
                acumulador_servico = 1.00
                return acumulador_servico
                break
            elif(servico == "IPB" or servico == "ipb"):
                acumulador_servico = 0.40
                return acumulador_servico
                break
            else:
                acumulador_servico = 0.20
                return acumulador_servico
                break
        except ValueError: # Usei os parametros try e except para dar suporte excluisvamente para  caso de um ValueError, como por exemplos letras (strings)
            print("Escolha inválida, entre com o tipo de serviço novamente.\n")
            
        
def num_pagina(): #Função para relacionar a escolha do número de paginas pelo usuario
    while True:    
        acumulador_pag = 0 #acumulador para receber os valores do números de páginas escolhidas pelo usuario
        try:
            num_pag = int(input("Entre com o número de páginas: "))
            if(1 <= num_pag < 20): #Condicional para validação de um número coesso de páginas, pois só possivel que ele escolhaum valor apartir de 1
                acumulador_pag  = num_pag
                return int(acumulador_pag)
                break
            elif(20 <= num_pag < 200):
                acumulador_pag = num_pag*0.85
                return int(acumulador_pag)
                break
            elif(200 <= num_pag < 2000):
                acumulador_pag = num_pag*0.8
                return int(acumulador_pag)
                break
            elif(2000 <= num_pag < 20000):
                acumulador_pag = num_pag*0.75
                return int(acumulador_pag)
                break
            elif(num_pag > 20000):
                print("Não aceitamos tantas páginas de uma vez.\nPor favor, entre em com o número de páginas novamente.\n")
                continue
            else: #Condicional para caso usuario insira valores como 0 ou números negativos
                print("Escolha inválida, entre com o número de paginas novamente.\n")
                continue
        except ValueError: #
            print("Escolha inválida, entre com o número de paginas novamente.\n")
            
        
def servico_extra(): #Função para relacionar a escolha de serviço extra pelo usuario
    print()
    acumulador_adc = 0 #Acumulador para receber os valores dos serviços extras escolhidos pelo usuario
    while True:
        print("Deseja adicionar algum serviço?")
        print("1 - Encardenação Simples - R$ 15.00\n2 - Encadernação Capa Dura - R$ 40.00\n0 - Não desejo mais nada")
        try:
            adicional = int(input(">>"))
            if(adicional != 1 and adicional != 2 and adicional != 0):
                print("Escolha inválida, entre com o tipo de serviço novamente\n")
            elif(adicional == 1):
                acumulador_adc += 15.00
                return acumulador_adc
            elif(adicional == 2):
                acumulador_adc += 40.00
                return acumulador_adc
            elif(adicional == 0):
                return acumulador_adc
                break
            else: 
                print("Escolha inválida, entre com o tipo de serviço adicional novamente\n")
        except ValueError:
            print("Escolha inválida, entre com o tipo de serviço adicional novamente\n")
            
#Programa Princial
print("Bem vindo a Copiadora do Vitor Carvalho")
valor_servico = escolha_servico() # Chama a função e recebe o valor do escopo local que ela retornar para poder ser usado no escopo global e mostrar o resultado final para o usuario logo abaixo 
valor_pagina = num_pagina()
valor_extra = servico_extra()
total = (valor_servico*valor_pagina)+valor_extra
print(f"Total: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {valor_pagina} + extra: {valor_extra:.2f})")





