"""
edad=int(input("Introduce tu edad: "))

while edad<5 or edad>100:
    print("Edad incorrecta")
    edad=int(input("Introduce tu edad: "))       

print(f"Edad del aspirante {edad}")    
"""
import math

print("Calculando raíz cuadrada")

intentos=0
num=int(input("Teclee el número: "))

while num<0 and intentos<3:
    intentos=intentos+1
    print("Imposible calcular la raíz a números negativos")
    if intentos==3:
        print("Agotados los posibles intentos")
    else:
        num=int(input("Teclee el número: "))

if intentos<3:
    raiz=math.sqrt(num)
    print(f"La raíz cuadrada de {num} es {raiz}")

