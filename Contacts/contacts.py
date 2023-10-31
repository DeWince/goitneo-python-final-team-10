from collections import UserDict
from datetime import datetime
from Contacts.record import Record


class Contacts(UserDict):
    def __init__(self, **config):
        filename = config.get("filename")
        self.data = UserDict()
        # self.database_connector = FileWriter(filename)
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
        
        self.data[record.name] = record
        self.save()
        return record
    # end def
    
    def find_record(self, needle: str):
        results = list()
        for contact in self.data:
            if f"{contact!r}".find(needle) != -1:
                results.append(contact)
            # end if
        # end for
    # end def
    
    def get_record(self, needle: str):
        results = self.find_record(needle)
        if len(results) == 0:
            raise KeyError("Нічого не знайдено")
        elif len(results) > 1:
            raise KeyError("Знайдено забагато результатів")
        # end if
        
        return results[0]
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
        current_date = datetime.now()

        next_birthdays = list()
        for record in list(self.data.values()):
            celebrate_day = record.get_celebrate_date(current_date.year)
            if celebrate_day == None:
                continue
            # end if

            if (celebrate_day > current_date and (celebrate_day - current_date).days <= days):
                next_birthdays.append(record)
            # end if
        # end for
        return next_birthdays
    # end def
# end class




    # def add_record(self, record):
    #     self.data[record.name.value] = record

    # def find(self, name):
    #     return self.data[name]
    

    # def delete(self, name):
    #     if name in self.data:
    #         del self.data[name]
    
    # def save(self):
    #     pass

    # def load(self, filename='phonebook.bin'):
    #     pass
    
    # def get_birthdays(self, days):
    #     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #     result = {day : [] for day in days}
    #     records = []
    #     today = datetime.today().date()

    #     for record in self.data.values():
    #         if(record.birthday == None):
    #             continue

    #         birthday = record.birthday.to_datetime().date()
            
    #         birthday_this_year = birthday.replace(year = today.year) 

    #         if birthday_this_year < today:
    #             birthday_this_year = birthday.replace(year = today.year + 1)

    #         day_of_week = birthday_this_year.weekday()  
    #         delta_days = (birthday_this_year - today).days

    #         if day_of_week == 5: 
    #             day_of_week = 0
    #             delta_days +=2

    #         if day_of_week == 6: 
    #             day_of_week = 0
    #             delta_days +=1

    #         day_name = days[day_of_week]
    #         if delta_days < days:
    #             result[day_name].append(record)

    #     for item in result:
    #         if len(result[item]) > 0:
    #             records.extend(result[item])

    #     return records