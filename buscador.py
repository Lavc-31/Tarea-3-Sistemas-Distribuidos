import fileinput

pagina = None
max = 0
lista = []
print("Ingrese la palabra que desea buscar:")
palabra = input()

for line in fileinput.input(files = ("output.txt")):
    linea = line.split()
    if (linea[0] == palabra):
        lista.append(list(linea[1]))
        lista.append(list(linea[2]))       
        lista.append(list(linea[3]))
        lista.append(list(linea[4]))
        lista.append(list(linea[5]))
        lista.append(list(linea[6]))
        lista.append(list(linea[7]))
        lista.append(list(linea[8]))
        lista.append(list(linea[9]))
        lista.append(list(linea[10]))

contador = 1
for i in lista:
    if contador != 10:
        if(int(i[3]) >= max ):
            max = int(i[3])
            pagina = int(i[1])
    else:
        if(int(i[4]) >= max ):
            max = int(i[4])
            pagina = 10
    contador += 1

print("--------\n")

if(pagina == 1):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Pokémon")

if(pagina == 2):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Methamidophos")

if(pagina == 3):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Dinosaur")

if(pagina == 4):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Chess")

if(pagina == 5):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Twitter")

if(pagina == 6):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Isle_of_Skye")

if(pagina == 7):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/YouTube")

if(pagina == 8):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Face_book")

if(pagina == 9):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Economy")

if(pagina == 10):
    print("La pagina que contiene mas veces la palabra buscada es:")
    print("https://en.wikipedia.org/wiki/Politics")