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

#q3 update product quantity
    def update(self,pid,quantity):
        temp = self.head

        while temp:
            if temp.pid == pid:
                temp.quantity = quantity
                print("Quantity Updated")
                return 
            temp = temp.next

#q4 display all records
    def display(self):
        temp = self.head

        while temp:
            print(temp.pid)
            print(temp.pname)
            print(temp.quantity)
            print(temp.price)

        temp = temp.next

#q5 product with highest price
    def highest(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        max = self.head

        while temp:
            if temp.price > max.price:
                max = temp
        temp = temp.next

    print(max.name, max.price)

#q7 7.	Display products whose quantity is below a specified limit.
    def low(self,limit):
        temp = self.head
        found = False

        while temp:
            if temp.quantity < limit:
                print(temp.name)
                print(temp.quantity)
                found = True
        temp = temp.next

        if found == False:
            print("No products below the limit")
