import pytest
from pgn_parser import PgnTokenizer
from pgn_token import HalbzugToken, VarianteStartToken, VarianteEndToken, SpielendToken
from halbzug import Halbzug
from zugnummer import Zugnummer
from farbe import Farbe
from spielstein import SpielsteinTyp

def test_tokenizer_simple_move():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.d4")
    
    assert len(tokens) == 1
    assert isinstance(tokens[0], HalbzugToken)
    assert tokens[0].halbzug.zu.spalte == 4
    assert tokens[0].halbzug.zu.reihe == 4

def test_tokenizer_two_moves():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.d4 Nf6")
    
    assert len(tokens) == 2
    assert isinstance(tokens[0], HalbzugToken)
    assert isinstance(tokens[1], HalbzugToken)
    assert tokens[0].halbzug.spielstein.typ == SpielsteinTyp.BAUER
    assert tokens[1].halbzug.spielstein.typ == SpielsteinTyp.SPRINGER

def test_tokenizer_move_numbers():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.e4 e5 2.Nf3")
    
    assert isinstance(tokens[0], HalbzugToken)
    assert isinstance(tokens[1], HalbzugToken)
    assert isinstance(tokens[2], HalbzugToken)
    assert tokens[0].halbzug.zugnummer.farbe == Farbe.W
    assert tokens[1].halbzug.zugnummer.farbe == Farbe.S
    assert tokens[2].halbzug.zugnummer.farbe == Farbe.W

def test_tokenizer_schach():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.Ke2+")
    
    assert isinstance(tokens[0], HalbzugToken)
    assert tokens[0].halbzug.ist_schach is True
    assert tokens[0].halbzug.ist_matt is False

def test_tokenizer_matt():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("10.Dd8#")
    
    assert isinstance(tokens[0], HalbzugToken)
    assert tokens[0].halbzug.ist_matt is True
    assert tokens[0].halbzug.ist_schach is False

def test_tokenizer_nag():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.d4 $1")
    
    assert len(tokens) == 1
    assert isinstance(tokens[0], HalbzugToken)
    assert tokens[0].halbzug.nag == 1

def test_tokenizer_variante():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.d4 ( 1.e4 ) 1.d4")
    
    assert isinstance(tokens[0], HalbzugToken)
    assert isinstance(tokens[1], VarianteStartToken)
    assert isinstance(tokens[2], HalbzugToken)
    assert isinstance(tokens[3], VarianteEndToken)
    assert isinstance(tokens[4], HalbzugToken)

def test_tokenizer_spielende():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.d4 *")
    
    assert isinstance(tokens[1], SpielendToken)

def test_tokenizer_rochade_kurz():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.O-O")
    
    assert isinstance(tokens[0], HalbzugToken)
    halbzug = tokens[0].halbzug
    assert halbzug.spielstein.typ == SpielsteinTyp.KOENIG
    assert halbzug.zu.spalte == 7
    assert halbzug.zu.reihe == 1

def test_tokenizer_rochade_lang():
    tokenizer = PgnTokenizer()
    tokens = tokenizer.tokenize("1.O-O-O")
    
    assert isinstance(tokens[0], HalbzugToken)
    halbzug = tokens[0].halbzug
    assert halbzug.spielstein.typ == SpielsteinTyp.KOENIG
    assert halbzug.zu.spalte == 3
    assert halbzug.zu.reihe == 1

def test_tokenizer_beispiel_pgn():
    tokenizer = PgnTokenizer()
    pgn = "1.d4 Nf6 2.Nf3 g6 3.Nbd2 ( 3.Nc3 Bg7 ) 3...Bg7 4.e4 $1 O-O $6 5.Bd3 d5 6.exd5 Qxd5 $14 *"
    tokens = tokenizer.tokenize(pgn)
    
    # Sollte mehrere Tokens enthalten
    assert len(tokens) > 10
    # Letzte Token sollte Spielende sein
    assert isinstance(tokens[-1], SpielendToken)
