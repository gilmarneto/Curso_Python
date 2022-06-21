# data: 31/05/2022
# import modulo (random)
import random
from secrets import choice
import string
# vamos ver o módulo (random) e algumas funções
print(dir(random))

# exemplo-001 | (randint)
x = random.randint(1,50)
print(x)

# exemplo-002 | (choice)
# ver ajuda
help(choice)
lista = ['gol','astra','fusca','palio','uno']
print(random.choice(lista)) # podemos usar para fazer sorteio de nomes

# exemplo-003 | (shuffle)
help(random.shuffle)
random.shuffle(lista)
print(lista)
