import pytest
import FizzBuzz


def should_return_fizz_for_multiples_of_3():
    # Arrange
    # Act
    actual_result = fizz_buzz(3)
    # Assert
    assert 'Fizz' == actual_result
