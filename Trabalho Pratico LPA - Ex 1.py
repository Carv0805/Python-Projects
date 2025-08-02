'''
Imagina-se que você é um dos programadores responsáveis pela construção de um 
app de vendas para uma determinada empresa X que vende em atacado. 

Uma das estratégias de vendas dessa empresa X é dar desconto maior 
conforme o valor da compra, conforme a listagem abaixo:

    Se valor for menor que 2500 o desconto será de 0%;
    Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
    Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;   
    Se valor for igual ou maior que 10000 o desconto será de 11%;
'''
print("Bem-vindo a Loja do Vitor Carvalho")
valor_unitario = float(input("Entre com o valor do produto: ")) #Atribuição de valor pelo usuario para ponto flutueante pois o valor pode ser um valor decimal
quantidade = int(input("Entre com a quantidade do produto: ")) #Atribuição de valor pelo usuario para inteiro pois este não pode ser um valor decimal

valor_total_sem_desconto = valor_unitario * quantidade
print(f"O valor SEM desconto: R${valor_total_sem_desconto}")

if (valor_total_sem_desconto <= 2500):
    valor_total_com_desconto = valor_total_sem_desconto #Caso em que a o valor não possui desconto, logo seu valor com desconto é o mesmo que o valor sem desconto
    print(f"O valor COM desconto: R${valor_total_com_desconto}")
    
elif (valor_total_sem_desconto >= 2500) and (valor_total_sem_desconto < 6000):
    valor_total_com_desconto = (valor_total_sem_desconto * 0.96) #Multiplica o valor sem desconto por 0.96 é o mesmo que fazer (valor_total_sem_desconto*0.04) - valor_total_sem_desconto 
    print(f"O valor COM desconto: R${valor_total_com_desconto}")

elif (valor_total_sem_desconto >= 6000) and (valor_total_sem_desconto < 10000):
    valor_total_com_desconto = (valor_total_sem_desconto * 0.93) #Multiplica o valor sem desconto por 0.93 é o mesmo que fazer (valor_total_sem_desconto*0.07) - valor_total_sem_desconto
    print(f"O valor COM desconto: R${valor_total_com_desconto}")

else: #Este "else" significa que como o valor sem desconto nao foi nenhuma das opções acima logo ele sera sempre o valor maior que 10000 
    valor_total_com_desconto = (valor_total_sem_desconto * 0.89) #Multiplica o valor sem desconto por 0.89 é o mesmo que fazer (valor_total_sem_desconto*0.11) - valor_total_sem_desconto
    print(f"O valor COM desconto: R${valor_total_com_desconto}")