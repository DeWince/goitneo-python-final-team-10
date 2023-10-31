from collections import UserDict
from datetime import datetime
from Contacts.record import Record
from Writers.FileWriter import FileWriter


class Contacts(UserDict):
    def __init__(self, **kwargs):
        filename = kwargs.get("filename")
        self.data = UserDict()
        self.database_connector = FileWriter(filename)
        self.load()
    # end def

    def save(self):
        self.database_connector.save(self.data)
    # end def

    def load(self):
        self.data = UserDict(self.database_connector.load())
    # end def

    def add_record(self, record: Record):
        if self.data.get(record.name, None):
            raise KeyError(f"{record.name} вже існує")
        # end if

        self.data[str(record.name)] = record
        self.save()
        return record
    # end def

    def find_record(self, needle: str):
        results = list()
        for record in self.data.values():
            representational_contact = repr(record)
            if representational_contact.find(needle) != -1:
                results.append(record)
            # end if
        # end for
        return results
    # end def

    def get_record(self, needle: str):
        try:
            return self.data[needle]
        except:
            raise KeyError("Контакт не знайдено")
        # end try
    # end def

    def delete_record(self, name: str):
        try:
            res = self.data.pop(name)
            self.save()
            return res
        except:
            raise KeyError("Контакт не знайдено")
        # end try
    # end def

    def get_birthdays(self, days: int = 7):
        days = int(days)
        current_date = datetime.now().date()

        next_birthdays = list()
        for record in list(self.data.values()):
            celebrate_day = record.get_celebrate_date(current_date.year)
            if celebrate_day == None:
                continue
            # end if

            celebrate_in_future = celebrate_day >= current_date
            celebrate_soon = (celebrate_day - current_date).days <= days

            if celebrate_in_future and celebrate_soon:
                next_birthdays.append(record)
            # end if
        # end for
        return next_birthdays
    # end def
# end class
