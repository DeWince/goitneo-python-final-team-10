from Contacts.fields import Birthday, Name, Phone


class Record:
    def __init__(self, name):
        self.birthday = None
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        pass

    def clear_phone(self, phone):
        pass

    def add_mail(self, mail):
        pass

    def change_mail(self, old_mail, new_mail):
        pass

    def clear_mail(self, phone):
        pass

    def set_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def set_address(self, address):
        pass 

    def __rep__():
        pass

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, birthday: {self.birthday}, phones: {phones_str}"
