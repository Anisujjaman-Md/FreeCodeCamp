def merge_sort(list):
    """Sort a list in accending order
        Retuns a  sorted list
        
        Divide: Find the midpoint of the list and divide into sublists
        Conquer: Recursively sort the sublists created in previous step
        Combine: Merge the sorted sublists created in previous step"""

    if len(list) <= 1:
        return list
    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """Split a list into two sublists
        Returns two sublists
        Takes O(n) time"""

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    """"
        Merge two sorted lists into one 
        sorted list
        Returns a sorted list"""
    result = []
    i = 0
    j = 0

    while i < len(left) and j <len(right):
        if left[i] < right [j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j +=1
    return result

def verify(list):
    n = len(list)

    if n in {0, 1}:  #n==0 or n==1
        return True

    return list[0] < list [1] and verify(list[1:])


a = [45, 23, 11, 89, 77, 10, 2, 3,844,5,88,9,7,4,6,1,0]
print(merge_sort(a))
print(verify(merge_sort(a)))