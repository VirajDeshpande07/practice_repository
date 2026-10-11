class Node:       #created a node
    def __init__(self,data):
        self.data = data
        self.next = None
# creating the multiple nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#connecting nodes to form a linked list.
node1.next = node2   
node2.next = node3
node3.next = node4

# insert a new node in the beginning
head = node1    #--> head points towards the node1.
new_node = Node(50)
new_node.next = head  # here head was already pointing towards the node 1 so when new_node.next stores head that means it comes before the node 1.
head = new_node # this updates the head value that means our new head is new_node.


# printing the linked list

current = head    # currenct -----> is the pointer that will be traversed in the list.
while current is not None:
    print(current.data, end="->")
    current=current.next
print(None)