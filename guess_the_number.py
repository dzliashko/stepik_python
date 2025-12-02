from random import randint


def is_valid(n, end):
    return n in range(1, end + 1)


print("Введите число больше 0")
end = int(input())

random_n = randint(1, end)
counter = 0

print("Добро пожаловать в числовую угадайку")
print("Введите число")

while True:
    n = int(input())
    if not is_valid(n, end):
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    if n < random_n:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        counter += 1
    elif n > random_n:
        print("Ваше число больше загаданного, попробуйте еще разок")
        counter += 1
    else:
        print("Вы угадали, поздравляем!")
        print(f"Всего было попыток {counter}")
        break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
