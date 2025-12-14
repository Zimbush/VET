import pytest
from pgn_token import HalbzugToken, VarianteStartToken, VarianteEndToken, SpielendToken
from halbzug import Halbzug
from koordinate import Koordinate
from spielstein import Spielstein, SpielsteinTyp
from farbe import Farbe
from zugnummer import Zugnummer

def test_halbzug_token():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1))
    token = HalbzugToken(ebene=0, halbzug=halbzug)
    
    assert token.ebene == 0
    assert token.halbzug == halbzug

def test_halbzug_token_mit_nag():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1), nag=1)
    token = HalbzugToken(ebene=0, halbzug=halbzug)
    
    assert token.halbzug.nag == 1

def test_variante_start_token():
    token = VarianteStartToken(ebene=1)
    assert token.ebene == 1

def test_variante_end_token():
    token = VarianteEndToken(ebene=1)
    assert token.ebene == 1

def test_spielend_token():
    token = SpielendToken()
    assert isinstance(token, SpielendToken)
