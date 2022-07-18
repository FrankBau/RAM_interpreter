Input:
==
Eine Folge von Zahlen (input tape)

Output:
==
Eine Folge von Zahlen (output tape)


RAM registers
==
R[0], R[1], ... index: eine nat. Zahl

R[0] ist der Akkumulator


RAM instructions
==
instructions are numbered by nat. numbers, starting with 0

READ    liest die nächste Zahl vom input in den Akkumulator
WRITE   gibt den Inhalt von Akkumulator auf dem output aus

LOADIMM i  schreibt die Konstante i in den Akkumulator

LOAD i  kopiert den Inhalt von Register i in den Akkumulator
STORE i kopiert den Wert aus dem Ak in das Register i

ADD i   addiert den Inhalt von Register i zum Wert im Akkumulator
SUB i   subtrahiert den Inhalt von Register i vom Wert im Akkumulator

JUMP i  unbedingter Sprung zum Befehl Nummer i
JZERO i bedingter Sprung zum Befehl Nummer i falls der Inhalt von A Null ist
JGTZ i  bedingter Sprung zum Befehl Nummer i falls der Inhalt von A größer als Null ist

HALT    hält die Programmausführung an
