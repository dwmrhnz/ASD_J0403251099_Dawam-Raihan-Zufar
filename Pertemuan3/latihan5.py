class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display_forward(self):
        print("\nLinked List sebelum dibalik:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        print("\nLinked List sesudah dibalik:")
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.data)
            temp = temp.next
        while stack:
            print(stack.pop(), end=" -> ")
        print("null")

sllist = LinkedList()
data_input = input("Masukan elemen untuk Linked List: ")
data = data_input.strip().split()

for d in data:
    sllist.insert_at_end(int(d))

sllist.display_forward()
sllist.display_backward()


