def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """ Add new contact to the contact list """
    if len(args) != 2:
        return f"Expected 2 arguments, got {len(args)}"

    name, phone = args
    contacts[name] = phone

    return "Contact added."

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """ Change the phone of specified name, it works only if name has already existed """
    if len(args) != 2:
        return f"Expected 2 arguments, got {len(args)}"

    name, phone = args

    if name not in contacts:
        return f"Contact {name} doesnt exist."

    contacts[name] = phone

    return "Contact changed."

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """ Returns phone number for specified name """
    if len(args) != 1:
        return f"Expected 1 arguments, got {len(args)}"

    name = args[0]

    if name not in contacts:
        return f"Contact {name} doesnt exist."

    return f"Phone number for {name}: {contacts.get(name)}"

def show_all_phone(contacts: dict[str, str]) -> str:
    """ List all contacts """
    formated_contacts = [f"Phone number for {name}: {contacts.get(name)}" for name in contacts]

    return "\n".join(formated_contacts)

