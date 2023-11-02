class FormatError(ValueError):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FormatError as e:
            return "\n".join(e.args)
        except (IndexError, KeyError) as e:
            return '\n'.join(e.args) if len(e.args) else "Incorrect args, provide a name"

    return inner


def contacts_search_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a note title and its content"
        except (IndexError, KeyError) as e:
            return "\n".join(e.args) if len(e.args) else "Incorrect args, provide a search string"

    return inner


def phone_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and a phone please."

    return inner


def birth_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and a birth date, use format DD.MM.YYYY"

    return inner


def address_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and an address"

    return inner


def email_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and a valid email"

    return inner


def note_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a note title and text"

    return inner


def note_search_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a note title and text"
        except (IndexError, KeyError) as e:
            return '\n'.join(e.args) if len(e.args) else "Incorrect args, provide a search string"

    return inner
