num = int(input())


def rev_last_five(num):
    result = 0
    cnt = 10
    while num > 0:
        result += num % 10 * 10
        num = num // 10
        cnt *= 10
    return result


res = rev_last_five(num)
print(res)
