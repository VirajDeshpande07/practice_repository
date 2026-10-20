class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

#creating instances of node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#creating link between the nodes
node1.next = node2
node2.next = node3
node3.next = node4

#insert node at the beginning
head = node1
new_node = Node(50)
new_node.next = head
head = new_node

#printing the linked list
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")