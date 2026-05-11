import pytest

def test_adaugare():
    assert 2 + 2 == 4

def test_mesaj():
    mesaj = "Salut din feature B"
    assert len(mesaj) > 0
    assert "Salut" in mesaj

def test_functia_salut():
    from main import salut
    assert salut() == "Salut din feature Aa"