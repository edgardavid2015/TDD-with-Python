def password_validator(password):
    error_list = []
    if len(password) < 8:
        error_list.append('Password length must be greater than 8 characters')

    total_numbers = [digit for digit in password if digit.isnumeric()]
    if len(total_numbers) < 2:
        error_list.append('Password must have at least 2 numbers')

    total_letters = [char for char in password if char.isupper()]
    if len(total_letters) < 1:
        error_list.append('Password must have at least 1 uppercase letter')

    total_esp_chars = [char for char in password if not password.isalnum() and not password.isspace()]
    if len(total_esp_chars) < 1:
        error_list.append('Password must have at least 1 special character')

    if len(error_list) > 0:
        string_errors = '\n'.join(error_list)
        return string_errors
    else:
        return 'Password accepted'
