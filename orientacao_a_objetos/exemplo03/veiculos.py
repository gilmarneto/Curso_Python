# data: 21/06/2022
# autor: GilmarNeto

# declarando classe Montadora
class Veiculo(object) :
    # declarando método construtor
    def __init__(self, veiculo) :
        self.veiculo = veiculo
    # declarando método Moto
    def fMoto(self) :
        print(f"Eu tenho um(a) {self.veiculo}")
        print(f"O veiculo {self.veiculo} cabe em uma garagem residencial.")
    
class Carro(Veiculo) :
    def __init__(self, veiculo) :
        self.veiculo = veiculo

    def fCarro(self) :
        self.veiculo = "Carro"
        super(Carro, self).fMoto()
        
# Aqui entra o Polimorfismo, onde posso subscrever o método da classe pai dentro da classe filho
class Caminhao(Veiculo) :
    def __init__(self, veiculo):
        self.veiculo = veiculo

    def fMoto(self) :
        print(f"O veiculo {self.veiculo} não cabe em uma garagem residencial.");