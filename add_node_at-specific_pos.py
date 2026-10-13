# add a node at specific position in the linked list.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#creating multiple nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connecting the nodes
node1.next = node2
node2.next = node3
node3.next = node4

# creating a new node to insert
new_node = Node(25)

#inserting the new node after 2nd position
current = node1
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node

current = node1
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")