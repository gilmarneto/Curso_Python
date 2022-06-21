# data: 03/06/2022

# declarando variável
nome01 = "gilmar;florencio;neto"
nome02 = "Gilmar Florencio Neto"

# exemplo_001 | replace(substituir)
nome01 = nome01.replace(";"," ")
print(nome01)

# exemplo_002 | split(dividir)
print(type(nome02.split()))
print(nome02.split()) # neste caso a String nome02 será divida, e colocado em formato de lista

# exemplo_003 | join(juntar)
data = ['03','06','2022'] # temo a nossa data em formato de lista
print(type(data))
print(data) # irá exibir a data formato de lista
# agora colocar a data separado por (/)
print(type("/".join(data)))
print("/".join(data))