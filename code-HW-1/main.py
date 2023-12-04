def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(contacts, args):
    if len(args) < 2:
        return False
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def verify_contact(contacts, args):
    if len(args) < 2:
        return False
    name, phone = args
    if name in contacts:
        return True
    return False

def change_contact(contacts, args):
    if not verify_contact(contacts, args):
        return False
    name, phone = args
    contacts[name] = phone 
    return True
       
def show_phone(contacts, name):
    if name not in contacts:
        return False
    
    return contacts[name]
        
    
def show_all(contacts):
    if not contacts:
        print("No contacts saved.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def print_supported_commands():
    print(f"To add a contact, use command 'Add'.\n"
      f"To end assistant, use command 'Close'.\n"
      f"To change contact, use command 'Change'.\n"
      f"To see a phone and a name, use command 'phone name'.\n"
      f"To see all saved names and phones, use command 'All'.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "stop"]:
            print("Good bye!")
            break

        elif command in ["hello", "hi", "wazzup", "morning", "greetings" ]:
            print("How can I help you?")
        elif command in ["add", "new contact", "new name"]:
            if verify_contact(contacts, args):
                print(f"The contact is already exists")

            elif add_contact(contacts, args):
                print(f"Contact was successfully added")
            else:
                print(f"Contact was not added")
        elif command == "change":
            if verify_contact(contacts, args):    
                if change_contact(contacts, args):
                    print(f"The contact {args[0]} has been changed successfully")
                else:
                    print(f"The contact {args[0]} hasn't been changed")
        elif command == "phone" and args[0]:
            if phone := show_phone(contacts, args[0]):
                print(f"{args[0]}: {phone}")
            else:
                print(f"There is no such contact")

        elif command in ["all", "everybody"]:
            show_all(contacts)   


        elif command in ['?', 'help', 'how']:
            print_supported_commands()
        else:

            print("Invalid command.")
            print_supported_commands()


if __name__ == "__main__":
    main()