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
    else:
        size = linked_list.size()
        mid = size //2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node =None

    return left_half, right_half
def merge(left, right):
    """Merge two sorted linked list into one sorted linked list
        -Create a new linked list"""

    #Creating a new linked list what that contain node from 
    #merging left and right

    merged = LinkedList()

    #add a fake head that is discarded later

    merged.add(0)

    #Set current to the head of the linked list

    current = merged.head

    #obtain head nodes fopr left and right linked lists
    left_head = left.head
    right_head = right.head
    
    #Iterating over left and right until we reach the tail node
    #of either

    while left_head or right_head:
        #if the head node  of the left is None, we're past the tail
        #and the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right  to set loop condition to False
            right_head = right_head.next_node

            #if the head node of right is none we are past the tail
            #and tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            #Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            #Not at either tail Node
            #either node data to perform comparison
            left_data = left_head.data
            right_data = right_head.data

            if left_data< right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    #Discard the fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    return merged

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)

print(l)
l.inseart(6, 4)
print(l)
print(l.size())
l.remove(3)
print(l)
print(l.search(3))
print(l.size())
print(marge_sort(l))