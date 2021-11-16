def password_validator(password):
    if len(password) < 8:
        return 'Password length must be greater than 8 characters'
    return 'Password accepted'
