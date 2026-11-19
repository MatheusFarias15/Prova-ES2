from idade import MINIMA, idade_permitida


def test_t1_idade_exatamente_limite():
    # RF01: idade exatamente 21 -> aceita (True)
    assert idade_permitida(21) is True


def test_t2_idade_limite_menos_um():
    # RF02: idade 20 -> rejeitada (False)
    assert idade_permitida(20) is False


def test_t3_idade_101():
    # RF03: idade 101 -> rejeitada (False)
    assert idade_permitida(101) is False