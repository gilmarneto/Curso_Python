# data: 21/06/2022
# autor: GilmarNeto

# vamos declarar a classe Carro
class Carro(object): # object->definimos como classe pai
    # vamos declarar o nosso método construtor
    def __init__(self, caminho) :
        self.caminho = caminho

    # vamos declarar o método andar    
    def andar(self) :         
        print(f"Estou caminhando pela {self.caminho}")


class Fusca(Carro) : # Estamos dizendo que a classe filha(Fusca) vai herdar da classe pai(Carro)
    # vamos declarar nosso método construtor
    def __init__(self, caminho):
        self.caminho = caminho

    def correr(self) :
        self.caminho = "avenida" 
        super(Fusca, self).andar()