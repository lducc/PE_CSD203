from BSTree import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = None
        self.obj=  None
    #end def    
    def q2(self, lineStart):
        f1 = open(self.fileName,'r')
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count == lineStart +1:
                self.obj = line
                break              
        pass 
    def readFile(self, lineStart, numberline):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart+1:                
                # listName = re.sub("\s+"," ",line.strip()).split(",")   
                listName = line.strip().split(",")             
                self.data =[listName];
            if count>lineStart+1 and count<lineStart+1+numberline: 
                # listValue = re.sub("\s+"," ",line.strip()).split(",")
                listValue = line.strip().split(",")
                self.data.append(listValue)
        f1.close()
    def display(self):
        for line in self.data:
            print(line, end ="\n")        
                # listName = line.strip().split(", ")
    def insert(self, tree):
        for i in range(len(self.data[0])):           
            tree.f1(int(self.data[0][i].strip()),self.data[1][i].strip(),int(self.data[2][i]))
    #end def       
    def createTree(self,tree,begin=0, end=0):
        self.readFile(begin, end)
        for i in range(len(self.data[0])):
            tree.f1(int(self.data[0][i].strip()),self.data[1][i].strip(),int(self.data[2][i]))
#####################            
m = Main("input.txt")
tree = BSTree()
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
print("4. Test f4 (1 mark)")
choice = int(input("Your selection (1->4)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(1,3)
    m.insert(tree)
    tree.breadth_first()
    tree.preVisit()            
elif choice ==2:
    tree.clear()
    m.createTree(tree,6,3)
    tree.inVisit()
    m.q2(5)
    x = int(m.obj)
    tree.f2(x)
elif choice ==3:
    tree.clear()
    m.q2(10)
    m.createTree(tree,11,3)   
    tree.preVisit()    
    tree.f3(int(m.obj))
    tree.preVisit()    
elif choice==4:
    tree.clear()
    m.q2(15)
    m.createTree(tree,16,3)
    tree.breadth_first()    
    tree.f4(int(m.obj))
    tree.breadth_first()
else:
    print("Wrong select")
print("FINISH")    