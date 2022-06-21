# data: 21/06/2022
# autor: GilmarNeto

# Declarando a classe Pessoa
class Pessoa(object):
    nome = None
    idade = None

    # Declarando Método
    def salvar_nome(self):
        print(f"Meu nome é: {self.nome} e tenho {self.idade} anos de idade.")