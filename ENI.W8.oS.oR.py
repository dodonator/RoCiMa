#coding: utf-8
# ENI.W8.oS.oR
# ENI: Enigma
# W5: acht Walzen
# oS: ohne Steckbrett
# oR: ohne Reflektor

def walzeDrehen(walze):
	tmp = walze[1:len(walze)]
	tmp.append(walze[0])
	walze = tmp
	return walze
	

w0 = [3,8,5,1,7,2,6,4]
w1 = [8,1,7,3,6,5,2,4]
w2 = [4,2,6,7,3,8,5,1]
w3 = [2,8,6,1,3,7,4,5]
w4 = [7,3,1,4,6,8,2,5]
w5 = [1,2,3,4,5,6,7,8]
w6 = [8,7,6,5,4,3,2,1]
w7 = [1,2,3,8,7,6,4,5]

klartext = '163826572354263245232547467567583562462523451'
klartextListe = list(klartext)
geheimtext = ''

counterW0 = 0
counterW1 = 0
counterW2 = 0
counterW3 = 0
counterW4 = 0
counterW5 = 0
counterW6 = 0
counterW7 = 0

for i in xrange(len(klartext)):
	if counterW0 > 8:
		w1 = walzeDrehen(w1)
		counterW1 += 1
		counterW0 = 0
	if counterW1 > 8:
		w2 = walzeDrehen(w2)
		counterW2 += 1
		counterW1 = 0
	if counterW2 > 8:
		w3 = walzeDrehen(w3)
		counterW3 += 1
		counterW2 = 0
	if counterW3 > 8:
		w4 = walzeDrehen(w4)
		counterW4 += 1
		counterW3 = 0
	if counterW4 > 8:
		w5 = walzeDrehen(w5)
		counterW5 += 1
		counterW4 = 0
	if counterW5 > 8:
		w6 = walzeDrehen(w6)
		counterW6 += 1
		counterW5 = 0
	if counterW6 > 8:
		w7 = walzeDrehen(w7)
		counterW7 += 1
		counterW6 = 0
	
	if counterW7 > 8:
		w7 = walzeDrehen(w7)
		counterW7 = 0
		
	
	
	tmp = w0[int(klartextListe[i])-1]
	tmp = w1[tmp-1]
	tmp = w2[tmp-1]
	tmp = w3[tmp-1]
	tmp = w4[tmp-1]
	tmp = w5[tmp-1]
	tmp = w6[tmp-1]
	tmp = w7[tmp-1]
	geheimtext += str(tmp)
	
	
	w0 = walzeDrehen(w0)
	counterW0 += 1
	
print klartext
print geheimtext
	
