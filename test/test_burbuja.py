from src.burbuja import ordenar


def test_ordenar():
    assert ordenar([8, 3, 1, 19, 14]) == [1, 3, 8, 14, 19]