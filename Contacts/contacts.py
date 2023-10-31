from collections import UserDict
from datetime import datetime


class Contacts(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]
    

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def save(self):
        pass

    def load(self, filename='phonebook.bin'):
        pass
    
    def get_birthdays(self, days):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        result = {day : [] for day in days}
        records = []
        today = datetime.today().date()

        for record in self.data.values():
            if(record.birthday == None):
                continue

            birthday = record.birthday.to_datetime().date()
            
            birthday_this_year = birthday.replace(year = today.year) 

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year = today.year + 1)

            day_of_week = birthday_this_year.weekday()  
            delta_days = (birthday_this_year - today).days

            if day_of_week == 5: 
                day_of_week = 0
                delta_days +=2

            if day_of_week == 6: 
                day_of_week = 0
                delta_days +=1

            day_name = days[day_of_week]
            if delta_days < days:
                result[day_name].append(record)

        for item in result:
            if len(result[item]) > 0:
                records.extend(result[item])

        return records