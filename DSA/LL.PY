#A supermarket maintains product information using a singly linked list. Each node contains Product ID, Product Name, Quantity, and Price.

class node:
    def __init__(self,pid,pname,quantity,price):
        self.pid = pid
        self.pname = pname
        self.quantity = quantity
        self.price = price
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

#q1 1.	Add a new product.
    def append(self,pid,pname,quantity,price):
         new = node(pid,pname,quantity,price)

         if self.head is None:
             self.head = new
             return

         temp = self.head

         while temp.next:
             temp = temp.next

             temp.next = new
# q2 search product using product id.
    def search(self,pid):
        temp = self.pid

        while temp:
            if temp.pid == pid:
                print("Product found")
                return 
            temp = temp.next
        print("Product not found")