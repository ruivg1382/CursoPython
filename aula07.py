class Pessoa:
    def __init__(self, nome,idade):
        self.nome=nome
        self.idade=idade
    
    def Trabalhar(self):
        print("Ela está trabalhando")
    
    def Jogar(self):
        if 10>20:
            print("Fez um Jogaço")
        else:
            print("Perna de Pau")

p=Pessoa("Carmen",27)

print(p.nome)
print(p.idade)

p.Trabalhar()
p.Jogar()