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
