from idade import MINIMA, idade_permitida


def test_t1_idade_exatamente_limite():
    assert idade_permitida(MINIMA) is True


def test_t2_idade_limite_menos_um():
    assert idade_permitida(MINIMA - 1) is False


def test_t3_idade_101():
    assert idade_permitida(101) is False


def test_t4_idade_limite_mais_meio():
    assert idade_permitida(MINIMA + 0.5) is False