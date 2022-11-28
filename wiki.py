import wikipedia as wiki

p1 = wiki.page("Pokemon")
f1 = open("page1.txt", "w")
for line in p1.content:
	f1.write(line)
f1.close()

p2 = wiki.page("Methamidophos")
f2 = open("page2.txt", "w")
for line in p2.content:
	f2.write(line)
f2.close()

p3 = wiki.page("Dinosaur")
f3 = open("page3.txt", "w")
for line in p3.content:
	f3.write(line)
f3.close()

p4 = wiki.page("Chess")
f4 = open("page4.txt", "w")
for line in p4.content:
	f4.write(line)
f4.close()

p5 = wiki.page("Twitter")
f5 = open("page5.txt", "w")
for line in p5.content:
	f5.write(line)
f5.close()

p6 = wiki.page("Skype")
f6 = open("page6.txt", "w")
for line in p6.content:
	f6.write(line)
f6.close()

p7 = wiki.page("Youtube")
f7 = open("page7.txt", "w")
for line in p7.content:
	f7.write(line)
f7.close()

p8 = wiki.page("Facebook")
f8 = open("page8.txt", "w")
for line in p8.content:
	f8.write(line)
f8.close()

p9 = wiki.page("Economía")
f9 = open("page9.txt", "w")
for line in p9.content:
	f9.write(line)
f9.close()

p10 = wiki.page("Política")
f10 = open("page10.txt", "w")
for line in p10.content:
	f10.write(line)
f10.close()

print("fin del programa :)")