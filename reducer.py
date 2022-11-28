import fileinput

f = open("output.txt", "w")

palabrasp1= {}
palabrasp2= {}
palabrasp3= {}
palabrasp4= {}
palabrasp5= {}
palabrasp6= {}
palabrasp7= {}
palabrasp8= {}
palabrasp9= {}
palabrasp10= {}


palabras_finales = []

for line in fileinput.input(files = ("pages-1/page1.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp1:
			palabrasp1[palabra] = 1
		else:
			palabrasp1[palabra] += 1

for line in fileinput.input(files = ("pages-1/page2.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp2:
			palabrasp2[palabra] = 1
		else:
			palabrasp2[palabra] += 1

for line in fileinput.input(files = ("pages-1/page3.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp3:
			palabrasp3[palabra] = 1
		else:
			palabrasp3[palabra] += 1

for line in fileinput.input(files = ("pages-1/page4.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp4:
			palabrasp4[palabra] = 1
		else:
			palabrasp4[palabra] += 1

for line in fileinput.input(files = ("pages-1/page5.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp5:
			palabrasp5[palabra] = 1
		else:
			palabrasp5[palabra] += 1

for line in fileinput.input(files = ("pages-2/page6.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp6:
			palabrasp6[palabra] = 1
		else:
			palabrasp6[palabra] += 1

for line in fileinput.input(files = ("pages-2/page7.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp7:
			palabrasp7[palabra] = 1
		else:
			palabrasp7[palabra] += 1

for line in fileinput.input(files = ("pages-2/page8.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp8:
			palabrasp8[palabra] = 1
		else:
			palabrasp8[palabra] += 1

for line in fileinput.input(files = ("pages-2/page9.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp9:
			palabrasp9[palabra] = 1
		else:
			palabrasp9[palabra] += 1

for line in fileinput.input(files = ("pages-2/page10.txt")):
	linea = line.split()
	for palabra in linea:
		if palabra not in palabrasp10:
			palabrasp10[palabra] = 1
		else:
			palabrasp10[palabra] += 1
	

for keys in palabrasp1.keys():
    palabras_finales.append(keys)

for keys in palabrasp2.keys():
    palabras_finales.append(keys)

for keys in palabrasp3.keys():
    palabras_finales.append(keys)

for keys in palabrasp4.keys():
    palabras_finales.append(keys)

for keys in palabrasp5.keys():
    palabras_finales.append(keys)

for keys in palabrasp6.keys():
    palabras_finales.append(keys)

for keys in palabrasp7.keys():
    palabras_finales.append(keys)

for keys in palabrasp8.keys():
    palabras_finales.append(keys)

for keys in palabrasp9.keys():
    palabras_finales.append(keys)

for keys in palabrasp10.keys():
    palabras_finales.append(keys)

palabras_totales = set(palabras_finales)

for i in palabras_totales:
    if i not in palabrasp1:
        palabrasp1[i] = 0
    if i not in palabrasp2:
        palabrasp2[i] = 0
    if i not in palabrasp3:
        palabrasp3[i] = 0
    if i not in palabrasp4:
        palabrasp4[i] = 0
    if i not in palabrasp5:
        palabrasp5[i] = 0
    if i not in palabrasp6:
        palabrasp6[i] = 0
    if i not in palabrasp7:
        palabrasp7[i] = 0
    if i not in palabrasp8:
        palabrasp8[i] = 0
    if i not in palabrasp9:
        palabrasp9[i] = 0
    if i not in palabrasp10:
        palabrasp10[i] = 0
    f.write(i+ "  (1,"+str(palabrasp1[i])+") (2,"+str(palabrasp2[i])+") (3,"+str(palabrasp3[i])+") (4,"+str(palabrasp4[i])+") (5,"+str(palabrasp5[i])+") (6,"+str(palabrasp6[i])+") (7,"+str(palabrasp7[i])+") (8,"+str(palabrasp8[i])+") (9,"+str(palabrasp9[i])+") (10,"+str(palabrasp10[i])+")\n")

f.close()