import argparse
from give_me.src.manager import PasswordManager
from give_me.src.help import HELP_TEXT


COMMANDS = ["create", "edit", "list", "remove"]


class CustomFormatter(argparse.RawTextHelpFormatter):
    def format_help(self):
        return HELP_TEXT


def run():
    parser = argparse.ArgumentParser(
        prog="give_me",
        description="CLI program to help with password management",
        formatter_class=CustomFormatter
    )

    parser.add_argument("command_or_password_name", help="Command or the name of the password to copy")
    parser.add_argument("password_name", nargs="?", default=None, help="Name of the password for create/edit/remove")
    parser.add_argument("--no-private", action="store_true", help="Show passwords in plain text (use with caution!)")
    args = parser.parse_args()

    password_manager = PasswordManager()

    if args.command_or_password_name in COMMANDS:
        command = args.command_or_password_name

        if command == "create":
            password_name = args.password_name or input("Enter name for password: ")
            password_manager.create_password(password_name)

        elif command == "edit":
            password_name = args.password_name or input("Enter name for password to edit: ")
            password_manager.edit_password(password_name)

        elif command == "list":
            password_manager.list_passwords(args.no_private)

        elif command == "remove":
            password_name = args.password_name or input("Enter name for password to remove: ")
            password_manager.remove_password(password_name)
    else:  # Default behavior: copy to clipboard
        password_manager.copy_password(args.command_or_password_name)
