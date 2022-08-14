class Hotel:
    total=0

    def __init__(self, nome, numero_quarto, localizacao):
        self.numero_quarto=numero_quarto
        self.nome=nome
        self.localizacao=localizacao

    
    

class Hotel1(Hotel):
    pass


h1=Hotel1("riba de água",120,"Calheta")

print(h1.nome)
