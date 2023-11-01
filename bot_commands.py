from Contacts import Record
from Errors import address_args_error, birth_args_error, contacts_search_args_error, email_args_error, input_error, note_search_args_error, phone_args_error
from Notes import Note


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(contacts, args):
    '''
        # Name is not unique identifier, so I'm not sure why we search for contact by name
        if not contacts.contains(name):
            record = Record(name)
        else:
            record = contacts.get_record(name)
        # Why are we trying to add already existing contact to contact book?
        contacts.add_record(record)
        return "Contact added."
    '''
    name = args[0]
    contacts.add_record(Record(name))
    return "Contact added."


@contacts_search_args_error
@input_error
def find_contact(contacts, args):
    # Returns records that have "search_by" in name, address, email or phone.
    # We can move this code to contacts.get_record() method
    search_by = args[0]
    records = contacts.find_record(search_by)    # changed method

    if records:
        # updated output
        return "Search results:\n" + "\n".join(str(record) for record in records)
    return f"Contact with attribute {search_by} not found!"


@input_error
def delete_contact(contacts, args):
    # I think Contacts delete command should return str with result of
    # deletion operation: Contact deleted or Contact {name} not in contacts.
    name = args[0]
    # will return True if successful, or raise an error
    contacts.delete_record(name)
    return "Contact deleted"


@phone_args_error
@input_error
def add_phone(contacts, args):
    name, *phones = args
    record = contacts.get_record(name)
    for phone in phones:    # BUG: if a phone throws an error, all following phones are not added
        record.add_phone(phone)
    return f"Phones added.\n{record}"


@phone_args_error
@input_error
def change_phone(contacts, args):
    name, old_phone, new_phone = args
    record = contacts.get_record(name)
    record.change_phone(old_phone, new_phone)
    return f"Phone changed.\n{record}"    # removed 's'


@phone_args_error
@input_error
def delete_phone(contacts, args):
    name, phone = args
    record = contacts.get_record(name)
    record.clear_phone(phone)   # changed method
    return f"Phone deleted.\n{record}"    # removed 's'


@phone_args_error
@input_error
def delete_all_phone(contacts, args):
    name = args[0]
    record = contacts.get_record(name)
    record.clear_phone("all")    # changed method
    return f"All phones deleted.\n{record}"


@email_args_error
@input_error
def add_email(contacts, args):
    name, email = args
    record = contacts.get_record(name)
    record.add_mail(email)    # changed method
    return f"Email added.\n{record}"    # removed 's'


@email_args_error
@input_error
def change_email(contacts, args):
    name, old_email, new_email = args
    record = contacts.get_record(name)
    record.change_mail(old_email, new_email)    # changed method
    return f"Email changed.\n{record}"


@email_args_error
@input_error
def delete_email(contacts, args):
    name, email = args
    record = contacts.get_record(name)
    record.clear_mail(email)  # changed method
    return f"Email deleted.\n{record}"  # removed 's'


@email_args_error
@input_error
def delete_all_email(contacts, args):
    name = args[0]
    record = contacts.get_record(name)
    record.clear_mail("all")    # changed method
    return f"All emails deleted.\n{record}"


@birth_args_error
@input_error
def set_birthday(contacts, args):
    name, birthday = args
    record = contacts.get_record(name)
    record.set_birthday(birthday)    # changed method
    return f"Birthday changed.\n{record}"


@input_error
def get_birthdays(contacts, args):

    # added parameter how many days ahead to look for birthdays
    days = int(args[0]) if (len(args) and str(args[0]).isdigit()) else 7
    records = contacts.get_birthdays(days)
    if len(records) <= 0:
        return "No birthdays next week"
    return "Birthdays next week:\n" + "\n".join(map(str, records))


@input_error
def delete_birthday(contacts, args):
    name = args[0]
    record = contacts.get_record(name)
    record.set_birthday()    # changed method
    return f"Birthday deleted.\n{record}"


@address_args_error
@input_error
def set_address(contacts, args):
    name, *address = args   # allow address to contain spaces
    record = contacts.get_record(name)
    record.set_address(" ".join(address))  # return spaces
    return f"Address changed.\n{record}"


def get_all_contacts(contacts, *args):
    if not contacts.values():
        return "No contacts yet, please use 'add' command to add them"
    return "\n".join(str(record) for record in contacts.values())


@input_error
def add_note(notes, args):
    note_text = args[0]

    # formatting
    notes.add_note(Note(
        title=f"{note_text[:10]}..." if len(note_text) > 10 else note_text,
        text=note_text
    ))
    return "Note added."


@note_search_args_error
@input_error
def find_note(notes, args):
    search_by = args[0]
    return notes.find_record(search_by)


@note_search_args_error
@input_error
def edit_note(notes, args):
    title, new_text = args
    notes.edit_note(title, new_text)
    return "Note edited."


@input_error
def delete_note(notes, args):
    title = args[0]
    notes.delete(title)
    return "Note deleted."


@input_error
def delete_all_note(notes, args):
    notes.__dict__ = None
    return "All notes deleted."


@input_error
def get_all_notes(notes, *args):
    if not notes.values():
        return "No notes yet, please use 'add' command to add them"
    return "\n".join(str(note) for note in notes.values())


CONTACTS_COMMANDS = {
    "add-contact": add_contact,
    "find-contact": find_contact,
    "delete-contact": delete_contact,
    "add-phone": add_phone,
    "change-phone": change_phone,
    "delete-phone": delete_phone,
    "delete-all-phone": delete_all_phone,
    "add-email": add_email,
    "change-email": change_email,
    "delete-email": delete_email,
    "delete-all-email": delete_all_email,
    "set-birthday": set_birthday,

    # changed command
    "get-birthdays": get_birthdays,
    "delete-birthday": delete_birthday,
    "set-address": set_address,
    "all-contacts": get_all_contacts
}


NOTES_COMMANDS = {
    "add-note": add_note,
    "find-note": find_note,
    "edit-note": edit_note,
    "delete-note": delete_note,
    "delete-all-note": delete_all_note,
    "all-notes": get_all_notes
}


COMMANDS_SYNTAX = {
    "add-contact": "add-contact <name>",
    "find-contact": "find-contact <search input>",
    "delete-contact": "delete-contact <name>",
    "add-phone": "add-phone <name> <phones>",
    "change-phone": "change-phone <name> <old_phone> <new_phone>",
    "delete-phone": "delete-phone <name> <phone>",
    "delete-all-phone": "delete-all-phone <name>",
    "add-email": "add-email <name> <email>",
    "change-email": "change-email <name> <old_email> <new_email>",
    "delete-email": "delete-email <name> <email>",
    "delete-all-email": "delete-all-email <name>",
    "set-birthday": "set-birthday <name> <birthday>",

    # changed command and syntax
    "get-birthdays": "get-birthdays <days>",
    "delete-birthday": "delete-birthday <name>",
    "set-address": "set-address <name> <address>",
    "all-contacts": "all-contacts",
    "add-note": "add-note <text>",
    "find-note": "find-note <title>",
    "edit-note": "edit-note <title> <new-text>",
    "delete-note": "delete-note <title>",
    "delete-all-note": "delete-all-note",
    "all-notes": "all-notes"
}
