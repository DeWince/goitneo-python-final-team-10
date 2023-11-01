from Contacts.record import Record
from Errors.error_handlers import address_args_error, birth_args_error, contacts_search_args_error, email_args_error, \
    input_error, note_search_args_error, phone_args_error, FormatError, note_args_error
from Notes.note import Note


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    contacts.add_record(Record(name))
    return "Contact added."


@contacts_search_args_error
@input_error
def find_contact(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    return (
        "Search result:\n" +
        "\n".join(str(record) for record in contacts.find_record(name))
    )


@input_error
def delete_contact(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    return "Contact deleted:\n" + str(contacts.delete_record(name))


@phone_args_error
@input_error
def add_phone(contacts, args):
    name, *phones = args
    if not phones:
        raise ValueError
    record = contacts.get_record(name)
    results = []
    for phone in phones:
        try:
            record.add_phone(phone)
            results.append(f"Phone {phone} added.")
        except FormatError as e:
            results.append(f"Phone {phone} format is invalid.")
    return "\n".join(results)


@phone_args_error
@input_error
def change_phone(contacts, args):
    name, old_phone, new_phone = args
    record = contacts.get_record(name)
    record.change_phone(old_phone, new_phone)
    return "Phones changed."


@phone_args_error
@input_error
def delete_phone(contacts, args):
    name, phone = args
    record = contacts.get_record(name)
    record.clear_phone(phone)
    return "Phones deleted."


@phone_args_error
@input_error
def delete_all_phone(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.phones = set()
    return "All phones deleted."


@email_args_error
@input_error
def add_email(contacts, args):
    name, email = args
    record = contacts.get_record(name)
    record.add_mail(email)
    return "Emails added."


@email_args_error
@input_error
def change_email(contacts, args):
    name, old_email, new_email = args
    record = contacts.get_record(name)
    record.change_mail(old_email, new_email)
    return "Email changed."


@email_args_error
@input_error
def delete_email(contacts, args):
    name, email = args
    record = contacts.get_record(name)
    record.clear_mail(email)
    return "Emails deleted."


@email_args_error
@input_error
def delete_all_email(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.emails = set()
    return "All emails deleted."


@birth_args_error
@input_error
def set_birthday(contacts, args):
    name, birthday = args
    record = contacts.get_record(name)
    record.set_birthday(birthday)
    return "Birthday changed."


@input_error
def get_birthday(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    return str(record.birthday)


@input_error
def get_birthdays_celebration(contacts, *args):
    days = int(args[0][0]) if (len(args) and str(args[0][0]).isdigit()) else 7
    records = contacts.get_birthdays(days)
    if len(records) <= 0:
        return f"No birthdays next {days} day"
    return (f"Birthdays in next {days} days:\n" +
            "\n".join(map(str, records)))


@input_error
def delete_birthday(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.birthday = None
    return "Birthday deleted."


@address_args_error
@input_error
def set_address(contacts, args):
    name, address = args
    record = contacts.get_record(name)
    record.set_address(address)
    return "Address changed."


def get_all_contacts(contacts, *args):
    if not contacts.values():
        return "No contacts yet, please use 'add' command to add them"
    return "\n".join(str(record) for record in contacts.values())


@note_args_error
@input_error
def add_note(notes, args):
    try:
        user_text = " ".join(args)
        if "|" in user_text:
            title, text = user_text.split("|")
        else:
            title = user_text[:10] if len(user_text) > 10 else user_text
            text = user_text
    except IndexError:
        raise FormatError("Please provide note title!")
    notes.add_note(title, text)
    return "Note added."


@note_search_args_error
@input_error
def find_note(notes, args):
    try:
        search_by = args[0]
    except IndexError:
        raise FormatError("Please provide search query!")
    return notes.find(search_by)


@note_search_args_error
@input_error
def edit_note(notes, args):
    title, new_text = " ".join(args).split("-")
    notes.edit_note(title, new_text)
    return "Note edited."


@note_search_args_error
@input_error
def delete_note(notes, args):
    try:
        title = " ".join(args)
    except IndexError:
        raise FormatError("Please provide note title!")
    notes.delete(title)
    return "Note deleted."


@input_error
def delete_all_note(notes, args):
    notes.data = {}
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
    "delete-all-phones": delete_all_phone,
    "add-email": add_email,
    "change-email": change_email,
    "delete-email": delete_email,
    "delete-all-emails": delete_all_email,
    "set-birthday": set_birthday,
    "get-birthday": get_birthday,
    "get-birthdays-celebration": get_birthdays_celebration,
    "delete-birthday": delete_birthday,
    "set-address": set_address,
    "all-contacts": get_all_contacts
}


NOTES_COMMANDS = {
    "add-note": add_note,
    "find-note": find_note,
    "edit-note": edit_note,
    "delete-note": delete_note,
    "delete-all-notes": delete_all_note,
    "all-notes": get_all_notes
}


COMMANDS_SYNTAX = {
    "add-contact": "add-contact <name>",
    "find-contact": "find-contact <search input>",
    "delete-contact": "delete-contact <name>",
    "add-phone": "add-phone <name> <phones>",
    "change-phone": "change-phone <name> <old_phone> <new_phone>",
    "delete-phone": "delete-phone <name> <phone>",
    "delete-all-phones": "delete-all-phone <name>",
    "add-email": "add-email <name> <email>",
    "change-email": "change-email <name> <old_email> <new_email>",
    "delete-email": "delete-email <name> <email>",
    "delete-all-emails": "delete-all-email <name>",
    "set-birthday": "set-birthday <name> <birthday>",
    "get-birthday": "get-birthday <name>",
    "get-birthdays-celebration": "get-birthdays-celebration",
    "delete-birthday": "delete-birthday <name>",
    "set-address": "set-address <name> <address>",
    "all-contacts": "all-contacts",
    "add-note": "add-note <text>",
    "find-note": "find-note <title>",
    "edit-note": "edit-note <title> - <new-text>",
    "delete-note": "delete-note <title>",
    "delete-all-notes": "delete-all-note",
    "all-notes": "all-notes"
}
