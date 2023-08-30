# Estamos modernizando  nossa loja e precisamos de um novo sistema de controle de estoque.

# ----> 1. CRIAR UM MENU PARA ACESSAR O SISTEMA DA LOJA <-----#

#Geralmente anotamos todos os produtos que temos disponíveis, e quando um dos produtos acaba,
#substituimos ele por algum outro produto.
#Ouvi dizer que vocês podem fazer um sistema para a gente que mostra a lista com todos nossos
#produtos, e nos deixa alterar um produto por outro.

# ----> ADICIONAR A FUNÇÃO PARA SUBSTITUIR UM PRODUTO POR OUTRO DE ESCOLHA <----#

# ---->  CRIAR UM ARRAY MOSTRANDO LISTA DOS ITENS QUE TEM NA LOJA DO CLIENTE. <-----#

#Além disso, estamos pensando em ampliar nosso armazém, para ter mais espaço para mais produtos.
#Então, se puderem fazer com que o sistema nos permita adicionar mais produtos à lista, e
#qualquer outra coisa que acharem necessário, seria muito bom.

# ----> CRIAR  UMA FUNÇÃO PARA ADICIONAR MAIS PRODUTOS A ARRAY <-----#
# ----> SISTEMA PARA ADICIONAR PRODUTOS A LOJA <----#


# ----> LISTA DE PRODUTOS BASE PARA A LOJA A ARRAY <----#
lista_de_produtos = ['Camisa Polo', 'Bermuda', 'Short', 'Camisa Manga Longa']

# ----> FUNÇÃO DO MENU PARA VERIFICAR OS PRODUTOS QUE TEM NA ARRAY <----#
def verificar_produtos():
    print('Os produtos disponíveis para venda são: ')
# AÇÃO NECESSÁRIA PARA QUE O VERIFICAR_PRODUTOS POSSA PUXAR DA ARRAY A LISTA DE ITENS
# ELE PROCURA OS PPRODUTOS QUE TEM DENTRO DA ARRAY E MOSTRA AO FUNCIONARIO QUE ACESSA A OPÇÃO
    for produto in lista_de_produtos:
        print(produto)
        
# UM ESTOQUE PARA QUE NA OPÇÃO VERIFICAR A QUANTIDADE DE PRODUTOS QUE TEM NO SISTEMA.

estoque = {
    'Camisa Polo': 15,
    'Bermuda': 15,
    'Short': 5,
    'Camisa Manga Longa': 5
}

# A FUNÇÃO PARA PUXAR  DO ESTOQUE QUE VERIFICA OS ITENS E SUAS QUANTIDADES

def verificar_estoque():
    print('verificar quantidade de itens: ')
    
# O CODIGO INFORMA QUE PARA PEÇA, QUANTIDADE NO ESTOQUE. FUNÇÃO ITEMS()
# PRINTAR A PEÇA DO ESTOQUE E A QUANTIDADE QUE TEM SALVA NA FUNÇÃO ESTOQUE{}

    for peça, quantidade in estoque.items():
        print(f'{peça}: {quantidade} unidades')
        
# A FUNÇÃO PARA SUBSTITUIR UM PRODUTO DO ESTOQUE POR OUTRO
def substituir_produtos():
    print('Qual produto você quer substituir: ')
    # AQUI CHAMO DE PRODUTO ANTIGO O DA LISTA E SOLICITO AO OPERADOR QUE DIGITE O NOME DO PRODUTO QUE DESEJA SUBSTITUIR
    produto_antigo = input('Digite o nome do produto que você deseja substituir:')
# NO CODIGO ABAIXO EXECUTA A SUBSTITUIÇÃO DO PRODUTO SELECIONADO POR UM NOVO
# PRECISEI PESQUISAR UM POUCO PARA CONSEGUIR FAZER FUNCIONAR ESTÁ OPÇÃO.
# ELE PROCURA NA BASE DOS DADOS, NA LISTA DE PRODUTOS O PRODUTO ANTIGO COM O NOEM SELECIONADO
# APÓS ENCONTRAR SOLICITA AO OPERADOR QUE DIGITE O NOME DO NOVO PRODUTO
# ASSIM ANEXANDO A LISTA DE PRODUTOS O NOVO PRODUTO MAS DE FORMA TEMPORARIA
# CASO O PRODUTO ANTIGO NÃO EXISTA ELE JÁ EXECUTA O SEGUNDO CODIGO COM A MENSAGEM.

    if produto_antigo in lista_de_produtos:
        index = lista_de_produtos.index(produto_antigo) #Index PARA VERIFICAR O PRODUTO QUE ESTÁ ANEXADO A ARRAY
        produto_novo = input('Qual o nome do novo produto a ser substituido: ')
        lista_de_produtos[index] = produto_novo
        print(f'O produto {produto_antigo} foi substituido por {produto_novo}')
    else:
        print('Produto não encontrado!')
        

# A FUNÇÃO PARA ADICIONAR PRODUTOS A LISTA TAMBÉM DE FORMA TEMPORARIA
def adicionar_produto():
    print('Qual produto você quer adicionar: ')
    
# AQUI SOLICITO AO OPERADOR PARA QUE DIGITE O NOME DO NOVO PRODUTO.
#  AQUI PROCURA SE O PRODUTO ESCOLHIDO JÁ EXISTE NA ARRAY CASO NÃO EXISTA ELE O ADICIONA EM SEGUIDA MOSTRA A MENSAGEM
# CASO ELE EXISTA PULA A PRIMEIRA EXECUÇÃO E MOSTRA QUE JÁ EXISTE UM PRODUTO COM ESTE NOME NA LISTA
    novo_produto = input('Qual o produto que você deseja adicionar: ') 
    if novo_produto not in lista_de_produtos:
        lista_de_produtos.append(novo_produto)
        print(f'O produto {novo_produto} foi adicionado à loja!')
    else:
        print('Produto já adicionado!')

# CRIAÇÃO DE UM MENU DE ACESSO COM OPÇÕES
def menu_acesso():
    print('Menu de acesso:')
    print('1. Verificar produtos disponíveis na loja: ')
    print('2. Verificar lista de itens no estoque: ')
    print('3. Substituir produtos: ')
    print('4. Adicionar produto a loja: ')
    print('5. Sair')
  
# NESSE CRIEI UM LOOP PARA QUE SE ESCOLHA UMA OPÇÃO E QUE CASO NÃO SEJÁ ESCOLHIDO NENHUM DESSES NUMEROS ELE MOSTRE QUE A OPÇÃO É INVÁLIDA.
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
