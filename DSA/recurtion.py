def sum(number):
    if not number:
        return 0
    total = sum(number[1:])
    return number[0] + total

print(sum([1, 2, 3, 4, 5]))