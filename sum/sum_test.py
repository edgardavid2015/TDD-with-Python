# El metodo suma puede tomar dos numeros en un string separado por comas,
# sumarlo y devolver el resultado como un entero. suma \n  '1\n 2, 3' 6
# si termina en , o en \n lanzar un error

import pytest
from sum import suma


def __generate_operands():
    return


def test_sum_returns_zero_when_argument_is_an_empty_string():
    assert 0 == suma('')


def test_sum_two_numbers_splitted_by_commas():
    assert 1 == suma('1,0')


@pytest.mark.parametrize('operands, result', [('1,2,4', 7), ('10,20,25,30', 85), ('100,100,100,50,50', 400)])
def test_sum_more_than_two_numbers_splitted_by_commas(operands, result):
    assert result == suma(operands)


def test_sum_two_numbers_splitted_by_new_line_character():
    assert 3 == suma('1\n2')


@pytest.mark.parametrize('operands, result', [('1\n3\n5', 9), ('1\n10\n100\n1000', 1111)])
def test_sum_more_than_two_numbers_splitted_by_new_line_character(operands, result):
    assert result == suma(operands)


def test_sum_two_numbers_splitted_by_commas_and_new_line_character():
    assert 8 == suma('1,2\n5')


def test_throws_exception_when_after_a_comma_appears_a_blank_space():
    with pytest.raises(ValueError):
        suma('1,2,1,2,')


def test_throws_exception_when_after_a_new_line_separator_appears_a_blank_space():
    with pytest.raises(ValueError):
        suma('1\n4\n10\n')
