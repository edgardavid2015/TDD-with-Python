# Una funcion llamada FizzBuzz que
# Cuando recibe un numero divisible por 3 devuelve Fizz
# Cuando recibe un numero divisible por 5 devuelve Buzz
# Cuando recibe un mumber divisible por 3 y 5 devuelve FizzBuzz
import pytest
import random


def fizz_buzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'


def __generate_multiples_of_3_and_5():
    return [i for i in range(1, random.randrange(100, 1000)) if i % 3 == 0 and i % 5 == 0]


def __generate_multiples_of_3():
    return [i for i in range(1, random.randrange(100, 1000)) if i % 3 == 0 and not i % 5 == 0]


def __generate_multiples_of_5():
    return [i for i in range(1, random.randrange(100, 1000)) if i % 5 == 0 and not i % 3 == 0]


@pytest.mark.parametrize('number', __generate_multiples_of_3())
def test_should_return_fizz_when_number_is_multiple_of_3(number):
    assert 'Fizz' == fizz_buzz(number)


@pytest.mark.parametrize('number', __generate_multiples_of_5())
def test_should_return_buzz_when_number_is_multiple_of_5(number):
    assert 'Buzz' == fizz_buzz(number)


@pytest.mark.parametrize('number', __generate_multiples_of_3_and_5())
def test_should_return_fizzbuzz_when_number_is_multiple_of_3_and_5(number):
    assert 'FizzBuzz' == fizz_buzz(number)
