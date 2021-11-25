# Apply the TDD methodology to create a validation function for a password:
# 1.- The length must be at least eight characters, otherwise it returns a descriptive error message.
# 2.- The password must have at least two numbers, otherwise it returns a descriptive error message.
# 3.- The password must have at least one capital letter, otherwise it returns a descriptive error message
# 4.- The password must have at least one special character, otherwise it returns a descriptive error message.
# 5.- If the password has more than one error message, the function must return all these messages separated by \n.

import pytest
from password import password_validator


@pytest.mark.parametrize('invalid_length_passwords', ['1234A*', '12345B*', '12346C*'])
def test_show_error_message_when_password_length_is_less_than_eight_char(invalid_length_passwords):
    assert password_validator(invalid_length_passwords) == 'Password length must be greater than 8 characters'


@pytest.mark.parametrize('invalid_numbers_in_password', ['1Aabbccd-', 'tuvWxy-1', '1-passworD'])
def test_show_error_message_when_password_has_less_than_two_numbers(invalid_numbers_in_password):
    assert password_validator(invalid_numbers_in_password) == 'Password must have at least 2 numbers'


@pytest.mark.parametrize('invalid_uppercase_letters_passwords', ['01aa+ccdd', 'mno+pq1234', 'p4ss+w0rd'])
def test_show_error_message_when_password_has_less_than_one_uppercase_letter(invalid_uppercase_letters_passwords):
    assert password_validator(invalid_uppercase_letters_passwords) == 'Password must have at least 1 uppercase letter'


@pytest.mark.parametrize('invalid_special_characters_passwords', ['01Aabbcc', 'HIJKL1234', 'USERn4m3'])
def test_show_error_message_when_password_has_less_than_one_special_character(invalid_special_characters_passwords):
    assert password_validator(invalid_special_characters_passwords) == 'Password must have at least 1 special character'


@pytest.mark.parametrize('invalid_length_and_numbers_in_password', ['1Aabbc-', 'Wxy-1', '1-pasrD'])
def test_show_two_error_messages_related_to_length_and_numbers_in_password(invalid_length_and_numbers_in_password):
    assert password_validator(invalid_length_and_numbers_in_password) == \
           'Password length must be greater than 8 characters' + '\n' + 'Password must have at least 2 numbers'


@pytest.mark.parametrize('valid_passwords', ['0123ABC**', 'T1CT4CT0E+', '-F1zzB0zz-'])
def test_show_error_message_when_password_has_less_than_one_special_character(valid_passwords):
    assert password_validator(valid_passwords) == 'Password accepted'
