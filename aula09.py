from socket import NI_NUMERICHOST


class Aluno:

    def __init__(self, nome, numero, turma):
        self.nome=nome
        self.numero=numero
        self.turma=turma


a1=Aluno("Mariano", 17, "11ºES")

print(a1.nome)
print(a1.numero)
print(a1.turma)

""" 
Vou apagar o objeto Aluno
"""
del a1.nome

print(a1.nome)