#coding: utf-8
# ENI.W3.oS.oR
# ENI: Enigma
# W3: drei Walzen
# oS: ohne Steckbrett
# oR: ohne Reflektor


def walzeDrehen(walze):
	'''Die Funktion walzeDrehen verschiebt jedes Element eines Arrays um eine Stelle nach rechts'''
	tmp = walze[1:len(walze)]
	tmp.append(walze[0])
	walze = tmp
	return walze



# Die Verdrahtung der Walzen kann durch simple Arrays dargestellt werden.

# Benutzerdefinierte Verdrahtung der Walzen [DEBUG]
# walzen = []
# frage = 'Bitte eine beliebige Reihenfolge der Zahlen 1-8 eingeben, in der jede Zahl ein einziges Mal vorkommt: \n'
# for i in range(3):
# 	walzen.append(list(raw_input(frage)))
# w0 = walzen[0]
# w1 = walzen[1]
# w2 = walzen[2]

# Im Quellcode festgelegte Walzenverdrahtung [HISTORY]
w0 = [3,8,5,1,7,2,6,4] 
w1 = [8,1,7,3,6,5,2,4]
w2 = [4,2,6,7,3,8,5,1]


# Benutzerdefinierter Klartext [HISTORY]
klartext = raw_input('Bitte eine Kombination von Zahlen von 1 bis 8 eingeben: \n')

# Im Quellcode festgelegter Klartext [DEBUG][NoHistory]
# klartext = '163826572354263245232547467567583562462523451'


klartextListe = list(klartext)
geheimtext = ''

counterW0 = 0 # Diese Counter zählen die Durchläufe der Walzen
counterW1 = 0
counterW2 = 0

for counter in xrange(len(klartext)):
	if counterW0 > 8:
		w1 = walzeDrehen(w1)
		counterW1 += 1
		counterW0 = 0
	if counterW1 > 8:
		w2 = walzeDrehen(w2)
		counterW2 += 1
		counterW1 = 0
	
	tmp = w0[int(klartextListe[i])-1]
	tmp = w1[tmp-1]
	tmp = w2[tmp-1]
	geheimtext += str(tmp)
	print str(counterW0) + ' ' + str(counterW1) + ' ' + str(counterW2) + ' | ' + str(tmp)	
	
	w0 = walzeDrehen(w0)
	counterW0 += 1
	
print geheimtext
		 
