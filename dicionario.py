# data: 06/06/2022

# Dicionário em Python, temos chave e valor(key, value).

#ex001 - exemplo básico
d = {}
print(type(d))
d['nome']  = "Gilmar"
d['sobrenome'] = "Neto"
d['idade'] = 38
print(d)

#ex002 - remover valor por chave
d.pop('idade') # neste caso estarei removendo o valor da chave idade 
print(d)

#ex003 - removendo valor da última chave
d.popitem()
print(d)

#ex004 - exibir apenas as chaves
d1 = {}
d1['nome'] = "Jumas"
d1['sobrenome'] = "Neto"
d1['idade'] = 38
d1['altura'] = 1.86
print(d1.keys())

#ex005 - exibir apenas os valores
print(d1.values())

#ex006 - exibir apenas item
print(d1.items())



