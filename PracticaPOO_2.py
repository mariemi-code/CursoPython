class Coche():

    def __init__(self,lc, ac, r, em):
        self.__largoChasis=lc
        self.__anchoChasis=ac
        self.__ruedas=r
        self.__enmarcha=em

    def arranca(self,arrancamos):
        self.__enmarcha=arrancamos
        if self.__enmarcha:
            return "Coche en marcha"
        else:
            return "Coche detenido"


    def estado(self):
        print("Largo del coche: ",self.__largoChasis)
        print("Ancho del coche: ",self.__anchoChasis)        
        print("El coche tiene ", self.__ruedas, " ruedas.")

miCoche=Coche(250,120,4,False)

print(miCoche.arranca(True))
miCoche.estado()

print("---segunda instancia---")

tuCoche=Coche(350,200,4,False)

print(tuCoche.arranca(False))
tuCoche.__ruedas=6  # no da error pero tampoco se ejecuta
tuCoche.estado()