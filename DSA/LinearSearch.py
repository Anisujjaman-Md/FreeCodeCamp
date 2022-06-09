def linear_serch(list, value):  # sourcery skip: use-next
    """
    This function will return the index of the value in the list
    """
    for i in range(len(list)):
        if list[i] == value:
            return i
    return None

def verif(index):
    if index is None:
        print("Value not found")
    else:
        print("Value found at index", index)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 5

verif(linear_serch(a, b))