from file_handler import (
    read_from_file,
    write_to_file
)
from bot_commands import (
    parse_input,
    CONTACTS_COMMANDS,
    NOTES_COMMANDS,
    COMMANDS_SYNTAX
)


def main():
    contacts, notes = read_from_file()

    def exit_bot():
        print("\nGood bye!")
        write_to_file(contacts, notes)
        exit()

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            exit_bot()

        command = ""
        args = []
        if user_input:
            command, *args = parse_input(user_input)
        if command in ["close", "exit", "quit"]:
            exit_bot()
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print("\nCommands syntax:\n" + "\n".join(COMMANDS_SYNTAX.values()))
        elif command in CONTACTS_COMMANDS:
            print(CONTACTS_COMMANDS[command](contacts, args))
            write_to_file(contacts, notes)
        elif command in NOTES_COMMANDS:
            print(NOTES_COMMANDS[command](notes, args))
            write_to_file(contacts, notes)
        else:
            print("Invalid command. To see all commands use 'help'")
            contacts_commands = [key for key in CONTACTS_COMMANDS if command in key]
            notes_commands = [key for key in NOTES_COMMANDS if command in key]

            if contacts_commands or notes_commands:
                print("Most similar commands:\n" + " | ".join(contacts_commands + notes_commands))


if __name__ == "__main__":
    main()
