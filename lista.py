# data: 06/06/2022

# List(As Listas em Python, são permitidas todos os tipos de valores)
# tipo: (inteiro, flutuante, string e booleano)

# ex001 - Lista
# Lista em python usamos colchetes, e cada posição é definida por índices. Estes índices são iniciados por zero(0)
lista = [1, 3.1, 'Gilmar', True] 
print(lista[2])

#ex002 - Lista com laço de repetição FOR
for l in lista:
    print(l)

#003 - Podemos também selecionar uma determinada posição da lista e atribuir um valor a esta posição
lista[1] = 3.2 # posição (1)
print(lista)

#004 - Podemos adicionar um valor a nossa lista usando (.append('valor')). Este valor será adicionado a última posição da lista
lista.append('Novo Valor')
print(lista)

#005 - Para remover um valor da lista usamos(.pop()). Este valor será removido sempre da última posição
lista.pop()
print(lista)

#006 - Agora se quisermos remover informando o valor, usamos o (.remove())
lista.remove(3.2)
print(lista)

#007 - Para inserir valor em uma posição especifica, usamos o (.insert(posição, 'valor'))
lista.insert(0, 'Valor Insert')
print(lista)

#008 - Para colocar uma lista ao inverso, usamos (.lista.reverse())
lista.reverse()
print(lista)

#009 - Se quisermos colocar uma lista em ordem alfabética usamos (.sort())
# lista.sort()
# print(lista) # haverá um erro, pois neste caso não podemos ter tipos diferentes de valores, como string e int

# Maneira correta de utilizar o Sort
lista02 = ['Marcos','Laide','Zaza', 'Abreu', 'Elisa']
lista02.sort()
print(lista02)

# Maneira reversa
lista02.sort(reverse=True)
print(lista02)

