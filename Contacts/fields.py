import re
from datetime import datetime
from Errors.error_handlers import FormatError

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __eq__(self, new):
        return str(self) == str(new)
    
class Validatable:
    def is_valid_type(self, value, regex):
        return re.fullmatch(regex, value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Address(Field):
    def __init__(self, value):
        self.value = value

class Birthday(Field, Validatable):
    def __init__(self, value):
        self.regex = r"\d{1,2}[-,.:/]\d{1,2}[-,.:/]\d{4}"
        if not super().is_valid_type(value, self.regex):
            raise FormatError("Not correct date")
        date = re.search(r"\d{1,2}[-,.:/]\d{1,2}[-,.:/]\d{4}", value)
        date_formated = re.sub(r"[-,:/]", '.', date.group())
        try:
            datetime.strptime(date_formated, "%d.%m.%Y")
            super().__init__(date_formated)
        except:
            FormatError("Not correct date")
    
    def to_datetime(self):
        return datetime.strptime(self.value, '%d.%m.%Y')
        
    def __str__(self):
        return str(f"{self.value.day}.{self.value.month}.{self.value.year}")

class Phone(Field, Validatable):
    def __init__(self, value):
        self.regex = r"\d{10}"
        if not super().is_valid_type(value, self.regex):
            raise FormatError("Not correct number, should contain 10 digits")
        super().__init__(value)

    def __str__(self):
        return str(self.value)

class Email(Field, Validatable):
    def __init__(self, value):
        self.regex = r"[a-zA-Z]{1}[a-zA-Z0-9_.]+[@]{1}[a-zA-z]+[.][a-zA-z]{1}[a-zA-z]+"
        if not super().is_valid_type(value, self.regex):
            raise FormatError("Not correct e-mail address")
        super().__init__(value)

    def __str__(self):
        return str(self.value)
