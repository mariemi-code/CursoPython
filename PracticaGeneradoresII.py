"""
#con dos for anidados
def devuelve_cuidades(*ciudades):
    for elem in ciudades:
        for subelem in elem:
            yield subelem
"""

#con yield from
def devuelve_cuidades(*ciudades):
    for elem in ciudades:
        yield from elem
cuidades_devueltas=devuelve_cuidades("Madrid", "Barcelona", "Pamplona", "Valencia")

print(next(cuidades_devueltas))
print(next(cuidades_devueltas))

