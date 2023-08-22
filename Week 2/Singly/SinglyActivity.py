#create a node class

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
#create Linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, node):
        while node:
            print (node.data, end = " -> ")
            node = node.next

linked_list = LinkedList()

linked_list.head = Node("earl")
node_b = Node("neil")
node_c = Node("brando")
node_d = Node("francyne")
node_e = Node("kristel")

linked_list.head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e

linked_list.traverse(linked_list.head)