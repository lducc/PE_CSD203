import math
from Product import *
from Node import *

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head is None
    
    def traverse(self):
        pt = self.head
        while pt.next:
            print(pt.data, end=" ")
            pt = pt.next
        print(pt.data)
    
    def clear(self):
        self.head = None
    
    # Q1-1: Add a new product to the end of the list if conditions are met
    def f1(self, id=0, name="", price=-1):
        if name.endswith("D") or id > 100 or price > 100:
            return  

        new_product = Product(id, name, price)
        new_node = Node(new_product)
        
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def f2(self, B):

        current = self.head
        prev = None
        odd_count = 0

        while current:
            if current.data.Id % 2 != 0:
                odd_count += 1
            if odd_count == 2:

                new_node = Node(B)
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node  
                new_node.next = current
                return
            prev = current
            current = current.next

    def f3(self, x):

        current = self.head
        prev = None

        while current:
            if current.data.price < x:
  
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = prev  
                return
            prev = current
            current = current.next

    def f4(self):

        odd_nodes = []
        current = self.head

        while current:
            if current.data.Id % 2 != 0:
                odd_nodes.append(current)
            current = current.next

        odd_nodes.sort(key=lambda node: (-node.data.price, node.data.name))

        current = self.head
        odd_index = 0

        while current:
            if current.data.Id % 2 != 0:

                current.data = odd_nodes[odd_index].data
                odd_index += 1
            current = current.next

