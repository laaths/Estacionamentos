#
#https://www.w3schools.com/python/python_classes.asp
#

class estacionar:
    def __init__(self,placa,box,h_entrada,h_saida):
        self.placa = placa
        self.box = box
        self.h_entrada = h_entrada
        self.h_saida = h_saida
#SET VALORES
    def setPlaca(self,placa):
        self.placa = placa

    def setBox(self,box):
        self.box = box

    def setH_entrada(self,h_entrada):
        self.h_entrada = h_entrada

    def setH_saida(self,h_saida):
        self.h_saida = h_saida
#GET VALORES
    def getPlaca(self):
        return self.placa

    def getBox(self):
        return self.box

    def getH_entrada(self):
        return self.h_entrada

    def getH_saida(self):
        return self.h_saida
#MOSTRAR DADOS
    def mostraDados(self):
        print(" Placa    : ", self.placa,"\n","Box      : ", self.box,"\n","H Entrada: ", self.h_entrada,"\n","H Saida  : ", self.h_saida)

    def mostraDados2(self):
        if int(self.box) <= 9:
            print(self.placa,"", self.box,"   ", self.h_entrada,"  ", self.h_saida)
        else:
            print(self.placa,"", self.box,"  ", self.h_entrada,"  ", self.h_saida)
