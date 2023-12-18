class Test:
    def echo(self):
        print("hello")



Test().echo()


def add_record(self, name, phone):
        if name not in self.data:
            record = Record(name)
            record
            self.data[name] = record
            self.data[name][record]['phones'].append(phone)
            return f"Contact {name} added to the address book"
        else:
            return f"Contact {name} already exists in the address book"
        


       

# Creating a new address book
book = AddressBook() 

# Creating John record
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John record to the Address book
book.add_record(john_record)

# Creating and adding a new Jane record
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Printing out all the data in the Address book
for name, record in book.data.items():
    print(record)

# Printing out Contact name: John, phones: 1112223333; 5555555555
print(john_record)  

john_record.edit_phone("1234567890", "1112223333")
print(john_record)
print(AddressBook)
