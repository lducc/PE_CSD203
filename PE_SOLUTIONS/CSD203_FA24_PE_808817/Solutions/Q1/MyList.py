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
        # if name.endswith("D") or id > 100 or price > 100:
        #     return  

        # new_product = Product(id, name, price)
        # new_node = Node(new_product)
        
        # if self.isEmpty():
        #     self.head = self.tail = new_node
        # else:
        #     self.tail.next = new_node
        #     self.tail = new_node
        

        if name[-1] == "D" or id > 100 or price > 100:
            return
        
        new_node = Node(Product(id, name, price))

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = self.tail.next

    def f2(self, B):
        # current = self.head
        # prev = None
        # odd_count = 0

        # while current:
        #     if current.data.Id % 2 != 0:
        #         odd_count += 1
        #     if odd_count == 2:

        #         new_node = Node(B)
        #         if prev:
        #             prev.next = new_node
        #         else:
        #             self.head = new_node  
        #         new_node.next = current
        #         return
        #     prev = current
        #     current = current.next


        if self.isEmpty():
            return
        
        curr, prev = self.head, None
        count = 0
        new_node = Node(B)

        while curr:
            if curr.data.Id % 2 != 0:
                count += 1

            if count == 2:
                prev.next = new_node
                new_node.next = curr
                return
            
            prev = curr
            curr = curr.next


    def f3(self, x):
#             current = self.head
    #         prev = None

    #         while current:
    #             if current.data.price < x:

    #                 if prev:
    #                     prev.next = current.next
    #                 else:
    #                     self.head = current.next
    #                 if current == self.tail:
    #                     self.tail = prev  
    #                 return
    #             prev = current
    #             current = current.next

        if self.isEmpty():
            return
        
        if self.head.data.Price < x:
            self.head = self.head.next
            return
        
        curr, prev = self.head.next, self.head

        while curr:
            if curr.data.Price < x:
                prev.next = curr.next
                return
            
            prev = curr
            curr = curr.next
       

    def f4(self):
        
    #   nodes = []

    #     curr = self.head
    #     while curr:
    #         if curr.data.Id % 2 != 0:
    #             nodes.append(curr)
    #         curr = curr.next

    #     nodes.sort(key = lambda node: (-node.data.Price, node.data.Name))

    #     idx = 0

    #     curr = self.head
    #     while curr:
    #         if curr.data.Id % 2 != 0:
    #             curr.data = nodes[idx].data
    #             idx += 1

    #         curr = curr.next

        curr = self.head
        while curr:
            n = curr.next
            while n:
                if n.data.Id % 2 != 0 and curr.data.Id % 2 != 0:
                    if n.data.Price > curr.data.Price or (n.data.Price == curr.data.Price and n.data.Name < curr.data.Name):
                        n.data, curr.data = curr.data, n.data

                n = n.next

            curr = curr.next

            

