"""_CLI (Command Line Interface) bot_
"""
USERS = {}
def greeting(*_):
    """greeting"""
    return "How can I help you?"
def good_bye(*_):
    """farewell"""
    return "Good bye!"

def add_contact(data):
    """add contact to dict"""
    name, phone = data
    
    USERS[name] = phone
    return f"The user with name: {name } and phone: {phone} was added."
def change_contact(data):
    """change contact in dict"""
    name, phone = data
    if name in USERS:
        USERS[name] = phone
    return f"The contact for the user {name} has been updated to {phone}."
def get_phone(data):
    """get contact phone number by name"""
    name = data[0]
    if name in USERS:
        return f"{name}'s number is {USERS[name]}"
    return f"{name}'s contact not found."
def show_all(*_):
    """Show all contacts in the dictionary."""
    if USERS:
        return "\n".join([f"Name: {key}, Phone Number: {value}" for key, value in USERS.items()])
    return "No contacts found."

OPERATIONS = {
    "hello": greeting,
    "add": add_contact,
    "change": change_contact,
    "phone": get_phone,
    "show_all": show_all,
    "good_bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye,
}
def input_errors(func):
    """Decorator to handle input errors"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "You must enter a valid command."
    return wrapper

@input_errors
def parse_command(user_input):
    """Parse commands from users"""
    user_input = user_input.lower()
    print(f'user_input: {user_input}')
    exit_commands = ("good bye", "close", "exit", ".")
    command = user_input.split()[0].lower()
    print(f'command: {command}')
    data = [word.lower() for word in user_input.split()[1:]]
    print(f'data: {data}')
    if command in exit_commands:
        return good_bye()
    
    if command in OPERATIONS:
        return OPERATIONS[command](data[0:] if data else "")
    
    return "Command not recognized."

def main():
    """Main function"""
    end_point = False
    while not end_point:
        user_input = input("... ")
        result = parse_command(user_input)
        print(result)

        if user_input.lower() in ('good bye', 'close', 'exit', '.'):
            end_point = True

if __name__ == "__main__":
    
    main()
