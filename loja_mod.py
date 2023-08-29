#controle de estoque
#produtos disponíveis lista
#codigo que leia os produtos que tenham em lista e me diga as quantidades que temos para venda.
#substituir produtos após acabar estoque
#--------------------------------------#
#Sistema que mostra lista de produtos
#possibilidade de alterar um produto por outro
#possibilidade de adicionar mais produtos

#lista de produtos da loja:
lista_de_produtos = ['Camisa Polo', 'Bermuda', 'Short', 'Camisa Manga Longa']

#Adicionando as funções para o menu
def verificar_produtos():
    print('Os produtos disponíveis para venda são: ')
#codigo para exibir função de ver produtos a seguir:
    for produto in lista_de_produtos:
        print(produto)
        
#----Peças do estoque e quantidades----#

estoque = {
    'Camisa Polo': 15,
    'Bermuda': 15,
    'Short': 5,
    'Camisa Manga Longa': 5
}
#----Função verificar a quantidade de itens do estoque----#

def verificar_estoque():
    print('verificar quantidade de itens: ')
    
#codigo para exibir função de ver produtos a seguir:

    for peça, quantidade in estoque.items():
        print(f'{peça}: {quantidade} unidades')
        
#----Função substituir um produto da lista----#
def substituir_produtos():
    print('Qual produto você quer substituir: ')
    # solicitando ao operador para digitar qual o produto que ele quer substituir por um novo.
    produto_antigo = input('Digite o nome do produto que você deseja substituir:')
#codigo para exibir função de ver produtos a seguir:

    if produto_antigo in lista_de_produtos:
        index = lista_de_produtos.index(produto_antigo) #Index verifica sé nesse indice do lista de produtos
        produto_novo = input('Qual o nome do novo produto a ser substituido: ')
        lista_de_produtos[index] = produto_novo
        print(f'O produto {produto_antigo} foi substituido por {produto_novo}')
    else:
        print('Produto não encontrado!')

#----Função adicionar um produto na lista----#
def adicionar_produto():
    print('Qual produto você quer adicionar: ')
#codigo para exibir função de ver produtos a seguir:
    novo_produto = input('Qual o produto que você deseja adicionar: ') #Adicionando a função para chamar o novo produto
    if novo_produto not in lista_de_produtos:
        lista_de_produtos.append(novo_produto)
        print(f'O produto {novo_produto} foi adicionado à loja!')
    else:
        print('Produto já adicionado!')

def menu_acesso():
    print('Menu de acesso:')
    print('1. Verificar produtos disponíveis na loja: ')
    print('2. Verificar lista de itens no estoque: ')
    print('3. Substituir produtos: ')
    print('4. Adicionar produto a loja: ')
    print('5. Sair')
    
while True:
    menu_acesso()
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        verificar_produtos()
    elif opcao == 2:
        verificar_estoque()
    elif opcao == 3:
        substituir_produtos()
    elif opcao == 4:
        adicionar_produto()
    elif opcao == 5:
        break
    else:
        print('Opção inválida!')