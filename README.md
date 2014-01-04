RoCiMa
======

Enigma and other rotor cipher maschines

#### Projektinterne Konventionen:
1. [DEBUG] kennzeichnet Features, die für die Entwicklung bestimmt sind
2. [HISTORY] kennzeichnet Features, die der historischen Vorlage (Enigma) entsprechen.
3. [NoHistory] kennzeichnet Features, die nicht der historischen Vorlage entsprechen.
   (Meist gleichbedeutend mit [DEBUG])
4. Es wird mit Tabs eingerückt.
5. Rückgabewerte allgemeiner Funktionen tragen den Namen "result".
6. Wird durch eine Liste iteriert trägt die Zählvariable den Namen "element".
   (Auch in anderen Projekten zu finden)
7. Wird eine for-Schleife zum zählen verwendet, so heißt die Zählvariable "counter".
8. Kommentare werden mit "#" erstellt (Ausnahme: Docstrings!)

###### Dateinamenkonvention:
Die komischen Dateinamen kommen so zusammen:
<Kürzel des historischen Vorbilds>.W<Walzenzahl>.<Steckerbrett?>.<Reflektor>.py 

#### Anhänge:
In manchen Codedateien wird auf Anhänge verwiesen, welche im Ordner "Anhang" zu finden sind.

#### TODO:
* [HISTORY]   Veränderungsmöglichkeit der Walzenlage durch den Benutzer 
* [HISTORY]   Eingabe von Buchstaben
*             Möglichkeit zufallsgenerierter Walzenanordnungen (siehe Anhang A)
* [HISTORY]   Möglichkeit die Startposition der Walzen festzulegen
* [NoHistory] Variable Walzenzahl
* [DEBUG]     Häufigkeitsanalyse des Geheimtextes
* [DEBUG]     Speichermöglichkeit der Walzen

#### /tmp/
* Die Dateien ENI.W5.oS.R.py und ENI.W8.oS.oR.py müssen noch an die Konventionen angepasst werden.


