class Trabalhador:
    salario_Base=0
    tempo_trabalho=0
    nome=""
    telefone=""

    def __init__(self,nome, salario_Base):
        self.nome=nome
        self.salario_Base=salario_Base
    

class Professor(Trabalhador):
    pass


class Pedreiro(Trabalhador):
    pass

class Jardineiro(Trabalhador):
    pass


p1=Professor("Rui Gonçalves", 54)


print(p1.nome)
print(float(p1.salario_Base))