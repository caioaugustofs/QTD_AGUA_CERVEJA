import pytest
from calc_aguaCerveja import CalculadoraAguaCerveja

@pytest.fixture
def calculadora():
    return CalculadoraAguaCerveja(
        ltc=20.0,
        rzm=3.0,
        qMalte=5.0,
        absMalte=1.0,
        evap=4.0,
        trubQ=1.0,
        trubF=1.0
    )

def test_perdasTrubTotal(calculadora):
    assert pytest.approx(calculadora.perdasTrubTotal()) == 2.0

def test_perdasContracao(calculadora):
    assert pytest.approx(calculadora.perdasContracao()) == 1.04

def test_perdasMalte(calculadora):
    assert pytest.approx(calculadora.perdasMalte()) == 5.0

def test_perdas(calculadora):
    assert pytest.approx(calculadora.perdas()) == 12.04

def test_aguaMostura(calculadora):
    assert pytest.approx(calculadora.aguaMostura()) == 15.0

def test_aguaLavagem(calculadora):
    assert pytest.approx(calculadora.aguaLavagem()) == 17.04

def test_aguaTotal(calculadora):
    assert pytest.approx(calculadora.aguaTotal()) == 32.04

def test_getinfo(calculadora):

    info = calculadora.getinfo()
    assert pytest.approx(info['agua_mostura']) == 15.0
    assert pytest.approx(info['agua_lavagem']) == 17.04
    assert pytest.approx(info['perdas']) == 12.04
    assert pytest.approx(info['agua_total']) == 32.04
