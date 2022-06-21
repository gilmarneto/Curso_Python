# data: 24/05/22
# variáveis em Python não precisamos colocar o tipo, é considerado tipagem dinâmica
# variáveis em Python não possuem limites de tamanho na memória

# variáveis
a = 6
b = 2
c = 2.5
d = 'Texto'
e = False

print(type(a)) # na impressão vamos ver que a variável (a) é do tipo (int)
print(type(c)) # na impressão vamos ver que a variável (c) é do tipo (float(flutuante))
print(type(d)) # na impressão vamos ver que a variável (d) é do tipo (str(String))
print(type(e)) # na impressão vamos ver que a variável (e) é do tipo (bool(booleano))

print(a + a)

# operadores aritméticos

# soma
print("soma: ", a + b)
# subtração
print("subtração: ", a - b)
# multiplicação
print("multiplicação: ", a * b)
# divisão
print("divisão: ", a / c)
# divisão de inteiros
print("divisão de inteiros: ", a // c) # no caso de divisão de inteiros, após o ponto as casas decimais são desconsideradas. Sendo o valor arredondado
# exponenciação
print("exponenciação: ", a ** 2) 
# módulo
print("módulo: ", 11 % 3) # no caso de módulo, teremos o resto da divisão

# Operadores relacionais
# < menor que | > maior que | == igual | <= menor igual | => maior igual | != diferente
print(a > 10) # false
print(a < 10) # true
print(a >= b) # true
print(b == c ) # false
print(e != True) # true

# Operadores lógicos
# and (e) | or (ou) | not (negação)

# vamos combinar operadores relacionais e lógicos abaixo

