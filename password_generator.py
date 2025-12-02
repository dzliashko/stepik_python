import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chats = ""

passwords_qty = input("Количество паролей для генерации ")
password_length = input("Длину одного пароля ")
inc_digits = input("Включать ли цифры '0123456789'? ")
inc_uppercase = input("Включать ли прописные буквы 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'? ")
inc_lowercase = input("Включать ли строчные буквы 'abcdefghijklmnopqrstuvwxyz'? ")
inc_punctuation = input("Включать ли символы '!#$%&*+-=?@^_'? ")
ex_symbols = input("Исключать ли неоднозначные символы 'il1Lo0O' ?")
