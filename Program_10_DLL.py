class Node:
    def __init__(self,info,prev=None,next=None):
        self.info = info
        self.prev = prev
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
     
    
        
    def insert_at_end(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            newNode.prev = current
            
    def deletenode(self,ele):
        if self.head == None:
            print("List is empty")
            return
        if self.head.next == None:
            if self.head.info == ele:
                temp  = self.head
                self.head = None
                temp = None
                return
            else:
                print("Element is found in our list")
                return
        
        temp = self.head.next
        while temp.next != None:
            if temp.info == ele:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
                return
            temp = temp.next
        
        if temp.info == ele:
            temp.prev.next = None
            temp = None
            return
        print("Element is not found in the list")
                    
    def display(self):
        if self.head == None:
            print("List is empty")
        current = self.head
        while current != None:
            print(current.info)
            current = current.next
            
LL = LinkedList()
LL.insert_at_beginning(10)
LL.insert_at_beginning(5)
LL.display()
print("******")
LL.insert_at_end(15)
LL.insert_at_end(20)
LL.display() 
LL.deletenode(15)
LL.deletenode(30)
LL.display()