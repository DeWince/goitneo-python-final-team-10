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


class Validatable(Field):
    def is_valid_type(self, value, regex):
        return re.fullmatch(regex, value)


class Name(Field):
    def __init__(self, value):
        self.value = value


class Address(Field):
    def __init__(self, value):
        self.value = value


class Birthday(Validatable):
    date_format = "%d.%m.%Y"

    def __init__(self, value):
        self.regex = r"\d{1,2}[-,.:/]\d{1,2}[-,.:/]\d{4}"
        if not super().is_valid_type(value, self.regex):
            raise FormatError("Date is not valid")
        date = re.search(r"\d{1,2}[-,.:/]\d{1,2}[-,.:/]\d{4}", value)
        date_formated = re.sub(r"[-,:/]", '.', date.group())
        try:
            self.to_datetime(date_formated)
            super().__init__(date_formated)
        except:
            FormatError("Date is not valid")

    @classmethod
    def to_datetime(cls, value):
        return datetime.strptime(value, cls.date_format)


class Phone(Validatable):
    def __init__(self, value):
        self.regex = r"\d{10}"
        if not super().is_valid_type(value, self.regex):
            raise FormatError("Number should contain only 10 digits")
        super().__init__(value)


class Email(Validatable):
    def __init__(self, value):
        self.regex = r"[a-zA-Z]{1}[a-zA-Z0-9_.]+[@]{1}[a-zA-z]+[.][a-zA-z]{1}[a-zA-z]+"
        if not super().is_valid_type(value, self.regex):
            raise FormatError("Email is not valid")
        super().__init__(value)
