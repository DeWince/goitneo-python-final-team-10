import pickle
from os.path import exists
from Contacts.contacts import Contacts
from Notes.notes import Notes

CONTACTS_FILENAME = "Contacts.pkl"
NOTES_FILENAME = "Notes.pkl"


def read_contacts_from_file() -> Contacts:
    if exists(CONTACTS_FILENAME):
        with open(CONTACTS_FILENAME, "rb") as file:
            return pickle.load(file)
    return Contacts()


def write_contacts_to_file(book: Contacts) -> None:
    with open(CONTACTS_FILENAME, "wb") as file:
        pickle.dump(book, file)


def read_notes_from_file() -> Notes:
    if exists(NOTES_FILENAME):
        with open(NOTES_FILENAME, "rb") as file:
            return pickle.load(file)
    return Notes()


def write_notes_to_file(book: Notes) -> None:
    with open(NOTES_FILENAME, "wb") as file:
        pickle.dump(book, file)


def read_from_file() -> tuple:
    return read_contacts_from_file(), read_notes_from_file()


def write_to_file(contacts: Contacts, notes: Notes) -> None:
    write_contacts_to_file(contacts)
    write_notes_to_file(notes)
