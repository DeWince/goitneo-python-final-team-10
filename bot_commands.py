from Contacts.record import Record
from Errors.error_handlers import (
    address_args_error,
    birth_args_error,
    contacts_search_args_error,
    email_args_error,
    input_error,
    note_search_args_error,
    phone_args_error,
    FormatError,
    note_args_error
)


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
    return f"Phone changed.\n{record}"


@phone_args_error
@input_error
def delete_phone(contacts, args):
    name, phone = args
    record = contacts.get_record(name)
    record.clear_phone(phone)
    return f"Phone deleted.\n{record}"


@phone_args_error
@input_error
def delete_all_phone(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.clear_phone("all")
    return f"All phones deleted.\n{record}"


@email_args_error
@input_error
def add_email(contacts, args):
    name, email = args
    record = contacts.get_record(name)
    record.add_mail(email)
    return f"Email added.\n{record}"


@email_args_error
@input_error
def change_email(contacts, args):
    name, old_email, new_email = args
    record = contacts.get_record(name)
    record.change_mail(old_email, new_email)
    return f"Email changed.\n{record}"


@email_args_error
@input_error
def delete_email(contacts, args):
    name, email = args
    record = contacts.get_record(name)
    record.clear_mail(email)
    return f"Email deleted.\n{record}"


@email_args_error
@input_error
def delete_all_email(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.clear_mail("all")
    return f"All emails deleted.\n{record}"


@birth_args_error
@input_error
def set_birthday(contacts, args):
    name, birthday = args
    record = contacts.get_record(name)
    record.set_birthday(birthday)
    return "Birthday changed."


@input_error
def get_birthdays_celebration(contacts, *args):
    days = int(args[0][0]) if (len(args) and str(args[0][0]).isdigit()) else 7
    end_text = f"in next {days} days" if days > 1 else "tomorrow"
    birthdays = contacts.get_birthdays(days)
    if len(birthdays) <= 0:
        return f"No birthdays next {days} day{'s' if days > 1 else ''}"
    return (f"Birthday{'s' if len(birthdays) > 1 else ''} in next {days} day{'s' if days > 1 else ''}:\n" + "\n".join(map(str, birthdays)))


@input_error
def delete_birthday(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.set_birthday()
    return f"Birthday deleted.\n{record}"


@address_args_error
@input_error
def set_address(contacts, args):
    name, *address = args
    record = contacts.get_record(name)
    record.set_address(" ".join(address))
    return f"Address changed.\n{record}"


@input_error
def delete_address(contacts, args):
    try:
        name = args[0]
    except IndexError:
        raise FormatError("Please provide a name!")
    record = contacts.get_record(name)
    record.set_address()    # changed method
    return f"Birthday deleted.\n{record}"


def get_all_contacts(contacts, *args):
    if not contacts.values():
        return "No contacts yet, please use 'add-contact' command to begin"
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
    notes.add_note(title.strip(), text.strip())
    return "Note added."


@note_search_args_error
@input_error
def find_note(notes, args):
    try:
        search_by = args[0]
    except IndexError:
        raise FormatError("Please provide a search query!")
    return notes.find(search_by)


@note_search_args_error
@input_error
def edit_note(notes, args):
    try:
        old_title, new_title, new_text = " ".join(args).split("|")
    except ValueError:
        raise FormatError(
            "Invalid input!\n Edit note syntax: edit-note "
            "<old title> | <new title> | <new note>")
    notes.edit_note(old_title, new_title, new_text)
    return "Note edited."


@note_search_args_error
@input_error
def delete_note(notes, args):
    try:
        title = " ".join(args)
    except IndexError:
        raise FormatError("Please provide a note title!")
    notes.delete(title)
    return "Note deleted."


@input_error
def delete_all_note(notes, args):
    notes.data = {}
    return "All notes deleted."


@input_error
def get_all_notes(notes, *args):
    if not notes.values():
        return "No notes yet, please use 'add-note' command to start"
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
    "add-birthday": set_birthday,
    "get-birthdays-celebration": get_birthdays_celebration,
    "delete-birthday": delete_birthday,
    "add-address": set_address,
    "delete-address": delete_address,
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
    "add-birthday": "add-birthday <name> <birthday>",
    "get-birthdays-celebration": "get-birthdays-celebration <days>",
    "delete-birthday": "delete-birthday <name>",
    "add-address": "add-address <name> <address>",
    "delete-address": "delete-address <name>",
    "all-contacts": "all-contacts",
    "add-note": "add-note <title> | <note>",
    "find-note": "find-note <title>",
    "edit-note": "edit-note <old title> | <new title> | <new note>",
    "delete-note": "delete-note <title>",
    "delete-all-notes": "delete-all-note",
    "all-notes": "all-notes"
}
