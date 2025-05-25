"""
#generando números pares con una función
def generaPares(limite):
    num=1
    miLista=[]
    while num<=limite:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))
"""

#generando números pares con un generador
def generaPares(limite):
    num=1
    while num<=limite:
        yield num*2
        num=num+1

paresDevueltos=generaPares(10)

#for i in paresDevueltos: #casi lo mismo que lo obtenido con la función
#    print(i)

print(next(paresDevueltos))

print("Más líneas de código...")

print(next(paresDevueltos))

print("Más líneas de código...")

print(next(paresDevueltos))