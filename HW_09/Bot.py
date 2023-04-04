contacts = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid command format"
        except IndexError:
            return "Invalid command format"
    return wrapper

@input_error
def add(command):
    name, phone = command.split()[1:]
    contacts[name] = phone
    return f"{name} added with phone number {phone}"

@input_error
def change(command):
    name, phone = command.split()[1:]
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for {name} updated to {phone}"

@input_error
def show_all():
    if not contacts:
        return "No contacts found"
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def phone(command):
    name = command.split()[1]
    if name not in contacts:
        raise KeyError
    return f"Phone number for {name}: {contacts[name]}"

def main():
    print("How can I help you?")
    while True:
        command = input().lower()
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            print(add(command))
        elif command.startswith("change "):
            print(change(command))
        elif command.startswith("phone "):
            print(phone(command))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
      
