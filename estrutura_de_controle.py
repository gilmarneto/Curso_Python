# data: 26/05/2022

# declarando variáveis
nota = 7
media = 7

# Estrutura de Controle

# Condições
# if(se)
if nota >= media :
    print("Aprovado")

# if(se) | else(senão)
if nota >= media :
    print("Aprovado")
else :
    print("Reprovado")

# if(se) | elif(senão se) | else(senão)
if nota > media :
    print("Aprovado")

elif (nota == media) :
    print("Recuperação")

else :
    print("Reprovado")


#Repetição
# for
for x in range(11):
    print(x) # neste caso será impresso o número de 0 a 10, pois estamos iniciando do 0

# while
# vamos declarar duas variáveis para este exemplo
x = 1
y = 10

while (x <= y) :
    print(x)
    x = x + 1
print("Fim de While...")
