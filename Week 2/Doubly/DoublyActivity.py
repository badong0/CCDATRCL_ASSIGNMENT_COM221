#double linked list prev data and next

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def traverse(self, node):
        while node:
            print(node.data, end = " -> ")
            node = node.next

doubly_linked_list = DoublyLinkedList()


doubly_linked_list.head = Node("earl")
node_b = Node("neil")
node_c = Node("brando")
node_d = Node("francyne")
node_e = Node("kristel")

doubly_linked_list.head.prev = None
doubly_linked_list.head.next = node_b

node_b.prev = doubly_linked_list.head
node_b.next = node_c

node_c.prev = node_b
node_c.next = node_d

node_d.prev = node_c
node_d.next = node_e

node_e.prev = node_d
node_e.next = None

print("Head Value: ", doubly_linked_list.head.data)
print("Prev Value: ", doubly_linked_list.head.prev)
print("Next Value: ", doubly_linked_list.head.next.data, "\n")

print("Head Value: ", node_b.data)
print("Prev Value: ", node_b.prev.data)
print("Next Value: ", node_b.next.data, "\n")

print("Head Value: ", node_c.data)
print("Prev Value: ", node_c.prev.data)
print("Next Value: ", node_c.next.data, "\n")

print("Head Value: ", node_d.data)
print("Prev Value: ", node_d.prev.data)
print("Next Value: ", node_d.next.data, "\n")

print("Head Value: ", node_e.data)
print("Prev Value: ", node_e.prev.data)
print("Next Value: ", node_e.next, "\n")

doubly_linked_list.traverse(doubly_linked_list.head)