from addressbook import AddressBook

from addressbook import Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    print(f'parser->>> {cmd} - {args}')
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        if len(args) < 2:
            return "Contact is in the wrong format. Provide <name> and <phone number>"
        try:
            return func(*args, **kwargs)
        except ValueError:
           return "Contact was not added. Type in a name and a phone number."
        except (KeyError, IndexError):
            return "There is no such contact! To add contact use command 'Add'." 
    return inner

@input_error
def add_contact(book, args):
    print(f'add contact->>> {args}')
    name, phone = args
    book.add_record(name, phone)
    return f"Contact added."

def verify_contact(book, args):  # an inside func
    if len(args) < 2:
        return False
    name, phone = args
    if name in book.data:
        return True
    return False

@input_error
def change_contact(book, args):
    if not verify_contact(book, args):
        return f"There is no such contact! To add contact use command 'Add'."
    name, phone = args
    book[name] = phone 
    return f"The contact {args[0]} has been changed successfully"
      
def show_phone(book, name):
    if name not in book.data:
        return "There is no such contact"
    return f"{name}: {book[name]}"

def show_birthday(book, name):
    if name not in book.data:
        return "There is no such contact"
    return f"{name}: {book.data[name]['birthday']}" 
  
def show_all(book):     
    if not book:
        print("No contacts saved.")
    else:
        for name, record in book.items():
            birthday = record.birthday
            phones = record.phones
            print(f"{name}: {phones}, Birthday {birthday}.")

def print_supported_commands():
    print(f"To add a phone number, use command 'Add phone <name> <phone>'.\n"
      f"To end assistant, use command 'Close'.\n"
      f"To change contact, use command 'Change name new_phone. '.\n"
      f"To see a phone and a name, use command 'phone name'.\n"
      f"To see all saved names and phones, use command 'All'.")
    
def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("No command entered. Please provide a command.")
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "stop"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi", "wazzup", "morning", "greetings" ]:
            print("How can I help you?")

        elif command in ["add-phone", "new-contact", "new-name"]:
            if verify_contact(book, args):
                print(f"The contact is already exists")
            else:
                print(add_contact(book, args))    
        elif command in ["change", "change-contact"]:
            print(change_contact(book, args))



        elif command == "show-birthday" and args[0]:
            print(show_birthday(book, args[0]))

        elif command == "birthdays":
            book.get_birthdays_per_week()   #?

            # for day, names in birthdays_per_day.items():
      #  print(f"{day}: {', '.join(names)}")  ??

        elif command == "add-birthday":
            while True:
                if len(args) < 2:
                    print(f"add-birthday must be <name> <DD-MM-YYYY>")
                    user_input = input("Enter command: ")
                    command, *args = parse_input(user_input) 
                else:
                    name, birthday = args
                    if name in book.data:
                        print(book.data[name].add_birthday(name, birthday))
                    else:
                        new_record = Record(name)
                        print(new_record.add_birthday(name, birthday))
                    break
             #  ? book.add_record(name, new_record)
        
                  
            #how to make it work and print "Birthday Added"



        elif command == "phone" and args[0]:
            print(show_phone(book, args[0]))
        elif command in ["all", "everybody"]:
            show_all(book.data)   
        elif command in ['?', 'help', 'how']:
            print_supported_commands()
        else:
            print("Invalid command.")
            print_supported_commands()


if __name__ == "__main__":
    main()