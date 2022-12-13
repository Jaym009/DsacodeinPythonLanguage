class Node:
    def __init__(self,info,link=None):
        self.info = info
        self.link = link
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginnning(self,info):
        newNode = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode
    
    def insert_at_middle(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode    
        else:
            ptr = self.head
            length = 0
            while(ptr != None):
                ptr = ptr.link
                length += 1   
            if(length % 2 == 0):
                count = length / 2
            else:
                (length + 1) / 2
 
            ptr = self.head
            while(count > 1):
                count -= 1
                ptr = ptr.link
            newNode.link = ptr.link
            ptr.link = newNode
            
    def insert_at_end(self,info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newNode
        else:
            self.head = newNode
            
    def delete_node(self,ele):
        if self.head == None:
            print("List is empty")
            return
        if self.head.info == ele:
            temp = self.head 
            self.head = temp.link
            temp = None
            return 
        current = self.head
        while current.link != None:
            if current.link.info == ele:
                temp = current.link 
                current.link = temp.link
                temp = None
                return
            current = current.link
        print("Element is not found in the list")
        
    def search(self,ele):
        if self.head == None:
            print("List is Empty")
            return
        current = self.head
        while current != None:
            if current.info == ele:
                print("Element is found in list")
                return 
            current = current.link            
    def display(self):
        if self.head == None:
            print("Empty list")
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.link
LL = LinkedList()
LL.insert_at_beginnning(10)
LL.insert_at_beginnning(5)
LL.display()
print("***************")
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.display()
LL.insert_at_middle(8)
LL.delete_node(40)
LL.delete_node(30)
LL.delete_node(8)
LL.display()
LL.search(20)
