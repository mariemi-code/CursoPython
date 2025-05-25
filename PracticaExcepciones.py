"""
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas")
        #se genera la excepción pero no la estamos gestionando con on bloque Try
    elif edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad <65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate"

print(evaluaEdad(-18))
"""

import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

oper=int(input("Teclee el número: "))

try:
    print(f"La raíz cuadrada es {calculaRaiz(oper)}")
except ValueError as MiErrorNumeroNeg:
    print(MiErrorNumeroNeg)
    
print("Programa terminado")
