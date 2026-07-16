class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O carro {self.modelo} acelerou para {self.velocidade} km/h.')

# Criar o objeto Carro
carroInstrutor = Carro("Fusca", "Amarelo")
carroEric = Carro("Jetta", "Preto")
carroJuliana = Carro("Agile", "Preto")

carroJuliana.acelerar(50)