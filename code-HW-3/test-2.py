from addressbook import AddressBook



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(book, args):
    if len(args) < 2:
        return "Contact was not added. The contact must be: <name phone number>"
    name, phone = args
    book.add_record(name)          
    return "Contact added."

def verify_contact(book, args):
    if len(args) < 2:
        return False
    name, phone = args
    if name in book:
        return True
    return False

def change_contact(book, args):
    if len(args) < 2:
        return f"To change the contact provide the existing name and a new phone. "
    if not verify_contact(book, args):
        return f"There is no such contact! To add contact use command 'Add'."
    name, phone = args
    book[name] = phone 
    return f"The contact {args[0]} has been changed successfully"
       
def show_phone(book, name):
    if name not in book:
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
        for name, phone in book.items():
            print(f"{name}: {phone}")


def print_supported_commands():
    print(f"To add a contact, use command 'Add name phone'.\n"
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
        elif command in ["add", "new contact", "new name"]:
            if verify_contact(book, args):
                print(f"The contact is already exists")
            print(add_contact(book, args))    
        elif command in ["change", "change contact"]:
            print(change_contact(book, args))



        elif command == "show birthday" and args[0]:
            print(show_birthday(book, args[0]))

        elif command == "birthdays":
            print(get_birthdays_per_week())




        elif command == "phone" and args[0]:
            print(show_phone(book, args[0]))
        elif command in ["all", "everybody"]:
            show_all(book)   
        elif command in ['?', 'help', 'how']:
            print_supported_commands()
        else:
            print("Invalid command.")
            print_supported_commands()


if __name__ == "__main__":
    main()