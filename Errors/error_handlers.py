class FormatError(ValueError):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FormatError as e:
            return "\n".join(e.args)
        except IndexError or KeyError:
            return "Incorrect args, provide name"

    return inner

def contacts_search_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note title and its content"
        except IndexError or KeyError:
            return "Incorrect args, provide search string"

    return inner

def phone_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def birth_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and birth date, use format DD.MM.YYYY"

    return inner

def address_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and address date"

    return inner

def email_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and valid email"

    return inner

def note_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note title and its content"

    return inner

def note_search_args_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note title and its content"
        except IndexError or KeyError:
            return "Incorrect args, provide search string"

    return inner