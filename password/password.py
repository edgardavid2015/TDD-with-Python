def password_validator(password):
    error_list = []
    if len(password) < 8:
        error_list.append('Password length must be greater than eight characters')

    total_numbers = [digit for digit in password if digit.isnumeric()]
    if len(total_numbers) < 2:
        error_list.append('Password must have at least two numbers')

    total_letters = [char for char in password if char.isupper()]
    if len(total_letters) < 1:
        error_list.append('Password must have at least one uppercase letter')

    total_esp_chars = [char for char in password if not password.isalnum() and not password.isspace()]
    if len(total_esp_chars) < 1:
        error_list.append('Password must have at least one special character')

    if len(error_list) > 0:
        string_errors = '\n'.join(error_list)
        return string_errors
    else:
        return 'Password accepted'
