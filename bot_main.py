from file_handler import (
    read_from_file,
    write_to_file
)
from bot_commands import (
    parse_input,
    CONTACT_COMMANDS,
    CONTACT_COMMANDS_SYNTAX,
    NOTES_COMMANDS,
    NOTES_COMMANDS_SYNTAX
)


def main():
    contacts, notes = read_from_file()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            write_to_file(contacts, notes)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print("\nContact commands:\n" + "\n".join(CONTACT_COMMANDS_SYNTAX.values()))
            print("\nNote commands:\n" + "\n".join(CONTACT_COMMANDS_SYNTAX.values()))
        elif command in CONTACT_COMMANDS:
            print(CONTACT_COMMANDS[command](contacts, args))
        elif command in NOTES_COMMANDS:
            print(NOTES_COMMANDS[command](notes, args))
        else:
            print("Invalid command. To see all commands use 'help' command")
            contact_commands = [key for key in CONTACT_COMMANDS if command in key]
            notes_commands = [key for key in NOTES_COMMANDS if command in key]
            if contact_commands:
                print("Most similar contact commands:\n" + " | ".join(contact_commands))
            if notes_commands:
                print("Most similar note commands:\n" + " | ".join(notes_commands))


if __name__ == "__main__":
    main()
