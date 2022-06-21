# data: 06/06/2022

# Tuplas | São como listas, porém não são mutáveis. São representadas por parênteses
# Quando usamos Tuplas? | R: Geralmente quando estamos trabalhando com funções e precisamos retornar vários valores. Valores que não poderão ser alterados

#ex001 - Exemplo de Tupla com parênteses
tupla01 = (1, 3.1, 'Gilmar', False) # também podemos usar todos os tipos de valores
print(tupla01)

#ex002 - Exemplo de Tupla sem parênteses
tupla02 = 1, 3.2, 'Neto', True
print(tupla02) # porém ao exibir, será representado por parênteses
# vamos ver o tipo
print(type(tupla02))