from Contacts.record import Record
from Errors.error_handlers import address_args_error, birth_args_error, contacts_search_args_error, email_args_error, input_error, note_search_args_error, phone_args_error
from Notes.note import Note


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
            record = contacts.find(name)
        # Why are we trying to add already existing contact to contact book?
        contacts.add_record(record)
        return "Contact added."
    '''
    name = args[0]
    if not contacts.find(name):
        contacts.add_record(Record(name))
        return "Contact added."
    return "Contact already exists."


@contacts_search_args_error
@input_error
def find_contact(contacts, args):
    # Returns records that have "search_by" in name, address, email or phone.
    # We can move this code to contacts.find() method
    search_by = args[0]
    records = []
    for name, record in contacts.values():
        if search_by in name:
            records.append(record)
        elif search_by in record.address.value:
            record.append(record)
        elif search_by in record.email.value:
            record.append(record)
        else:
            records += list(filter(lambda x: search_by in x.value, record.phones))

    if records:
        return "Search results:'n" + "\n".join(records)
    return f"Contact with attribute {search_by} not found!"


@input_error
def delete_contact(contacts, args):
    # I think Contacts delete command should return str with result of
    # deletion operation: Contact deleted or Contact {name} not in contacts.
    name = args[0]
    return contacts.delete(name)


@phone_args_error
@input_error
def add_phone(contacts, args):
    name, *phones = args
    record = contacts.find(name=name)
    for phone in phones:
        record.add_phone(phone)
    return "Phones added."


@phone_args_error
@input_error
def change_phone(contacts, args):
    name, old_phone, new_phone = args
    record = contacts.find(name=name)
    record.change_phone(old_phone, new_phone)
    return "Phones changed."


@phone_args_error
@input_error
def delete_phone(contacts, args):
    name, phone = args
    record = contacts.find(name=name)
    record.delete_phone(phone)
    return "Phones deleted."


@phone_args_error
@input_error
def delete_all_phone(contacts, args):
    name = args[0]
    record = contacts.find(name=name)
    record.phones = None
    return "All phones deleted."


@email_args_error
@input_error
def add_email(contacts, args):
    name, email = args
    record = contacts.find(name)
    record.add_email(email)
    return "Emails added."


@email_args_error
@input_error
def change_email(contacts, args):
    name, old_email, new_email = args
    record = contacts.find(name=name)
    record.change_phone(old_email, new_email)
    return "Email changed."


@email_args_error
@input_error
def delete_email(contacts, args):
    name, email = args
    record = contacts.find(name=name)
    record.delete_email(email)
    return "Emails deleted."


@email_args_error
@input_error
def delete_all_email(contacts, args):
    name = args[0]
    record = contacts.find(name=name)
    record.email = None
    return "All emails deleted."


@birth_args_error
@input_error
def set_birthday(contacts, args):
    name, birthday = args
    record = contacts.find(name)
    record.add_birthday(birthday)
    return "Birthday changed."


@input_error
def get_birthdays(contacts, *args):
    records = contacts.get_birthdays()
    if len(records) <= 0:
        return "No birthdays next week"
    return "Birthdays next week:\n" + "\n".join(map(str, records))


@input_error
def delete_birthday(contacts, args):
    name = args[0]
    record = contacts.find(name)
    record.birthday = None
    return "Birthday deleted."


@address_args_error
@input_error
def set_address(contacts, args):
    name, address = args
    record = contacts.find(name)
    record.set_address(address)
    return "Address changed."


def get_all_contacts(contacts, *args):
    if not contacts.values():
        return "No contacts yet, please use 'add' command to add them"
    return "\n".join(str(record) for record in contacts.values())


@input_error
def add_note(notes, args):
    note_text = args[0]
    notes.add_note(
        Note(
            title=note_text[:10] if len(note_text) > 10 else note_text,
            text=note_text
        )
    )
    return "Note added."


@note_search_args_error
@input_error
def find_note(notes, args):
    search_by = args[0]
    return notes.find(search_by)

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
    "get-birthday": get_birthdays,
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
    "get-birthday": "get-birthdays <name>",
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
