class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, 
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
        

class Moto(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.hcaballito=""

    def caballito(self):
        self.hcaballito="Voy haciendo caballito"

    def estado(self):
        super().estado()
        print(self.hcaballito)


class Furgoneta(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.cargado=False

    def carga(self, cargar):
        self.cargado=cargar

        if (self.cargado):
            print("Furgoneta cargada")
        else:
            print("Furgoneta vacía")


class VElectricos():

    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True
    
class BiciElectrica(Vehiculo, VElectricos):   
    pass

miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Citroen", "Berlingo")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)

mibiciElect=BiciElectrica("Orbea", "EseMismo")
mibiciElect.estado()
