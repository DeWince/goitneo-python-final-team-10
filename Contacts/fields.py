import re
from datetime import datetime
from Errors.error_handlers import FormatError

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Validatable:
    def is_valid_type(self, value, regex):
        return re.match(regex, value)


class Name(Field):
    pass

class Address(Field):
    pass

class Birthday(Field, Validatable):
    def __init__(self, value, regex):
        self.regex = regex
        if not super().is_valid_type(value, regex):
            raise FormatError("Not correct date, use format DD.MM.YYYY")
        super().__init__(value)
    
    def to_datetime(self):
        return datetime.strptime(self.value, '%d.%m.%Y')
        
    def __str__(self):
        return str(f"{self.value.day}.{self.value.month}.{self.value.year}")

class Phone(Field, Validatable):
    def __init__(self, value, regex):
        self.regex = regex
        if not super().is_valid_type(value, regex):
            raise FormatError("Not correct number, should contain 10 digits")
        super().__init__(value)

class Email(Field, Validatable):
    def __init__(self, value, regex):
        pass