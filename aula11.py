class Transporte:

    def __init__(self, nome, tipo):
        self.nome=nome
        self.tipo=tipo


# Pode -se definir de duas formas destintas
class Toyota(Transporte):

    def __init__(self, nome, tipo):
        #Transporte.__init__(self, nome, tipo)
        super().__init__(nome, tipo)

t1=Toyota("Galucho","Motorizado")

print(t1.nome)
