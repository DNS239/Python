"""curso =   "PyThOn  "

print(curso.upper())

print(curso.lower())

print(curso.title())"""




"""curso = "    PyThOn"

print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())"""




"""
curso = "PyThOn"

print(curso.center(10, "#"))

print(".".join(curso))"""



nome = "     Dns  "

print(nome.strip() + ".")

print(nome.lstrip() + ".")

print(nome.rstrip() + ".")

texto = "  Ola, Mundo!   "

print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14, "$"))

for letra in menu:
    print(letra, end="-")

print()

print("-".join(menu))


