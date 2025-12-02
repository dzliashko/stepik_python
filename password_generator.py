from random import shuffle, sample, randint

digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""

passwords_qty = int(input("Количество паролей для генерации? "))
password_length = int(input("Длину одного пароля? "))
inc_digits = input("Включать ли цифры '0123456789'? (y) ")
if inc_digits == "y":
    chars += digits
inc_uppercase = input("Включать ли прописные буквы 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'? (y) ")
if inc_uppercase == "y":
    chars += uppercase
inc_lowercase = input("Включать ли строчные буквы 'abcdefghijklmnopqrstuvwxyz'? (y) ")
if inc_lowercase == "y":
    chars += lowercase
inc_punctuation = input("Включать ли символы '!#$%&*+-=?@^_'? (y) ")
if inc_punctuation == "y":
    chars += punctuation
ex_symbols = input("Исключать ли неоднозначные символы 'il1Lo0O' (y)? ")
if ex_symbols == "y":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")


def generate_password(chars, length):
    chars = list(chars)
    for n in range(randint(1, 5)):
        shuffle(chars)
    chars = "".join(chars)
    return sample(chars, length)


passwords = []
for i in range(passwords_qty):
    passwords.append("".join(generate_password(chars, password_length)))

print(*passwords)
