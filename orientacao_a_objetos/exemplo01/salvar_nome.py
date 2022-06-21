# data: 21/06/2022
# autor: GilmarNeto

# importar classe Pessoa
from pessoas import Pessoa # pessoas(nome_do_arquivo(módulo)) | Pessoa(nome_da_classe)

p = Pessoa() 
p.nome = "Gilmar Neto"
p.idade = 38

p.salvar_nome()