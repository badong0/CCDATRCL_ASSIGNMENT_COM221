class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.data = None
    def traverse(self,node):
        head = node
        while node:
            print(node.data, end = " -> ")
            node = node.next
            #break to prevent infinite recursion
            if node == head:
                break
circular_linked_list = CircularLinkedList()

circular_linked_list.head = Node("earl")
node_b = Node("neil")
node_c = Node("brando")
node_d = Node("francyne")
node_e = Node("kristel")

circular_linked_list.head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = circular_linked_list.head

print("Head Value: ", circular_linked_list.head.data)
print("Next Value: ", circular_linked_list.head.next.data, "\n")

print("Head Value: ", node_b.data)
print("Next Value: ", node_b.next.data, "\n")

print("Head Value: ", node_c.data)
print("Next Value: ", node_c.next.data, "\n")

print("Head Value: ", node_d.data)
print("Next Value: ", node_d.next.data, "\n")

print("Head Value: ", node_e.data)
print("Next Value: ", node_e.next.data, "\n")

circular_linked_list.traverse(circular_linked_list.head)