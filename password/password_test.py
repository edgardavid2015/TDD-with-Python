# hacer una funcion que valide un password:
# 1 largo de al menos 8 caracteres, si no devuelve este mensaje: El password por lo menos debe tener 8 char
# 2 que por lo menos contenga 2 numeros. sino que de devuelva un mensaje diciendote que debe tener 2 numeros
# 3 si el passwor tiene mas de 1 error que te devuelva todos los mensajes de error separados por un \n
# 4 que el pass tenga por lo menos una letra en mayuscula, sino mensaje de error descriptivo
# 5 que el pass tenga por lo menos un caracter especial, sino mensaje de error.

import pytest
from password import password_validator


@pytest.mark.parametrize('invalid_length_passwords', ['1234', '12345', '1234567'])
def test_show_error_message_when_password_length_is_less_than_eight_char(invalid_length_passwords):
    assert password_validator(invalid_length_passwords) == 'Password length must be greater than 8 characters'


@pytest.mark.parametrize('invalid_numbers_in_password', ['1Aabbccdd', 'tuvWxyz1', '1passworD'])
def test_show_error_message_when_password_has_less_than_two_numbers(invalid_numbers_in_password):
    assert password_validator(invalid_numbers_in_password) == 'Password must have at least 2 numbers'


@pytest.mark.parametrize('invalid_uppercase_letters_passwords', ['01aabbccdd', 'mnopq1234', 'p4ssw0rd'])
def test_show_error_message_when_password_has_less_than_one_uppercase_letter(invalid_uppercase_letters_passwords):
    assert password_validator(invalid_uppercase_letters_passwords) == 'Password must have at least one uppercase letter'
