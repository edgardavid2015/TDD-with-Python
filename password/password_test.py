# hacer una funcion que valide un password:
# 1 largo de al menos 8 caracteres, si no devuelve este mensaje: El password por lo menos debe tener 8 char
# 2 que por lo menos contenga 2 numeros. sino que de devuelva un mensaje diciendote que debe tener 2 numeros
# 3 si el passwor tiene mas de 1 error que te devuelva todos los mensajes de error separados por un \n
# 4 que el pass tenga por lo menos una letra en mayuscula, sino mensaje de error descriptivo
# 5 que el pass tenga por lo menos un caracter especial, sino mensaje de error.

import pytest
from password import password_validator


def test_show_error_message_when_password_length_is_less_than_eight_char():
    assert password_validator('12345') == 'Password length must be greater than 8 characters'


def test_show_accept_message_when_password_length_is_eight_or_more_char():
    assert password_validator('12345678') == 'Password accepted'

