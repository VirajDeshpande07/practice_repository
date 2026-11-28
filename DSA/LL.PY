
class node:
    def __init__(self, pid, pname, quantity, price):
        self.pid = pid
        self.pname = pname
        self.quantity = quantity
        self.price = price
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    # q1 Add a new product
    def append(self, pid, pname, quantity, price):
        new = node(pid, pname, quantity, price)

        if self.head is None:
            self.head = new
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new

    # q2 Search product using Product ID
    def search(self, pid):
        temp = self.head

        while temp:
            if temp.pid == pid:
                print("Product found")
                print(temp.pid, temp.pname, temp.quantity, temp.price)
                return

            temp = temp.next

        print("Product not found")

    # q3 Update product quantity
    def update(self, pid, quantity):
        temp = self.head

        while temp:
            if temp.pid == pid:
                temp.quantity = quantity
                print("Quantity Updated")
                return

            temp = temp.next

        print("Product not found")

    # q4 Display all records
    def display(self):
        temp = self.head

    while temp:
        print(temp.pid, temp.pname, temp.quantity, temp.price)
        temp = temp.next

    # q5 Product with highest price
    def highest(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        high = self.head

        while temp:
            if temp.price > high.price:
                high = temp

            temp = temp.next

        print(high.pname, high.price)

    # q7 Products below specified quantity
    def low(self, limit):
        temp = self.head
        found = False

        while temp:
            if temp.quantity < limit:
                print(temp.pname)
                print(temp.quantity)
                found = True

            temp = temp.next

        if found == False:
            print("No products below the limit")


# Execution
list = linkedlist()

list.append(101, "Milk", 20, 60)
list.append(102, "Bread", 30, 70)
list.append(103, "Eggs", 40, 80)
list.append(104, "Butter", 30, 20)

print("Original List")
list.display()

print("\nSearch product with ID 102:")
list.search(102)

print("\nUpdate Quantity")
list.update(103, 70)

print("\nHighest price product:")
list.highest()

print("\nProducts below quantity 30")
list.low(30)
