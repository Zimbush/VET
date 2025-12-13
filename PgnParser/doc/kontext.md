# PgnParser

Das Programm liest eine Datei, in der eine Schachpartie im Format Portable Game Notation (pgn) notiert ist, und wandelt die Notation in einen Variantenbaum um.

## Entwicklungsumgebung

- Programmiersprache Python
- Projektverwaltung mittels uv
- virtuelle Umgebung: uv venv --python 3.14
- pytest
- Ordner src: funktionaler Code
- Ordner test: Modultests
- python-chess: keine Verwendung

## Code Conventions

- PEP 8 grundsätzlich beachten
- keine docstring-Kommentare
- Enum möglichst nutzen
- Klassen in der Regel als Dataclass anlegen
- Bei Klassen prüfen, ob die Objekte unveränderlich sein sollten.

## Fachliche Klassen

- Die Farben im Schach (Spieler, Zugrecht, Farbe des Spielsteins) werden als Enum modelliert.
- Das Schachbrett ist eine 8 x 8-Matrix von Feldern.
- Eine Koordinate ist ein Paar von zwei Ganzzahlen, die zuerst die Spalte, dann die Reihe bezeichnen.
  - Die textuelle Darstellung einer Koordinate wird als Paar aus einem Buchstaben und der Reihennummer geschrieben.
- Ein Feld
  - besitzt eine Koordinate.
  - ist entweder
    - leer oder
    - mit genau einem Spielstein besetzt.
- Es gibt die Spielsteine:
  - König
  - Dame
  - Turm
  - Läufer
  - Springer
  - Bauer
- Ein Spielstein besitzt eine Farbe.
- Ein Halbzug besitzt folgende Attribute:
  - Zugnummer
  - Spielstein
  - Startfeld: ist temporär leer oder nur teilweise gefüllt.
  - Zielfeld
  - optional: Schachgebot
  - optional: Umwandlung in Spielstein

## Programmlogik

- Die pgn-Notation ist ein String. Dieser wird zuerst in eine Liste von Token umgewandelt.
- Ein Token besitzt folgende Attribute:
  - Die Variantenebene
  - Die Zugnummer
  - Der Halbzug
