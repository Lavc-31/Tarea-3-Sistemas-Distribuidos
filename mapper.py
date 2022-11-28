import fileinput

count = 0
for line in fileinput.input(files = ("pages-1/page1.txt","pages-1/page2.txt","pages-1/page3.txt","pages-1/page4.txt","pages-1/page5.txt","pages-2/page6.txt","pages-2/page7.txt","pages-2/page8.txt","pages-2/page9.txt","pages-2/page10.txt")):
    words = line.split()
    for word in words:
        print('{}\t{}'.format(word,1))
        count += 1
print ("palabras totales en 10 paginas: ", count)