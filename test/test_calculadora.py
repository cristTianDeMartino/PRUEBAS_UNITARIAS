from src.calculadora import sumar_num, restar_num, multiplicar_num, dividir_num


def test_sum():

    assert sumar_num(5, 5) == 10
    assert sumar_num(0, 0) == 0
    assert sumar_num(-5, 3) == -2


def test_rest():
    assert restar_num(10, 8) == 2


def test_mult():
    assert multiplicar_num(2, 2) == 4
    assert multiplicar_num(2, 0) == 0
    assert multiplicar_num(2, 1) == 0


def test_div():
    assert dividir_num(10, 2) == 5
