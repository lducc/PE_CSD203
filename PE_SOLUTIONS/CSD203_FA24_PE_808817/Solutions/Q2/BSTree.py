import math
from Product import *
from Node import *
from MyQueue import *

class BSTree:
    def __init__(self):
        self.root = None
    
    def clear(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def visit(self, p):
        if p == None:
            return
        print(f"{p.data}", end=" ")
    
    def preOrder(self, p):
        if p == None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    
    def postOrder(self, p):
        if p == None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    
    def inOrder(self, p):
        if p == None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)
    
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left != None:
                my.EnQueue(p.left)
            if p.right != None:
                my.EnQueue(p.right)
        print("")

    # Q1-1: Insert if conditions are met
    def f1(self, id, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name.startswith("G") or id > 100 or price > 100:
            return  # Do nothing if any condition is met
        
        # Create the new Product
        new_product = Product(id, name, price)
        # Insert into the BST
        if self.root is None:
            self.root = Node(new_product)
        else:
            self.root = self.insert_node(self.root, new_product)
        # ===END PART 1============================================================
    
    def insert_node(self, root, product):
        if root is None:
            return Node(product)
        
        if product.id < root.data.id:
            root.left = self.insert_node(root.left, product)
        elif product.id > root.data.id:
            root.right = self.insert_node(root.right, product)
        
        return root

    # Q1-2: Display nodes with price < x during in-order traversal
    def f2(self, x):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        def inOrder_price_check(p, x):
            if p is None:
                return
            inOrder_price_check(p.left, x)
            if p.data.price < x:
                self.visit(p)
            inOrder_price_check(p.right, x)
        
        inOrder_price_check(self.root, x)
        print("")  # New line for separation
        # ===END PART 2============================================================

    # Q1-3: Delete the first node with two children and price < x
    def f3(self, x):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        def find_and_delete(root, x):
            if root is None:
                return None, False
            
            # Check if current node meets the criteria
            if root.data.price < x and root.left and root.right:
                self.root = self.delete_node(self.root, root.data.id)
                return None, True
            
            # Recursively search in left and right subtrees
            left_result, deleted = find_and_delete(root.left, x)
            if deleted:
                return None, True
            
            right_result, deleted = find_and_delete(root.right, x)
            return None, deleted

        find_and_delete(self.root, x)
        # ===END PART 3============================================================

    def delete_node(self, root, id):
        if root is None:
            return root
        
        if id < root.data.id:
            root.left = self.delete_node(root.left, id)
        elif id > root.data.id:
            root.right = self.delete_node(root.right, id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_larger_node = self.find_min(root.right)
            root.data = min_larger_node.data
            root.right = self.delete_node(root.right, min_larger_node.data.id)
        
        return root

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Q1-4: Rotate left if node has right child and price < x
    def f4(self, x):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========
        def preorder_rotate(node, x):
            if node is None:
                return None, False
            
            # Check if node meets the rotation criteria
            if node.right and node.data.price < x:
                # Rotate node to the left
                return self.rotate_left(node), True
            
            node.left, rotated = preorder_rotate(node.left, x)
            if rotated:
                return node, True
            
            node.right, rotated = preorder_rotate(node.right, x)
            return node, rotated

        self.root, _ = preorder_rotate(self.root, x)
    
    def rotate_left(self, p):
        new_root = p.right
        p.right = new_root.left
        new_root.left = p
        return new_root
