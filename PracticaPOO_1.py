class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arranca(self):
        self.enmarcha=True

    def detener(self):
        self.enmarcha=False

    def estado(self):
        if self.enmarcha:
            return "Coche en marcha"
        else:
            return "Coche detenido"

miCoche=Coche()

print("Largo del coche: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas.")
miCoche.arranca()
print(miCoche.estado())

print("---segunda instancia---")

tuCoche=Coche()

print("Largo del coche: ",tuCoche.largoChasis)
print("El coche tiene ",tuCoche.ruedas, " ruedas.")
print(tuCoche.estado())
