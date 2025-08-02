'''
Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. 
Este software deve ter o seguinte menu e opções:
    1)Cadastrar Livro
    2)Consultar Livro
        1. Consultar Todos 
        2. Consultar por Id
        3. Consultar por Autor
        4. Retornar ao menu
    3)Remover Livro
    4)Encerrar Programa
'''
def cadastrar_livro(id):
    id = []
    print("-"*50)
    print("-"*15,"MENU CADASTRAR LIVRO","-"*16)
    id.append(input("Id do livro: "))
    id.append(input(("Por favor entre com o nome do livro: "))
    id.append(input(("Por favor entre com o autor do livro: "))
    id.append(input(("Por favor entre com a editora do livro: "))
    lista_livro (id[:])
    id.clear()
    
def consultar_livro():
    print("-"*50)
    print("-"*15,"MENU CONSULTAR LIVRO","-"*16)
    escolha=int(input("1 - Consultar Todos os Livros\n2 - Consultar por Id\n3 - Consultar por Livros(s) por autor\n4 - Retornar ao menu"))
    print(">>")
    """
    try:
        while (escolha != 4)
            if (escolha == 1):
                for ids in id
        
            elif(escolha == 2):
                consultar_livro()
    
            elif(escolha == 3):
                remover_livro()
            else:
                print("Opção Inválida")
                break
    except ValueError:
        print("Escolha inválida")
    """


def remover_livro():
    print("-"*50)
    print("-"*15,"MENU REMOVER LIVRO","-"*16)
    id_removido = int(input("Digite o id do livro a ser removido: "))
    del id[id_removido]
    print("Livro removido com sucesso")

#Programa Principal
lista_livro = []
id_global = 0 
print("Bem vindo a a Livraria do Vitor Carvalho")
print("-"*50)
print("-"*15," MENU PRINCIPAL ","-"*15)
print("Escolha a opção desejada:")   
print("1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair")
escolha = int(input(">>"))

while True:
    try:
        if (escolha == 1):
            cadastrar_livro(id)
        
        elif(escolha == 2):
            consultar_livro()
    
        elif(escolha == 3):
            remover_livro()
        
        elif(escolha == 4):
            break
        else:
            print("Opção inválida")
    except ValueError:
        print("Escolha inválida ")
