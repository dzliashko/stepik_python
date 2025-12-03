num = int(input())


def rev_last_five(num):
    result = 0
    cnt = 10000
    while num > 0:
        result += num % 10 * cnt
        num = num // 10
        cnt /= 10
    return int(result)


res = rev_last_five(num)
print(res)
