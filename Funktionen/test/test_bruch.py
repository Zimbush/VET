import pytest
from src.bruch import Bruch_LY, Bruch_PY, Bruch_DC, Bruch_IM


class TestBruch_LY:
    
    def test_init(self):
        bruch = Bruch_LY(3, 4)
        assert bruch.zaehler == 3
        assert bruch.nenner == 4
    
    def test_init_nenner_null(self):
        with pytest.raises(ValueError):
            Bruch_LY(1, 0)
    
    def test_gleichheit_gleich(self):
        bruch1 = Bruch_LY(3, 4)
        bruch2 = Bruch_LY(3, 4)
        assert bruch1 == bruch2
    
    def test_gleichheit_ungleich_zaehler(self):
        bruch1 = Bruch_LY(3, 4)
        bruch2 = Bruch_LY(1, 4)
        assert bruch1 != bruch2
    
    def test_gleichheit_ungleich_nenner(self):
        bruch1 = Bruch_LY(3, 4)
        bruch2 = Bruch_LY(3, 2)
        assert bruch1 != bruch2
    
    def test_str(self):
        bruch = Bruch_LY(3, 4)
        assert str(bruch) == "(3,4)"
    
    def test_str_negative(self):
        bruch = Bruch_LY(-5, 8)
        assert str(bruch) == "(-5,8)"


class TestBruch_PY:
    
    def test_init(self):
        bruch = Bruch_PY(3, 4)
        assert bruch.zaehler == 3
        assert bruch.nenner == 4
    
    def test_init_nenner_null(self):
        with pytest.raises(ValueError):
            Bruch_PY(1, 0)
    
    def test_property_getter(self):
        bruch = Bruch_PY(5, 6)
        assert bruch.zaehler == 5
        assert bruch.nenner == 6
    
    def test_property_setter(self):
        bruch = Bruch_PY(3, 4)
        bruch.zaehler = 7
        assert bruch.zaehler == 7
    
    def test_property_setter_nenner(self):
        bruch = Bruch_PY(3, 4)
        bruch.nenner = 8
        assert bruch.nenner == 8
    
    def test_property_setter_nenner_null(self):
        bruch = Bruch_PY(3, 4)
        with pytest.raises(ValueError):
            bruch.nenner = 0
    
    def test_gleichheit_gleich(self):
        bruch1 = Bruch_PY(3, 4)
        bruch2 = Bruch_PY(3, 4)
        assert bruch1 == bruch2
    
    def test_gleichheit_ungleich_zaehler(self):
        bruch1 = Bruch_PY(3, 4)
        bruch2 = Bruch_PY(1, 4)
        assert bruch1 != bruch2
    
    def test_gleichheit_ungleich_nenner(self):
        bruch1 = Bruch_PY(3, 4)
        bruch2 = Bruch_PY(3, 2)
        assert bruch1 != bruch2
    
    def test_str(self):
        bruch = Bruch_PY(3, 4)
        assert str(bruch) == "(3,4)"
    
    def test_str_negative(self):
        bruch = Bruch_PY(-5, 8)
        assert str(bruch) == "(-5,8)"


class TestBruch_DC:
    
    def test_init(self):
        bruch = Bruch_DC(3, 4)
        assert bruch.zaehler == 3
        assert bruch.nenner == 4
    
    def test_init_nenner_null(self):
        with pytest.raises(ValueError):
            Bruch_DC(1, 0)
    
    def test_gleichheit_gleich(self):
        bruch1 = Bruch_DC(3, 4)
        bruch2 = Bruch_DC(3, 4)
        assert bruch1 == bruch2
    
    def test_gleichheit_ungleich_zaehler(self):
        bruch1 = Bruch_DC(3, 4)
        bruch2 = Bruch_DC(1, 4)
        assert bruch1 != bruch2
    
    def test_gleichheit_ungleich_nenner(self):
        bruch1 = Bruch_DC(3, 4)
        bruch2 = Bruch_DC(3, 2)
        assert bruch1 != bruch2
    
    def test_str(self):
        bruch = Bruch_DC(3, 4)
        assert str(bruch) == "(3,4)"
    
    def test_str_negative(self):
        bruch = Bruch_DC(-5, 8)
        assert str(bruch) == "(-5,8)"


class TestBruch_IM:
    
    def test_init(self):
        bruch = Bruch_IM(3, 4)
        assert bruch.zaehler == 3
        assert bruch.nenner == 4
    
    def test_init_nenner_null(self):
        with pytest.raises(ValueError):
            Bruch_IM(1, 0)
    
    def test_immutability(self):
        bruch = Bruch_IM(3, 4)
        with pytest.raises(AttributeError):
            bruch.zaehler = 5
    
    def test_immutability_nenner(self):
        bruch = Bruch_IM(3, 4)
        with pytest.raises(AttributeError):
            bruch.nenner = 8
    
    def test_gleichheit_gleich(self):
        bruch1 = Bruch_IM(3, 4)
        bruch2 = Bruch_IM(3, 4)
        assert bruch1 == bruch2
    
    def test_gleichheit_ungleich_zaehler(self):
        bruch1 = Bruch_IM(3, 4)
        bruch2 = Bruch_IM(1, 4)
        assert bruch1 != bruch2
    
    def test_gleichheit_ungleich_nenner(self):
        bruch1 = Bruch_IM(3, 4)
        bruch2 = Bruch_IM(3, 2)
        assert bruch1 != bruch2
    
    def test_str(self):
        bruch = Bruch_IM(3, 4)
        assert str(bruch) == "(3,4)"
    
    def test_str_negative(self):
        bruch = Bruch_IM(-5, 8)
        assert str(bruch) == "(-5,8)"
    
    def test_hash(self):
        bruch1 = Bruch_IM(3, 4)
        bruch2 = Bruch_IM(3, 4)
        assert hash(bruch1) == hash(bruch2)
    
    def test_in_set(self):
        bruch1 = Bruch_IM(3, 4)
        bruch2 = Bruch_IM(3, 4)
        bruch_set = {bruch1}
        assert bruch2 in bruch_set
    
    def test_as_dict_key(self):
        bruch = Bruch_IM(3, 4)
        bruch_dict = {bruch: "three quarters"}
        assert bruch_dict[bruch] == "three quarters"
