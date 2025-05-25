"""
for letra in "Python":
    if letra=="h" or letra=="H":
        continue
    print(f"Letra: {letra}")
"""

cadena="Quiero contar las letras"
print(f"longitud de cadena {len(cadena)} caracteres")
cant=0

for i in cadena:
    if i== " ":
        continue
    cant=cant+1

print(f"Cantidad de letras:{cant}")
