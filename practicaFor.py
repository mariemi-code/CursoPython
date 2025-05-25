"""
email=False
for i in "mariemi.pacheco@gmail.com":
    print(i, end= " ")
    if (i == "@"):
        email=True

print("")
if email:
    print("Correcto")
else:
    print("incorrecto")
"""

valido=False
email=input("Introduce el email: ")
for i in range(len(email)):
    print(email[i], end= " ")
    if email[i] == "@":
        valido=True

print("")
if valido:
    print("Correcto")
else:
    print("incorrecto")