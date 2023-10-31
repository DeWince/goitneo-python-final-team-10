
from Contacts.contacts import Contacts
from Contacts.record import Record
from Errors.error_handlers import address_args_error, birth_args_error, contacts_search_args_error, email_args_error, input_error, note_search_args_error, phone_args_error
from Notes.notes import Notes

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name = args[0]
    if not contacts.contains(name):
        record = Record(name)
    else:
        record = contacts.find(name)
    contacts.add_record(record)
    return "Contact added."

@contacts_search_args_error
@input_error
def find_contact(args, contacts):
    pass

@input_error
def delete_contact(args, contacts):
    pass

@phone_args_error
@input_error
def add_phone(args, contacts):
    pass

@phone_args_error
@input_error
def change_phone(args, contacts):
    pass

@phone_args_error
@input_error
def delete_phone(args, contacts):
    pass

@email_args_error
@input_error
def add_mail(args, contacts):
    pass

@email_args_error
@input_error
def change_mail(args, contacts):
    pass

@email_args_error
@input_error
def delete_mail(args, contacts):
    pass

@birth_args_error
@input_error
def set_birthday(args, contacts):
    name, bithday = args
    record = contacts.find(name)
    record.add_birthday(bithday)
    return "Bithday changed."

@input_error
def get_birthdays(contacts):
    records = contacts.get_birthdays()
    if len(records) <= 0:
        return "No birthdays next week"
    return "Birthdays next week:\n" + "\n".join(map(str, records))

@address_args_error
@input_error
def set_address(args, contacts):
    pass

@input_error
def add_note(args, notes):
    pass

@note_search_args_error
@input_error
def find_note(args, notes):
    pass

@input_error
def delete_note(args, notes):
    pass

@input_error
def get_all(contacts):
    if len(contacts) == 0:
        return "No contacts yet, please use 'add' command to add them"
    return "".join(map(lambda x : f"{x}: {contacts[x]}\n", contacts))

def hello_response():
    return "How can I help you?"


def main():
    contacts = Contacts()
    notes = Notes()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello_response())
        #add commands
        else:
            print("""Invalid command. Use one of following: 
'hello', 'close', 'exit'""")

if __name__ == "__main__":
    main()