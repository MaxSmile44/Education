def is_very_long(password):
    return True if len(password) > 12 else False

def has_digit(password):
    return any(letter.isdigit() for letter in password)

def has_letters(password):
    return any(letter.isalpha() for letter in password)

def has_upper_letters(password):
    return any(letter.isupper() for letter in password)

def has_lower_letters(password):
    return any(letter.islower() for letter in password)

def has_symbols(password):
    return any(not letter.isalnum() for letter in password)

def rating_password(password):
    score = 0
    for function in [is_very_long, has_digit, has_letters, has_upper_letters, has_lower_letters, has_symbols]:
        score += 2 if function(password) else 0
    return score


if __name__ == '__main__':
    password = input('Введите пароль: ')
    print(f'Рейтинг пароля: {rating_password(password)}')