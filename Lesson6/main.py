import urwid


def is_very_long(password):
    return len(password) > 12


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


def rating_password(edit, password):
    score = 0
    for function in [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]:
        score += 2 if function(password) else 0
    reply.set_text("Рейтинг пароля: %s" % score)


def main():
    global reply
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', rating_password)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    main()