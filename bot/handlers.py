"""handlers module"""


def parse_input(user_input):
    """parses commands"""
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


def add_contact(args, contacts):
    """adds contacts in format: 'name':'phone'"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """changes contact's phone"""
    name, new_phone = args
    contacts[name] = new_phone
    return "Contact changed."


def show_phone(args, contacts):
    """shows phone of specific name"""
    name = args[0]
    return contacts[name]
    