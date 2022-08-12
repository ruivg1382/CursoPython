class Carro:

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
    
    def verificar(self, ano):
        self.ano=ano
        if(self.ano > 2021):
            print("carro Recente - E novinho em Folha")
        else:
            print("Carro Antigo - Precisa ser atualizado")


Car=Carro("Toyota", "Dyna150")

x=Car.verificar(2022)

print(x)
print(Car.marca)
print(Car.modelo)