import re
from pgn_token import HalbzugToken, VarianteStartToken, VarianteEndToken, SpielendToken, Token
from halbzug import Halbzug
from zugnummer import Zugnummer
from spielstein import Spielstein, SpielsteinTyp
from farbe import Farbe
from koordinate import Koordinate

class PgnTokenizer:
    """Zerlegt PGN-Strings in eine Liste von Schachzügen und Metadaten."""
    spalten_buchstaben = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    # PGN-Notation: K=König, Q=Dame, R=Turm, B=Läufer, N=Springer, (Bauer hat kein Symbol)
    pgn_spielstein_notation = {
        'K': SpielsteinTyp.KOENIG,
        'Q': SpielsteinTyp.DAME,
        'R': SpielsteinTyp.TURM,
        'B': SpielsteinTyp.LAEUFER,
        'N': SpielsteinTyp.SPRINGER,
        '': SpielsteinTyp.BAUER,
    }

    def tokenize(self, pgn_string: str) -> list[Token]:
        """Konvertiert einen PGN-String in eine Liste von Tokens."""
        tokens = []
        ebene = 0
        zugnummer = None
        
        # Whitespace bereinigen und in Raw-Tokens aufteilen
        raw_tokens = self._split_pgn(pgn_string)
        
        i = 0
        while i < len(raw_tokens):
            raw_token = raw_tokens[i]
            
            if raw_token == '(':
                ebene += 1
                tokens.append(VarianteStartToken(ebene=ebene))
            elif raw_token == ')':
                tokens.append(VarianteEndToken(ebene=ebene))
                ebene -= 1
            elif raw_token == '*':
                tokens.append(SpielendToken())
            elif raw_token.startswith('$'):
                # NAG - wird an letzten Halbzug-Token angehängt
                nag = int(raw_token[1:])
                if tokens and isinstance(tokens[-1], HalbzugToken):
                    tokens[-1].halbzug.nag = nag
            elif self._ist_zugnummer(raw_token):
                zugnummer = self._parse_zugnummer(raw_token)
            elif zugnummer is not None and not raw_token.startswith('$'):
                # Das ist ein Halbzug nach einer Zugnummer
                try:
                    halbzug = self._parse_halbzug(raw_token, zugnummer)
                    tokens.append(HalbzugToken(ebene=ebene, halbzug=halbzug))
                    zugnummer = zugnummer.nachfolger()  # Für nächsten Halbzug
                except (ValueError, KeyError, IndexError):
                    # Token konnte nicht als Halbzug geparst werden
                    pass
            
            i += 1
        
        return tokens

    def _split_pgn(self, pgn_string: str) -> list[str]:
        """Teilt einen PGN-String in rohe Tokens auf."""
        # Klammern und Varianten-Symbole werden mit Whitespace getrennt
        pgn_string = pgn_string.replace('(', ' ( ').replace(')', ' ) ')
        # $ und * auch separiert
        pgn_string = re.sub(r'(\$\d+|\*)', r' \1 ', pgn_string)
        # Zugnummern von Zügen trennen (z.B. "1.d4" -> "1. d4")
        pgn_string = re.sub(r'(\d+\.\.?)([a-zA-Z0-9])', r'\1 \2', pgn_string)
        
        # In Tokens aufteilen und leere entfernen
        return [t for t in pgn_string.split() if t.strip()]

    def _ist_zugnummer(self, token: str) -> bool:
        """Prüft, ob ein Token eine Zugnummer ist."""
        return bool(re.match(r'^\d+\.{1,2}$', token))

    def _parse_zugnummer(self, token: str) -> Zugnummer:
        """Parst eine Zugnummer aus einem Token."""
        # '1.' = Weiß (Zug 1), '1...' = Schwarz (Zug 1)
        match = re.match(r'^(\d+)\.{1,2}$', token)
        if not match:
            raise ValueError(f"Ungültige Zugnummer: {token}")
        
        zugnummer_int = int(match.group(1))
        farbe = Farbe.W if token.count('.') == 1 else Farbe.S
        
        return Zugnummer(zugnummer_int, farbe)

    def _parse_halbzug(self, token: str, zugnummer: Zugnummer) -> Halbzug:
        """Parst einen Halbzug aus algebraischer Notation."""
        # Rochade?
        if token in ('O-O', 'O-O-O'):
            # Rochade wird mit König als Spielstein modelliert
            spielstein = Spielstein(SpielsteinTyp.KOENIG, zugnummer.farbe)
            if token == 'O-O':
                # Kurze Rochade: König e1 -> g1 (Weiß) oder e8 -> g8 (Schwarz)
                zu = Koordinate(7, 1 if zugnummer.farbe == Farbe.W else 8)
            else:
                # Lange Rochade: König e1 -> c1 (Weiß) oder e8 -> c8 (Schwarz)
                zu = Koordinate(3, 1 if zugnummer.farbe == Farbe.W else 8)
            
            return Halbzug(zugnummer, spielstein, zu)
        
        # Normaler Zug: [Spielstein][Disambiguierung][x]Ziel[+#]
        # Beispiele: d4, Nf6, Nbd2, exd5, Qxd5, Ke2+, Dd8#
        
        # Schach/Matt-Symbol entfernen
        ist_schach = token.endswith('+')
        ist_matt = token.endswith('#')
        if ist_schach or ist_matt:
            token = token[:-1]
        
        # Spielstein-Typ bestimmen (erstes Zeichen oder Bauer)
        spielstein_char = token[0] if token[0].isupper() else ''
        spielstein_typ = self.pgn_spielstein_notation.get(spielstein_char, SpielsteinTyp.BAUER)
        
        if spielstein_char:
            token = token[1:]  # Spielstein-Zeichen entfernen
        
        # Nun: [Disambiguierung][x]Ziel
        # Zielfeld (letzten 2 Zeichen: Spalte + Reihe)
        ziel_spalte = self.spalten_buchstaben[token[-2]]
        ziel_reihe = int(token[-1])
        zu = Koordinate(ziel_spalte, ziel_reihe)
        
        # Restlicher Token: Disambiguierung und Capture
        rest = token[:-2]
        von = None
        
        # Falls 'x' vorhanden, ist es ein Schlag
        if 'x' in rest:
            rest = rest.replace('x', '')
        
        # Disambiguierung parsen (z.B. 'b' in 'Nbd2', oder '3' in 'R3e3')
        # Bei Bauern kann die Spalte stehen (z.B. 'exd5')
        if rest:
            if rest[0].isdigit():
                # Reihe angegeben (nur Reihenangabe, Spalte unbekannt)
                # Diese Information speichern wir nicht, da von meist optional ist
                pass
            elif rest[0].isalpha():
                # Spalte angegeben
                spalte = self.spalten_buchstaben[rest[0]]
                # Wenn nur Spalte ohne Reihe, lassen wir von = None
                # Die Zug-Validierung kann damit umgehen
        
        spielstein = Spielstein(spielstein_typ, zugnummer.farbe)
        return Halbzug(zugnummer, spielstein, zu, von=von, ist_schach=ist_schach, ist_matt=ist_matt)
