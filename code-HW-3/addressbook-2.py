from collections import UserDict

from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.name_value = self.value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone_number = self.validate_phone()

    def validate_phone(self):
        if self.value.isdigit() and len(self.value) == 10:  
            return self.value
        else:
            raise Exception("The phone format is not correct.")  
        
class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def add_phone(self, phone):
        number = Phone(phone)
        self.phones.append(number)

    def add_birthday(self, name, birthday):
        print(f"birthday->> {name}, {birthday}")
        if self.birthday is None:
            if name and self.is_valid_birthday(birthday):
                self.birthday = birthday
                return f"Birthday added for {name}"
            else:
                return f"Invalid birthday format. The birthday date format must be DD-MM-YYYY."
        else:
            return f"A birthday date is already exists for this contact."
        
    def is_valid_birthday(self, birthday):
        format_str = "%d-%m-%Y" #format string
        try:
            datetime.strptime(birthday, format_str)
            return True
        except ValueError:
            return False

    def remove_phone(self, phone):
        for idx, phone_num in enumerate(self.phones):
            if phone_num.value == phone:
                del self.phones[idx]
                return f"The phone {phone} has been removed."
        return f"The phone has not been found."
        
    def edit_phone(self, old_phone, new_phone):
        for phone_num in self.phones:
            if phone_num.value == old_phone:
                phone_num.value = new_phone
                return f"Phone number {old_phone} updated to {new_phone} for contact {self.name.value}"
        return f"Phone number {old_phone} has not been found."

    def find_phone(self, phone):
        for phone_num in self.phones:
            if phone_num.value == phone:
                return f"Phone number {phone} found for the contact {self.name.value}"
        return f"Phone number {phone} hasn't been found for the contact {self.name.value}"
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}" 

class AddressBook(UserDict):
    
    def add_record(self, name, phone):
        if name not in self.data:
            record = Record(name)
            record.add_phone(phone) 
            #print 
            self.data[name] = record
            return f"Contact {name} added to the address book"
        else:
            return f"Contact {name} already exists in the address book"
        
    def delete(self, name):
        if name in self:
            del self[name]
            return f"Contact {name} was successfuly deleted."
        else:
            return f"Contact {name} wasn't found"

    def find(self, name):
        if name in self:
            return f"Contact {name} found in the address book." # print all the info
        else:
            return f"Contact {name} wasn't found in the address book."
        
    def get_birthdays_per_week(self):
        today = datetime.today().date()
        birthdays_per_day = {}

        week = ('Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday' 
        )

        for name in self.data.values():
            name = name["name"]
            birthday = name["birthday"].date()  # date type conversion
            birthday_this_year = birthday.replace(year=today.year) 
         
            delta_days = (birthday_this_year - today).days

            if delta_days <= 7:
                day = week[birthday.weekday()]
                if birthday.weekday() >= 5: 
                    birthdays_per_day['Monday'].append(name)
                else:
                    birthdays_per_day[day].append(name)    
            
            elif birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            if birthday.weekday() == 5 or birthday.weekday() == 6:
                pass

        for day, names in birthdays_per_day.items():
            print(f"{day}: {', '.join(names)}")
 


 

