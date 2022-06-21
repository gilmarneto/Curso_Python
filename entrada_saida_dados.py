#data: 26/05/2022

# variável
nome = "Gilmar Neto"
media = 9.1

# para saída de dados usamos o (print)
# exemplos:

#01 > imprimindo texto todo junto
print("Olá, Gilmar!")

#02 > imprimindo valores separados
print("Gilmar","Neto")

#03 > imprimindo com valor de uma variável
print("Olá,", nome)

#04 > imprimindo com valor de uma variável, utilizando marcador
print("Olá, %s" %nome) # aqui estamos dizendo que %s é uma String, e %nome, estamos informando o valor da nossa variável nome

#05 > imprimindo com valor de uma variável, utilizando mais de um marcador, em forma de lista
print("Meu nome é %s, tenho %d anos e minha média escolar é de %f." %(nome, 38, media))

#06 > imprimindo com valor de uma variável, utilizando mais de um marcador e tratamento de casas decimais
print("Meu nome é %s, tenho %d anos e minha média escolar é de %.1f." %(nome, 38, media)) # com apenas uma casa decimal, após o ponto

