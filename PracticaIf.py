#ejemplo de sentencia if
print("Programa de Evaluación")

nota_alumno=input("Introduce la nota del alumno: ")

def Evalua(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion

print(Evalua(int(nota_alumno)))
#haciendo pruebas de varis ramas