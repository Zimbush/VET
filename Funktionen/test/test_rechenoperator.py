import pytest
from src.rechenoperator import Operator


class TestOperator:
    """Tests für die Operator-Klasse."""
    
    def test_addition(self):
        """Test Addition von zwei Gleitkommazahlen."""
        assert Operator.ADD.verknuepfen(5.5, 3.2) == pytest.approx(8.7)
        assert Operator.ADD.verknuepfen(0, 0) == 0
        assert Operator.ADD.verknuepfen(-5, 3) == -2
    
    def test_multiplikation(self):
        """Test Multiplikation von zwei Gleitkommazahlen."""
        assert Operator.MULT.verknuepfen(5.5, 3.2) == pytest.approx(17.6)
        assert Operator.MULT.verknuepfen(0, 100) == 0
        assert Operator.MULT.verknuepfen(-5, 3) == -15
        assert Operator.MULT.verknuepfen(-5, -3) == 15
    
    def test_enum_values(self):
        """Test die Enum-Werte."""
        assert Operator.ADD.value == "+"
        assert Operator.MULT.value == "*"
