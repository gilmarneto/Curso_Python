# data: 31/05/2022
import string

# agora vamos ver algumas funções de String
print(dir(string))

# ex_001 | capwords 
nome = "gilmar florencio neto"
formatado = string.capwords(nome, sep=" ") # após cada espaço entre um inicio e outro,a primeira letra será maiúscula
print(formatado)

# ex_002 | digits
help(string.digits)
print(string.digits)

# ex_003 | hexgigits
help(string.hexdigits)
print(string.hexdigits)

# ex_004 | octdigits
help(string.octdigits)
print(string.octdigits)

# ex_005 | punctuation
help(string.punctuation)
print(string.punctuation)