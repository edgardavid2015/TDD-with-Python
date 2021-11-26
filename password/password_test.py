# Apply the TDD methodology to create a validation function for a password:
# 1.- The length must be at least eight characters, otherwise it returns a descriptive error message.
# 2.- The password must have at least two numbers, otherwise it returns a descriptive error message.
# 3.- The password must have at least one capital letter, otherwise it returns a descriptive error message
# 4.- The password must have at least one special character, otherwise it returns a descriptive error message.
# 5.- If the password has more than one error message, the function must return all these messages separated by \n.

import pytest
from password import password_validator


@pytest.mark.parametrize('test_password', ['1234A*', '12345B*', '12346C*'])
def test_show_error_message_when_password_length_is_less_than_eight_char(test_password):
    assert password_validator(test_password) == 'Password length must be greater than eight characters'


@pytest.mark.parametrize('test_password', ['1Aabbccd-', 'tuvWxy-1', '1-passworD'])
def test_show_error_message_when_password_has_less_than_two_numbers(test_password):
    assert password_validator(test_password) == 'Password must have at least two numbers'


@pytest.mark.parametrize('test_password', ['01aa+ccdd', 'mno+pq1234', 'p4ss+w0rd'])
def test_show_error_message_when_password_has_less_than_one_uppercase_letter(test_password):
    assert password_validator(test_password) == 'Password must have at least one uppercase letter'


@pytest.mark.parametrize('test_password', ['01Aabbcc', 'HIJKL1234', 'USERn4m3'])
def test_show_error_message_when_password_has_less_than_one_special_character(test_password):
    assert password_validator(test_password) == 'Password must have at least one special character'


@pytest.mark.parametrize('test_password', ['1abbc', 'wxy7', '9pasr'])
def test_show_all_error_messages_separated_by_new_line_character(test_password):
    assert password_validator(test_password) == \
           'Password length must be greater than eight characters' + '\n' + \
           'Password must have at least two numbers' + '\n' + \
           'Password must have at least one uppercase letter' + '\n' + \
           'Password must have at least one special character'


@pytest.mark.parametrize('test_password', ['0123ABC**', 'T1CT4CT0E+', '-F1zzB0zz-'])
def test_show_accepted_message_when_password_is_correct(test_password):
    assert password_validator(test_password) == 'Password accepted'
