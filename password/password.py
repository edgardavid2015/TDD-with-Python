def password_validator(password):
    if len(password) < 8:
        return 'Password length must be greater than 8 characters'
    total_numbers = [digit for digit in password if digit.isnumeric()]
    if len(total_numbers) < 2:
        return 'Password must have at least 2 numbers'
    total_letters = [char for char in password if char.isupper()]
    if len(total_letters) < 1:
        return 'Password must have at least one uppercase letter'
    return 'Password accepted'


def verify_char(char):
    if char.isupper():
        return print('letra')
    else:
        return print('numero')


def main():
    verify_char('A')
    verify_char('a')
    verify_char('1')
    password_validator('1234AbcD')


main()
