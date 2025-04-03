def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Будь ласка, введіть ім'я та номер телефону."
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Введіть команду та необхідні аргументи."
        except Exception as e:
            return f"Виникла непередбачена помилка: {e}"
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def show_phone(args, contacts):
    if not args:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "Список контактів порожній."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Приклад використання в основному циклі бота:
def main():
    contacts = {}
    while True:
        command = input("Введіть команду: ").lower()
        if command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            args_str = input("Введіть ім'я та номер телефону через пробіл: ")
            args = args_str.split()
            print(add_contact(args, contacts))
        elif command == "phone":
            args_str = input("Введіть ім'я контакту: ")
            args = args_str.split()
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["good bye", "close", "exit"]:
            print("До побачення!")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
