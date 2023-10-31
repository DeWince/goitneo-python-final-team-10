import re
from datetime import datetime
from Errors.error_handlers import FormatError

class Field:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return str(self.value)
    
class Validatable(Field):
    def is_valid_type(self, value):
        return re.fullmatch(self.regex, value)


class Name(Field):
    pass

class Address(Field):
    pass

class Birthday(Validatable):
    regex = r"\d{2}.\d{2}.\d{4}"
    str_format = "%d.%m.%Y"
    
    def __init__(self, value):
        if not super().is_valid_type(value):
            raise FormatError("Incorrect date format, use format DD.MM.YYYY")

        try:
            self.value = datetime.strftime(
                datetime.strptime(
                    value, 
                    self.str_format
                ),
                self.str_format
            )
        except Exception as e:
            raise ValueError("Дата не існує")
        # end try
        # super().__init__(value)
    
    def to_datetime(self):
        return datetime.strptime(self.value, self.str_format)
        
    def __str__(self):
        return str(self.value)

class Phone(Validatable):
    regex = r"\d{10}"
    def __init__(self, value):
        if not super().is_valid_type(value):
            raise FormatError("Incorrect phone number format, should contain 10 digits")
        super().__init__(value)

class Email(Validatable):
    regex = r".+"
    def __init__(self, value):
        if not super().is_valid_type(value):
            raise FormatError("Incorrect email format, should _____")
        super().__init__(value)