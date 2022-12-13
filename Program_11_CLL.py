class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
            self.head = newNode
            
    def insert_at_middle(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode 
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head.next = newNode
            newNode.next = current.next
            
    def insert_at_end(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode 
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
        
    def deletenode(self,ele):
        if self.head == None:
            print("List is empty")
            return
        if self.head.info == ele:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            if current.next.info == ele:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current = current.next
        print("Element is not found in the list")
            
    def traverse(self):
        current = self.head
        while current.next != self.head:
            print(current.info)
            current = current.next
        print(current.info)
        
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.traverse()
print("******")
ll.insert_at_middle(15)
ll.traverse()
print("*****")
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.traverse()
print("****")
ll.deletenode(5)
ll.traverse()
print("****")
ll.deletenode(40)
ll.traverse()

