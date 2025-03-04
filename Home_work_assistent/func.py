from input_data import correct_number

def hello() -> None:
    print('How i can help you?')

#Додає новий словник якщо name не збігається
def add_contact(contact, args):
    
    if len(args) != 2:
        return "Invalid number of arguments"
    
    name, phone = args
    
    if name in contact:
        return "User already added"
    
    if correct_number(phone):
        contact[name] = phone
        return 'Contact added.'
    else:
        return 'Invalid symbols in number'
    
#Змінює значення phone якщо name у списку
def change_contact(contact, args):
    if len(args) != 2:
        return "invalid number of arguments"
    
    name, phone = args
    
    if name not in contact:
        return "User not found"
    
    if correct_number(phone):
        contact[name] = phone
        return "Сontact updated"
    else:
        return 'Invalid symbols in number'

#Повертає номер якщо name у списку
def show_phone(contacts, users_request):
    name = users_request[0]
    if name in contacts:
        return contacts[name]
    
    return "Contact not found"

#Повертає усі збереженні контакти
def show_all(contacts):
    return '\n'.join(f'{key}: {value}' for key, value in contacts.items())

