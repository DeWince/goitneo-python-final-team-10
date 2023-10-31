import calendar
from datetime import datetime
from Contacts import Birthday, Name, Phone, Address, Email


class Record:
    fields = {
        "name": "Контакт",
        "address": "Адреса",
        "emails": "Електронка",
        "phones": "Телефон",
        "birthday": "День народження"
    }
    sets = ["phones", "emails"]

    def __init__(self, name: Name):
        self.name = str(name)
        self.address = None
        self.birthday = None
        self.phones = set()
        self.emails = set()
    # end def

    def __str__(self):
        return_string = []
        if self.birthday != None:
            return_string.append(
                f"{self.fields['birthday']}: {str(self.birthday):<10}")
        if len(self.phones) > 0:
            return_string.append(
                f"{self.fields['phones']}: {'; '.join(self.phones)}")
        if len(self.emails) > 0:
            return_string.append(
                f"{self.fields['emails']}: {'; '.join(self.emails)}")
        if self.address != None:
            return_string.append(
                f"{self.fields['address']}: {str(self.address)}")
        # end if

        if len(return_string) == 0:
            return_string = ["данні відсутні"]
        # end if

        return_string = f"{(str(self.name)):>15}:  {(' | '.join(return_string))}"
        return return_string
    # end def

    def __repr__(self):
        name = self.name
        address = self.address or None
        birthday = self.birthday or None
        phones = ";".join(self.phones) if len(self.phones) else None
        emails = ";".join(self.emails) if len(self.emails) else None
        data_stream = [value for value in [name, address,
                                           birthday, phones, emails] if value != None]

        return_string = f"{(','.join(data_stream))}"
        return return_string

    def __getitem__(self, key):
        key = str(key)
        if key in self.__dict__:
            return self.__dict__[key]
        # end if
    # end def

    def __setitem__(self, key, value):
        key = str(key)
        value = str(value)
        if key in self.__dict__:
            self.__dict__[key] = value
        # end if
    # end def

    def add_info(self, type, value):
        value = str(value)
        if type in self.sets:
            if value in self.__dict__[type]:
                raise KeyError(f"{(self.fields[type])} вже існує")
            # end if

            self.__dict__[type].add(value)
        elif type in ["address", "birthday"]:
            self.__dict__[type] = value
        # end if

        return True
    # end def

    def modify_info(self, type, old_value, new_value):
        if type in self.sets:
            new_value = str(new_value)

            if old_value not in self.__dict__[type]:
                raise KeyError("Запис не існує")
            if new_value in self.__dict__[type]:
                raise KeyError("Новий запис вже існує")
            # end if

            self.add_info(type, new_value)
            self.delete_info(type, old_value)
        # end if

        return True
    # end def

    def delete_info(self, type, value):
        value = str(value)
        if type in self.sets:
            try:
                if value == "all":
                    self.__dict__[type] = set()
                else:
                    self.__dict__[type].remove(value)
                # end if
            except:
                raise KeyError(f"{(self.fields[type])} не знайдено")
            # end try
        elif type == "address":
            del self.__dict__[type]
        # end if

        return True
    # end def

    def add_phone(self, phone):
        self.add_info("phones", Phone(phone))

        return self
    # end def

    def change_phone(self, old_phone, new_phone):
        self.modify_info("phones", old_phone, Phone(new_phone))

        return self
    # end def

    def clear_phone(self, phone):
        try:
            self.delete_info("phones", phone)
        finally:
            return self
        # end try

        return self
    # end def

    def add_mail(self, email):
        self.add_info("emails", Email(email))

        return self
    # end def

    def change_mail(self, old_email, new_email):
        self.modify_info("emails", old_email, Email(new_email))

        return self
    # end def

    def clear_mail(self, email):
        try:
            self.delete_info("emails", email)
        finally:
            return self
        # end try

        return self
    # end def

    def set_address(self, address):
        self.add_info("address", str(Address(address)))

        return self
    # end def

    def set_birthday(self, birthday):
        self.add_info("birthday", str(Birthday(birthday)))

        return self
    # end def

    def get_celebrate_date(self, celebrate_year=None):
        if self.birthday == None:
            return
        if celebrate_year == None:
            celebrate_year = datetime.now().year
        # end if

        is_leap = calendar.isleap(celebrate_year)
        bday = datetime.strptime(self.birthday, "%d.%m.%Y")
        month = bday.month
        day = bday.day
        if (month == 2 and day == 29 and not is_leap):
            day = 28
        # end if

        return datetime(
            year=celebrate_year,
            month=month,
            day=day
        ).date()
    # end def
# end class
