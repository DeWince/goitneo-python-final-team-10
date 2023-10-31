import calendar
from datetime import datetime
from Contacts.fields import Birthday, Name, Phone, Address, Email

class Record:
    fields = {
        "name": "Контакт",
        "address": "Адреса",
        "emails": "Електронка",
        "phones": "Телефон",
        "birthday": "День народження"
    }
    sets = ["phones", "emails"]

    def __init__(self, name: Name, address: Address = None, phones: set = set(), emails: set = set(), birthday: Birthday = None):
        self.name = name if type(name) == Name else Name(name)
        self.address = address if type(address) == Address else Address(address)
        self.birthday = birthday if type(birthday) == Birthday else Birthday(birthday)
        self.phones = set([phone if type(phone) == Phone else Phone(phone) for phone in phones])
        self.emails = set([email if type(email) == Email else Email(email) for email in emails])
    # end def

    def __str__(self):
        str = f"{self.name:>15}:   "
        if self.birthday != None:
            str += f"{self.fields['birthday']}: {self.birthday:<14}"
        if len(self.phones) > 0:
            str += f"{self.fields['phones']}: {'; '.join(self.phones)}"
        if len(self.emails) > 0:
            str += f"{self.fields['emails']}: {'; '.join(self.emails)}"
        if self.address != None:
            str += f"{self.fields['address']}: {self.address}"
        # end if
        return str
    # end def
    
    def __repr__(self):
        str = f"Record({self.name}, {self.address}, {self.phones}, {self.emails}, {self.birthday}"

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        # end if
    # end def

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
        # end if
    # end def
    
    def add_info(self, type, value):
        if type in self.sets:
            if value in self.__dict__[type]:
                raise KeyError(f"{(self.fields[type])} вже існує")
            # end if
            
            self.__dict__[type].add(value)
        elif type in ["address", "birthday"]:
            self.__dict__[type] = value
        # end if
    # end def
    
    def modify_info(self, type, old_value, new_value):
        if type in self.sets:
            self.delete_info(type, old_value)
        # end if

        self.add_info(type, new_value)
        # end if
    # end def
    
    def delete_info(self, type, value=None):
        if type in self.sets:
            try:
                self.__dict__[type].remove(value)
            except:
                raise KeyError(f"{(self.fields[type])} не знайдено")
            # end try
        elif type == "address":
            del self.__dict__[type]
        # end if
    # end def

    def add_phone(self, phone):
        self.add_info("phone", Phone(phone))
    # end def

    def change_phone(self, old_phone=None, new_phone=None):
        if type(old_phone) == str:
            old_phone = Phone(old_phone)
        if type(new_phone) == str:
            new_phone = Phone(new_phone)
        # end if

        self.modify_info("phones", old_phone, new_phone)
        
        return self
    # end def

    def delete_phone(self, phone):
        if type(phone) == str:
            phone = Phone(phone)
        # end if

        try:
            self.delete_info("phones", phone)
        except:
            pass
        # end try
        
        return self
    # end def

    def add_email(self, email):
        self.add_info("email", Email(email))
    # end def

    def change_email(self, old_email=None, new_email=None):
        if type(old_email) == str:
            old_email = Email(old_email)
        if type(new_email) == str:
            new_email = Email(new_email)
        # end if

        self.modify_info("emails", old_email, new_email)
        
        return self
    # end def

    def delete_email(self, email):
        if type(email) == str:
            email = Email(email)
        # end if

        try:
            self.delete_info("emails", email)
        except:
            pass
        # end try

        return self
    # end def

    def set_birthday(self, birthday):
        if type(birthday) == str:
            birthday = Birthday(birthday)
        # end if
        self.add_info("birthday", birthday)
        
        return self
    # end def

    def set_address(self, address):
        if type(address) == str:
            address = Address(address)
        # end if
        self.add_info("address", address)
        
        return self
    # end def
    
    def get_celebrate_date(self, celebrate_year = None):
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




    # def __init__(self, name):
    #     self.birthday = None
    #     self.name = Name(name)
    #     self.phones = []

    # def add_phone(self, phone):
    #     self.phones.append(Phone(phone))

    # def change_phone(self, old_phone, new_phone):
    #     pass

    # def clear_phone(self, phone):
    #     pass

    # def add_mail(self, mail):
    #     pass

    # def change_mail(self, old_mail, new_mail):
    #     pass

    # def clear_mail(self, phone):
    #     pass

    # def set_birthday(self, birthday):
    #     self.birthday = Birthday(birthday)

    # def set_address(self, address):
    #     pass 

    # def __rep__():
    #     pass

    # def __str__(self):
    #     phones_str = '; '.join(str(p) for p in self.phones)
    #     return f"Contact name: {self.name}, birthday: {self.birthday}, phones: {phones_str}"
