import random
numbers = [1, 8, 6, 14, 15, 16, 8, 9 , 9, 4, 55, 66, 8, 10]

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True
def bogo_sort(values):
    i = 0
    while not is_sorted(values):
        random.shuffle(values)
        i += 1
    print(i)
    return values

print(bogo_sort(numbers))