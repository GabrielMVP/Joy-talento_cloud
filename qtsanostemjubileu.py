from datetime import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido. Deve estar entre 1922 e 2021.")
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

nome = input("Digite o nome completo: ")
ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"Nome: {nome}")
print(f"Idade em 2023: {idade} anos")
