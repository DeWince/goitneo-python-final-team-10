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
        raise IndexError
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
    name, old_phone, new_phone, *_ = args
    record = contacts.get_record(name)
    record.change_phone(old_phone, new_phone)
    return f"Phone changed.\n{record}"


@phone_args_error
@input_error
def delete_phone(contacts, args):
    name, phone, *_ = args
    record = contacts.get_record(name)
    record.clear_phone(phone)
    return f"Phone deleted.\n{record}"


@phone_args_error
@input_error
def delete_all_phones(contacts, args):
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
    name, email, *_ = args
    record = contacts.get_record(name)
    record.add_mail(email)
    return f"Email added.\n{record}"


@email_args_error
@input_error
def change_email(contacts, args):
    name, old_email, new_email, *_ = args
    record = contacts.get_record(name)
    record.change_mail(old_email, new_email)
    return f"Email changed.\n{record}"


@email_args_error
@input_error
def delete_email(contacts, args):
    name, email, *_ = args
    record = contacts.get_record(name)
    record.clear_mail(email)
    return f"Email deleted.\n{record}"


@email_args_error
@input_error
def delete_all_emails(contacts, args):
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
    name, birthday, *_ = args
    record = contacts.get_record(name)
    record.set_birthday(birthday)
    return "Birthday changed."


@input_error
def get_birthdays_celebration(contacts, *args):
    if len(args[0]) and str(args[0][0]).isdigit():
        days = int(args[0][0])
    elif len(args[0]):
        return "Please enter valid number of days!"
    else:
        days = 7

    birthdays = contacts.get_birthdays(days)
    end_text = f"in next {days} days" if days > 1 else "tomorrow"

    if len(birthdays) <= 0:
        return f"No birthdays {end_text}"
    return (f"{len(birthdays)} Birthday{'s' if len(birthdays) > 1 else ''} {end_text}:\n" + "\n".join(map(str, birthdays)))


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
    if not address:
        return "Address missing!"
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


def get_all_contacts(contacts, *_):
    if not contacts.values():
        return "No contacts yet, please use 'add-contact' command to begin"
    return "\n".join(str(record) for record in contacts.values())


@note_args_error
@input_error
def add_note(notes, args):
    if len(args) == 0:
        raise IndexError("Note must contain something")
    note_input = " ".join(args)
    notes.add_note(note_input)
    return "Note added"


@note_search_args_error
@input_error
def find_note(notes, args):
    if len(args):
        return notes.find(args[0])
    raise IndexError("Enter search string")


@note_search_args_error
@input_error
def edit_note(notes, args):
    if len(args) < 2:
        raise IndexError("Incorrect number of arguments")
    idx, *new_text = args
    note_input = " ".join(new_text)
    notes.edit_note(idx, note_input)
    return "Note changed"


@note_search_args_error
@input_error
def delete_note(notes, args):
    if len(args) == 0 or not args[0].isdigit():
        raise IndexError("Enter note number")
    notes.delete(args[0])
    return "Note deleted"


@input_error
def delete_all_notes(notes, *_):
    notes.delete()
    return "All notes deleted"


@input_error
def get_all_notes(notes, *_):
    if not notes.values():
        return "No notes yet, please use 'add-note' to start"
    return notes.print_notes(notes.values())


@input_error
def add_tag(notes, args):
    if len(args) < 2:
        raise IndexError("Incorrect number of arguments")
    idx, tag, *_ = args
    if tag[0:1] != "#":
        tag = f"#{tag}"
    note = notes.get_note_by_id(idx)

    notes.add_tag(idx, tag)
    return f"Tag {tag} added to note {note.title if note.title else ('#' + str(note.number))}"


@input_error
def remove_tag(notes, args):
    if len(args) < 2:
        raise IndexError("Incorrect number of arguments")
    idx, tag, *_ = args
    if tag[0:1] != "#":
        tag = f"#{tag}"
    note = notes.get_note_by_id(idx)

    notes.remove_tag(idx, tag)
    return f"Tag {tag} removed from note {note.title if note.title else ('#' + str(note.number))}"


@input_error
def remove_all_tags(notes, args):
    if not args:
        raise IndexError("Enter note number")
    idx = args[0]
    note = notes.get_note_by_id(idx)

    notes.remove_tag(idx)
    return f"All tags removed from note {note.title if note.title else ('#' + str(note.number))}"


@input_error
def sort_notes_by_tags(notes, *_):
    return notes.sort_notes_by_tags()


@input_error
def group_notes_by_tags(notes, *_):
    return notes.group_notes_by_tags()


@input_error
def find_by_tag(notes, args):
    tag = args[0]
    if tag[0:1] != "#":
        tag = f"#{tag}"
    found_notes = notes.find_by_tag(tag)
    if found_notes:
        return found_notes
    else:
        return f"No notes found with tag {tag}"


CONTACTS_COMMANDS = {
    "add-contact": add_contact,
    "find-contact": find_contact,
    "delete-contact": delete_contact,
    "add-phone": add_phone,
    "change-phone": change_phone,
    "delete-phone": delete_phone,
    "delete-all-phones": delete_all_phones,
    "add-email": add_email,
    "change-email": change_email,
    "delete-email": delete_email,
    "delete-all-emails": delete_all_emails,
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
    "delete-all-notes": delete_all_notes,
    "all-notes": get_all_notes,
    "add-tag": add_tag,
    "remove-tag": remove_tag,
    "remove-all-tags": remove_all_tags,
    'find-tag': find_by_tag,
    'sort-tags': sort_notes_by_tags,
    'group-tags': group_notes_by_tags,
}


COMMANDS_SYNTAX = {
    "add-contact": "add-contact <name>",
    "find-contact": "find-contact <search>",
    "delete-contact": "delete-contact <name>",
    "add-phone": "add-phone <name> <phones>...n",
    "change-phone": "change-phone <name> <old_phone> <new_phone>",
    "delete-phone": "delete-phone <name> <phone>",
    "delete-all-phones": "delete-all-phones <name>",
    "add-email": "add-email <name> <email>",
    "change-email": "change-email <name> <old_email> <new_email>",
    "delete-email": "delete-email <name> <email>",
    "delete-all-emails": "delete-all-emails <name>",
    "add-birthday": "add-birthday <name> <birthday>",
    "get-birthdays-celebration": "get-birthdays-celebration <days>",
    "delete-birthday": "delete-birthday <name>",
    "add-address": "add-address <name> <address>",
    "delete-address": "delete-address <name>",
    "all-contacts": "all-contacts",
    "add-note": "add-note <title> | <note>",
    "find-note": "find-note <search>",
    "edit-note": "edit-note <note_number> <new title> | <new note>",
    "delete-note": "delete-note <note_number>",
    "delete-all-notes": "delete-all-notes",
    "all-notes": "all-notes",
    "add-tag": "add-tag <note_number> <tag>",
    "remove-tag": "remove-tag <note_number> <tag>",
    "remove-all-tags": "remove-all-tags <note_number>",
    "find-tag": "find-tag <tag>",
    "sort-tags": "sort-tags",
    "group-tags": "group-tags",
}
