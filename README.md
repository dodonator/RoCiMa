RoCiMa
======

Enigma and other rotor cipher maschines

#### Plädoyer:
Die Rotor Chiffriermaschinen repräsentieren den technischen Stand mechanischer Verschlüsselungsaperaturen, zur Zeit
des zweiten Weltkriegs. Die Enigma ist wohl der bekannteste Vertreter dieser Art. Alle RCMs basieren auf Walzen, durch
die Drähte verlaufen und so eine Tastatur mit einem Lampenfeld oder wahlweise einem Fernschreiber verbanden. Das Geheim-
niss bestand in der genauen Verdrahtung der Walzen, der Lage der verschiedenen Walzen in der Maschine, der Anfangsposition
und dem Steckerbrett. Die Enigma wurde durch Alan Turing, einem britischen Kryptoanalyst, der für das GCHQ tätig war, nach
Vorarbeit durch den polnischen Geheimdienst gebrochen. Für die polnische Vorarbeit, war unteranderm ein deutscher Spion
verantwortlich, der den Polen Codebücher über mehrere Monate zukommen ließ. Turing erkannte Schwachstellen in der Benutzung
der Maschine durch die Nationalsozialisten und nutzte diese, um einen Anhaltspunkt zu finden um mithilfe primitiver
"Computer" das deutsche Standbein der Kriegskommunikation zu brechen. Seine Vorgesetzten hielten diese Errungenschaft lange
Zeit geheim um störungsfrei deutsche Kommunuikation abhören zu können. Der Bruch dieses Verschlüsselungssystem wird gemeinhin
als wichtiger Faktor für den Ausgang des Krieges gesehen. Die durch Turing erfolgte Entschlüsselung ist allerdings eher auf
Bedienungsfehler, wie Wiederholungen, einfache Schlüssel und statische Nachrichteninhalte sowie auf eine geringe Schlüsselzahl
zurückzuführen, als auf Unsicherheit des Systems. Durch Alan Turings Arbeit besitzen wir heutzutage jedoch leistungsfähige
Computer, die in der Lage sind, die Komplexität der Enigma zu verhundertfachen und die Walzenanzahl zu verzehnfachen.
Insofern ist die Enigma weiterhin ein gutes Verschlüsselungssystem, auch wenn es in den Zeiten asymmetrischer Kryptographie
eher symbolischen Wert hat.
#### Technik:
Die deutsche Enigma basierte, sowie die meisten RCMs, auf dem Einsatz von mehreren intern verdrahteten
Walzen. Jede Walze war, alleine, eine einfache Permutation, das bedeutet, das jeder Buchstabe durch einen
anderen ersetzt wurde. Diese Form der monoalphabetischen Substitution wurde schon von arabischen Kryptoanalysten
gebrochen und ist somit weit überholt. Der Vorteil war, dass die Walzen sich drehen konnten und somit jede
Walze so eine Cäsarverschiebung auf das, durch die Verdrahtung festgelegte Alphabet machte. Das allein
reicht jedoch immer noch nicht, um ein geeignetes Maß an Sicherheit zu erreichen. Eine RCM bestand nun
aus mehreren Walzen, die hintereinander (in Reihe) angeordnet waren und sich in einem bestimmten Muster drehten.
Dabei konnte die Anfangsposition der Walzen, und die Anordnug der Walzen als Schlüssel benutzt werden.
Die Verdrahtung der Walzen konnte jedoch nicht als Schlüssel verwendet werden, weil sie statisch war und
daher zum Algorithmus gehörte. Die einfachste Synchronisation der Walzen wäre alle gleichzeitig drehen
zu lassen, was allerdings nicht sicher genug wäre, weil die Anzahl möglicher Schlüssel darunter leiden würde.
Die von den Deutschen benutzte Synchronisation, welche im Gerät festgelegt war und daher ebenfalls zum Algorithmus
und nicht zum Schlüssel gehört, bestand darin, dass die erste Walze sich drehte. Sobald Walze 1 eine
vollständige Umdrehung gemacht hatte, drehte sich Walze 2 um einen Schritt weiter. Sobald diese eine
volle Umdrehung vollbracht hatte drehte sich die nächste Walze einen Schritt weiter. Diese Synchronisation
gehörte auch zum kryptographischen Algorithmus und konnte daher bekannt sein. Ein weiteres, allerdings zu
vernachlässigendes, Bauteil der RCMs war das Steckerbrett. Auf dem Steckerbrett konnte der Anwender, mit Hilfe
von ein paar Verbindungen, Buchstabenpaare tauschen. Dies entspricht jedoch einer teilweise durchgeführten
Substitution (monoalphabetisch) und bringt daher ein geringes Maß an Sicherheit aber ein zusätzliches Paket
an möglichen Schlüssel. Im Verlauf des Krieges wurde die Enigma mehrfach nachgerüstet, teilweise wurde die Walzenzahl
erhöht oder die Anzahl der Steckverbindungen auf dem Steckerbrett. Eine Neuerung war auch der sogenannte "Reflektor".
Dieser Refloktor leitete die ankommenden Signale erneut in umgekehrter Reihenfolge durch alle Walzen durch und
"spiegelte" sozusagen die Walzenanordnung. Der Reflektor macht es allerdings nicht schwieriger den Schlüssel
herauszufinden, weil er die maximale Schlüsselanzahl nicht erhöht.
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

##### Dateinamenkonvention:
Die komischen Dateinamen kommen so zusammen:

> Kürzel des historischen Vorbilds.W+Walzenzahl.Steckerbrett?.Reflektor?.py 

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
*             Den Quellcode auf OOP umbauen
* [HISTORY]   Die Verwendung eines Schlüssels ermöglichen
* [HISTORY]   Dechiffrierroutine

#### /tmp/
* Die Dateien ENI.W5.oS.R.py und ENI.W8.oS.oR.py müssen noch an die Konventionen angepasst werden.


