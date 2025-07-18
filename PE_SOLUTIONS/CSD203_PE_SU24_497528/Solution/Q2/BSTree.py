import math
from Employee import *
from Node import *
from MyQueue import *
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def    
    def preVisit(self):
        self.preOrder(self.root)
        print("")        
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    def f1(self, name, age, salary=-1):        
        if name[0] == 'Y' or age < 0 or salary <= 0:
            return
        
        new_node = Node(Employee(name, age, salary))

        if self.root is None:
            self.root = new_node
            return
        self.root = self.insert(self.root, new_node)

    def insert(self, start, curr):
        if start is None:
            return curr
        
        if start.data.Age > curr.data.Age:
            start.left = self.insert(start.left, curr)

        if start.data.Age < curr.data.Age:
            start.right = self.insert(start.right, curr)
        
        return start

    def postOrder2(self,p):
        if p==None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        if p.data.Age % 2 == 0 and p.data.Salary > 20:
            self.visit(p)

    def f2(self):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        self.postOrder2(self.root)
        print("")

        
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========      
        p = self.search_f4_postorder(self.root)
        self.rotate_right(p)        
    #-----------------     
    def search_f4(self):
        if self.isEmpty():
            return
        Q = MyQueue()
        Q.EnQueue(self.root)
        count = 0
        while not Q.isEmpty():
            curr = Q.DeQueue()
            if curr.left and curr.data.Age % 2 != 0:
                count += 1
            if count == 1:
                return curr
            if curr.left is None:
                Q.EnQueue(curr.left)
            if curr.right is None:
                Q.EnQueue(p.right)
        return None
    
    def search_f4_postorder(self, node):
        if node is None:
            return None

        found_node = self.search_f4_postorder(node.left)
        if found_node: 
            return found_node

        found_node = self.search_f4_postorder(node.right)
        if found_node: 
            return found_node

        if node.left is not None and node.data.Age % 2 != 0:
            return node 

        return None    
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Age < root.data.Age:
        #Sửa data. theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        
    def rotate_right(self, node):
        if not node:                                            
            return None
        left_node = node.left                                   
        if not left_node:                                       
            return node
        left_right_node = left_node.right
        node.left = left_right_node                             
        left_node.right = node
        if node == self.root:                                   
            self.root = left_node
        else:                                                   
            parent = self._find_parent(self.root, node)         
            if parent.left == node:                             
                parent.left = left_node
            else:                                               
                parent.right = left_node
        return left_node
    
    def rotate_left(self, node):    
        if not node:                                            
            return None
        right_node = node.right                                 
        if not right_node:                                      
            return node
        right_left_node = right_node.left
        node.right = right_left_node                            
        right_node.left = node
        if node == self.root:                                   
            self.root = right_node
        else:                                                   
            parent = self._find_parent(self.root, node)         
            if parent.left == node:                             
                parent.left = right_node
            else:                                               
                parent.right = right_node
        return right_node
# end class
