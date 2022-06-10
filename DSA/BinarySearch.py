def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == target:
            return mid
    
        elif list[mid] < target:
            low = mid + 1
    
        else:
            high = mid - 1

    return None

def verif(index):
    if index is None:
        print("Value not found")
    else:
        print("Value found at index", index)

a = [5, 6, 7, 8, 9, 10]
b = 5

verif(binary_search(a, b))  
