import random
import string

def generate_password(length):
    if length < 6 or length > 32:
        raise ValueError("Довжина пароля повинна бути від 6 до 32 символів.")

    # Набори символів
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_+="

    # Перевіряємо, щоб у паролі були всі необхідні типи символів
    all_characters = lowercase + uppercase + digits + special_characters

    # Гарантуємо наявність хоча б одного символу кожного типу
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Заповнюємо решту пароля випадковими символами
    password += random.choices(all_characters, k=length - 4)

    # Перемішуємо пароль
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    try:
        length = int(input("Введіть довжину пароля (від 6 до 32): "))
        print(f"Ваш випадковий пароль: {generate_password(length)}")
    except ValueError as e:
        print(f"Помилка: {e}")