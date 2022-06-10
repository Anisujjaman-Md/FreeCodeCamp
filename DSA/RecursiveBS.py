def recursive_binary_search(list, target):
    if len(list) == 0:
        return None
    mid = len(list) // 2

    if list[mid] == target:
        return True
    elif list[mid] < target:
        return recursive_binary_search(list(mid + 1), target)
    else:
        return recursive_binary_search(list[:mid], target)

def verify(result):
    print("Value found: ", result)

n = [5, 6, 7, 8, 9, 10]
verify(recursive_binary_search(n, 5))