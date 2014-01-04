RoCiMa
======

Enigma and other rotor cipher maschines

#### Plädoyer:
Die Rotor Chiffriermaschienen repräsentieren den technischen Stand mechanischer Verschlüsselungsaperaturen, zur Zeit
des zweiten Weltkriegs. Die Enigma ist wohl der bekannteste Vertreter dieser Art. Alle RCMs basieren auf Walzen, durch
die Drähte verlaufen und so eine Tastatur mit einem Lampenfeld oder wahlweise einem Fernschreiber verbanden. Das Geheim-
niss bestand in der genauen Verdrahtung der Walzen, der Lage der verschiedenen Walzen in der Maschiene, der Anfangsposition
und dem Steckerbrett. Die Enigma wurde durch Alan Turing, einem britischen Kryptoanalyst, der für das GCHQ tätig war, nach
Vorarbeit durch den polnischen Geheimdienst gebrochen. Für die polnische Vorarbeit, war unteranderm ein deutscher Spion
verantwortlich, der den Polen Codebücher über mehrere Monate zukommen ließ. Turing erkannte Schwachstellen in der Benutzung
der Maschiene durch die Nationalsozialisten und nutzte diese um einen Anhaltspunkt zu finden um mithilfe primitiver
"Computer" das deutsche Standbein der Kriegskommunikation zu brechen. Seine Vorgesetzten hielten diese Errungenschaft lange
Zeit geheim um störungsfrei deutsche Kommunuikation abhören zu können. Der Bruch dieses Verschlüsselungssystem wird gemeinhin
als wichtiger Faktor für den Ausgang des Krieges gesehen. Die durch Turing erfolgte Entschlüsselung ist allerdings eher auf
Bedienungsfehler, wie Wiederholungen, einfache Schlüssel und statische Nachrichteninhalte sowie auf eine geringe Schlüsselzahl
zurückzuführen, als auf Unsicherheit des Systems. Durch Alan Turings Arbeit besitzen wir heutzutage jedoch leistungsfähige
Computer, die in der Lage sind, die Komplexität der Enigma zu verhundertfachen und die Walzenanzahl zu verzehnfachen.
Insofern ist die Enigma weiterhin ein gutes Verschlüsselungssystem, auch wenn es in den Zeiten asymmetrischer Kryptographie
eher symbolischen Wert hat.

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

#### /tmp/
* Die Dateien ENI.W5.oS.R.py und ENI.W8.oS.oR.py müssen noch an die Konventionen angepasst werden.


