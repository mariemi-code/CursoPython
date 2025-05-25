"""
#esta es una versión
edad=-7

if 0<edad<100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

#esta línea debe aparecer debajo
"""

salario_presidente=int(input("Salario presidente: "))
print("Salario del presidente es "+str(salario_presidente))

salario_director=int(input("Salario director: "))
print("Salario del director es "+str(salario_director))

salario_jefe=int(input("Salario jefe: "))
print("Salario del jefe es "+str(salario_jefe))

salario_asistente=int(input("Salario asistente: "))
print("Salario del asistente es "+str(salario_asistente))

if salario_asistente<salario_jefe<salario_director<salario_presidente:
    print("Todo OK")
else:
    print("Algo huele mal aquí")

