import math
from Product import *
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
    def f1(self, id=0, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        
        pass        
    # end def
#Q1-2          
    def f2(self, B):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        
        
        pass        
    # end def
#Q1-3
    def f3(self,x):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        
        
        
        pass 
    #end def
# Q1-4
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========
        
        
        
        pass
    #end def
    