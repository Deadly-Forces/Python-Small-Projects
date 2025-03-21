import string
import getpass
def check_pwd():
    password = getpass.getpass("Enter your password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    if strength == 1:
        remarks = 'That\'s a very bad password.'
    elif strength == 2:
        remarks = 'That\'s a weak password.'
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = 'Your password is hard to guess.'
    elif strength == 5:
        remarks = 'Now that\'s one hell of a strong password !!!'
    print('Your password has:-')
    print(f"{lower_count} lowercase letters")
    print(f"{upper_count} uppercase letters")
    print(f"{num_count} digits")
    print(f"{wspace_count} whitespaces")
    print(f"{special_count} special characters")
    print(f"Password strength: {strength}/5")
    print(f"Hint:{remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice=input("Do you want to check another password? (y/n): ")
    else:
        choice=input("Do you want to change your password's strength? (y/n): ")
    while not valid:
        if choice.lower() == 'y':
            check_pwd()
            ask_pwd(True)
            valid = True
        elif choice.lower() == 'n':
            print("Thank you!")
            valid = True
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
if __name__ == '__main__':
    print("Welcome to the password strength checker!")
    ask_pwd = ask_pwd()
    while check_pwd:
        check_pwd()
        ask_pwd = ask_pwd(True)
