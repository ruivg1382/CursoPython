class Aluno:

    idade=0

    def __init__(self,nome,morada, idade):
        self.nome=nome
        self.morada=morada
        self.idade=idade
    
    def verificarIdade(self):
        if(self.idade<18):
            print("menor de idade")
        else:
            print("Maior de idade")



a1=Aluno("Marina","Praia",12)


print(a1.nome)
print(a1.morada)
print(a1.idade)
print(a1.verificarIdade())