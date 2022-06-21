# data: 06/06/2022

# Set | Podemos adicionar valores no Set começando com ele zerado. Valores no Set não podem ser repetidos, e caso queira inserir um valor repetido não será apresentado nenhuma notificação.

#ex001 - exemplo básico 
s = set()
print(s)

#ex002 - adicionando valores
s.add('Gilmar')
s.add('Neto')
s.add(38)
print(type(s))
print(s)

#ex003 - removendo valor, apartir da primeira posição
s.pop()
print(s)

#ex004 - removendo valor específico
s.remove(38)
print(s)
