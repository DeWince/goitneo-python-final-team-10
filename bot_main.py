from file_handler import (
    read_from_file,
    write_to_file
)
from bot_commands import (
    parse_input,
    COMMANDS,
    COMMANDS_SYNTAX
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
            print("\nCommands syntax:\n" + "\n".join(COMMANDS_SYNTAX.values()))
        elif command in COMMANDS:
            print(COMMANDS[command](contacts, args))
        else:
            print("Invalid command. To see all commands use 'help'")
            commands = [key for key in COMMANDS if command in key]
            if commands:
                print("Most similar commands:\n" + " | ".join(commands))


if __name__ == "__main__":
    main()
