from linked_list import LinkedList

def marge_sort(linked_list):
    """Sorts a linked list in accending order
        -Recursively divide the linked list into sublist containing a single node
        -Repetedly merge the sublist to produce sorted sublists until one remains
         Returns a sorted linked list       """
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = marge_sort(left_half)
    right = marge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """Divide the unsorted linked list at midpoint intu subLinked List"""
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
    return 