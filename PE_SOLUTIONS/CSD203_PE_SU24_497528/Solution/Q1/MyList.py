import math
from Employee import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt.next:
            print(pt.data, end = " ")
            pt = pt.next
        print(pt.data)

    def clear(self):
        self.head = None    
#Q1-1
    def f1(self, name="", age="", salary=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name.startswith("Z") or age < 15 or salary <=0:
            return
        else:
            n = Node(Employee(name,age,salary))
    #         node = Node(name, price)
            if self.isEmpty():
                self.head = n
                self.tail = n
            else:
                n.next = self.head #cho addfirst keets noi va dua len head(dau tien)
                self.head = n        
    # end def
#Q1-2          
    def f2(self, A):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        new_node = Node(A)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

            return
        
        curr = self.head

        if curr.data.Age % 2 == 0:
            new_node.next = curr
            self.head = new_node
            return

        curr, prev = self.head.next, self.head
        while curr:
            if curr.data.Age % 2 == 0:
                prev.next = new_node
                new_node.next = curr
                return
            prev = curr
            curr = curr.next            
        # if self.head is None:
        #     self.head 
#Q1-3
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========

        if self.isEmpty():
            return
        
        if self.head.data.Age % 2 == 0:
            self.head = self.head.next
            return
        
        curr, prev = self.head.next, self.head

        while curr:
            if curr.data.Age % 2 == 0:
                prev.next = curr.next
                return
            
            prev = curr
            curr = curr.next

    #end def
# Q1-4
    def count(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next 
        return count
    
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========

        if self.isEmpty():
            return
        
        curr = self.head

        while curr:
            n = curr.next
            while n:
                if n.data.Age % 2 == 0 and curr.data.Age % 2 == 0:
                    if n.data.Age < curr.data.Age or (n.data.Age == curr.data.Age and n.data.Salary > curr.data.Salary):
                        n.data, curr.data = curr.data, n.data
                n = n.next

            curr = curr.next
        
        # totalNode = self.count()
        
        # lst2 = []
        # cur = self.head
        # for i in range(totalNode):
        #     if i % 2 == 1:
        #         lst2.append((cur.data.Name, cur.data.Salary))
        #     cur = cur.next
        
        # lst2 = sorted(lst2, key = lambda x: x[1], reverse=True)
        # j = 0
        # cur = self.head
        # for i in range(totalNode):
        #     if i % 2 == 1:
        #         cur.data.Name = lst2[j][0]
        #         cur.data.Salary = lst2[j][1]
        #         j += 1
        #     cur = cur.next
    #end def

    