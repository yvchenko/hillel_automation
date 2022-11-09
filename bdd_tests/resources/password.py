import secrets
import string


def generate_password(length):
    """
    Generates a random password of a given length
    """
    letters = string.ascii_letters
    numbers = string.digits

    symbols = letters + numbers

    password = ''
    for i in range(length):
        password += ''.join(secrets.choice(symbols))

    return password

print(generate_password(8))