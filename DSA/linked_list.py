from turtle import position
from winreg import KEY_CREATE_SUB_KEY


class Node:
    """An object for storing a single node of a linked list
    Models two attributes -data and link to the next mode in list"""
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"< Node is : {self.data}>"

class LinkedList:
    # head = None
    """Singly Linked List"""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Returns True if list is empty, False otherwise"""
        return self.head is None

    def size(self):
        """Return thr nimber of nodes in the list
            is takes O(n) time"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node

        return count
    
    def add (self, data):
        """Add a new node containing data at the head of the linked List"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        """Search fot the first node conatiainung data matches the key 
            Returnt the  node o 'None' if not found
            Takes O(n) time"""

        current = self.head

        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def inseart(self, data, index):
        """Inseart a new node at the index postion 
            Insertion takes O(0) time and
            Finiding the index takes O(n) time"""
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node 
                position -= 1 

            prev_node = current 
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node= next_node
    def remove(self, key):
        """Remove Node Cotaint  data that matches the key
            Returns the node or None if key doesn't exit
            Takes O(n) time"""
        current = self.head
        prev = None
        found = False
        while current and  not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node

        return current
         

    def __str__(self):     #sourcery skip: replace-interpolation-with-fstring
        """Return a string representation of the list"""

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)

            elif current.next_node is None:
                nodes.append("[Tail: %s]" %current.data)

            else:
                nodes.append("[%s]" %current.data)
                
            current = current.next_node

        return "->".join(nodes)
            
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