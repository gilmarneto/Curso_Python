# data: 26/05/2022

# Funções em Python
#--------------------------------------------------------------------------------

# função sem parâmetro
from html.entities import name2codepoint


def func01() : # usamos o (def) para definir uma função, (func01) nome_da_função
    soma = 1 + 1
    print(soma)

# abaixo vamos chamar a nossa função, nome_da_função() // sem parâmetro
func01()

#--------------------------------------------------------------------------------

# função com parâmetro
def func02(n1, n2) :
    multiplicacao = n1 * n2
    print(multiplicacao)

# abaixo vamos chamar a nossa função, nome_da_função(parâmetro-1,parâmetro-2) // com parâmetro
func02(2, 5)

#--------------------------------------------------------------------------------

# função com parâmetro e retorno
def func03(n1, n2) :
    subtracao = n1 - n2
    return subtracao

# abaixo vamos chamar a nossa função, nome_da_função(parâmetro-1,parâmetro-2) // com parâmetro e retorno
print(func03(20,5))

#--------------------------------------------------------------------------------

# função com diversos parâmetros
def func04(**kwargs) : # **kwargs é o parâmetro, passado para forma de dicionário do python
    for key, value in kwargs.items() : # key(chave) | value(valor) | kwargs.items() = pegar items do dicionario
        print(f"{key}: {value}")
    
# abaixo vamos chamar a nossa função, nome_da_função(key(chave) = "value(valor)")
func04(nome="Gilmar", idade="38")

#--------------------------------------------------------------------------------




