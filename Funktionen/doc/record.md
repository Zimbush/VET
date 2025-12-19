# Python: Dataclass

Code-Beispiele zu OOP mit Python, insbesondere zur Nutzung der Dataclass-Annotation

Als fachlicher Gegenstand soll die Bruchrechnung dienen. Es sollen also verschiedene Varianten einer Klasse gezeigt werden, die einen mathematischen Bruch modellieren. Zu jeder Klasse soll ein Test mit pytest generiert werden.

Für alle Klassen soll gelten:

- Zwei Brüche sind genau dann gleich, wenn jeweils die beiden Zähler und die beiden Nenner übereinstimmen.
- Die textuelle Darstellung lautet "(&lt;zaehler&gt;,&lt;nenner&gt;)"
- Keine Docstring-Kommentare
- Verwendung von Type-Hints

Es sollen folgende Code-Beispiele erzeugt werden:

- Eine Klasse Bruch_LY ohne Nutzung von @dataclass
- Eine Klasse Bruch_PY ohne Nutzung von @dataclass, mit dunder-Attributen und Properties zum Lesen und Setzen der Attribute
- Eine Klasse Bruch_DC mit Verwendung von @dataclass
- Eine Klasse Bruch_IM mit unveränderlichen Attributen
