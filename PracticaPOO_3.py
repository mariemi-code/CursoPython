class Coche():

    def __init__(self,lc, ac, r, em):
        self.__largoChasis=lc
        self.__anchoChasis=ac
        self.__ruedas=r
        self.__enmarcha=em

    def arranca(self,arrancamos):
        self.__enmarcha=arrancamos

        if self.__enmarcha:
            chequeo=self.__chequeo_inicial()

        if self.__enmarcha and chequeo:
            return "Coche en marcha"
        elif self.__enmarcha and not chequeo:
            return "Problemas en el chequeo, no se ha podido poner en marcha el coche."
        else:
            return "Coche detenido"


    def estado(self):
        print("Largo del coche: ",self.__largoChasis)
        print("Ancho del coche: ",self.__anchoChasis)        
        print("El coche tiene ", self.__ruedas, " ruedas.")

    def __chequeo_inicial(self):
        print("Realizando chequeo inicial")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False
        


miCoche=Coche(250,120,4,False)

print(miCoche.arranca(True))
miCoche.estado()

print("---segunda instancia---")

tuCoche=Coche(350,200,4,False)

print(tuCoche.arranca(False))
tuCoche.estado()