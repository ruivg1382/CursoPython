nome=input("Como te chamas?\n")
idade=int(input(print("Quanto anos tens?\n")))
morada=input(print("Onde Moras?\n"))

if(idade >=18):
    print("Estamos perante um cliente chamado"+nome+" que mora em "+morada+"e tem "+str(idade)+"anos")
else:
    print("Pedimos desculpas")